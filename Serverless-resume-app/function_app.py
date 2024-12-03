
import os
import azure.functions as func
import logging
import json
from azure.cosmos import CosmosClient, exceptions

# Environment Variables
cosmos_url = os.getenv("CosmosDB_URL")
cosmos_key = os.getenv("CosmosDB_Key")
database_name = os.getenv("CosmosDB_Database")
resume_container_name = os.getenv("CosmosDB_Container")
visitor_count_container_name = os.getenv("VisitorCount_Container")

# Initialize Cosmos DB Clients
cosmos_client = CosmosClient(cosmos_url, credential=cosmos_key)
database = cosmos_client.get_database_client(database_name)
resume_container = database.get_container_client(resume_container_name)
visitor_count_container = database.get_container_client(visitor_count_container_name)

# Function App Initialization
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# Metadata Filter Helper
def filter_metadata(item):
    """Removes unnecessary metadata from Cosmos DB items."""
    keys_to_remove = ["_rid", "_self", "_etag", "_attachments", "_ts"]
    return {key: value for key, value in item.items() if key not in keys_to_remove}

# Increment Visitor Counter Logic
def get_and_update_visitor_count():
    """Fetches and increments the visitor count from Cosmos DB."""
    visitor_count_item_id = 'visitor-count'  # Fixed ID for visitor count
    try:
        # Fetch the visitor count
        visitor_count_item = visitor_count_container.read_item(item=visitor_count_item_id, partition_key=visitor_count_item_id)
        current_count = visitor_count_item.get('count', 0)
    except exceptions.CosmosResourceNotFoundError:
        # Initialize the count if the item doesn't exist
        current_count = 0

    # Increment and update the count
    new_count = current_count + 1
    visitor_count_container.upsert_item({'id': visitor_count_item_id, 'count': new_count})
    return new_count

# Fetch Resume Data
def get_resume_data(resume_id):
    """Fetches resume data from Cosmos DB using the provided ID."""
    try:
        # Fetch the resume item
        resume_item = resume_container.read_item(item=resume_id, partition_key=resume_id)
        return filter_metadata(resume_item)
    except exceptions.CosmosResourceNotFoundError:
        return None

# Handle API Requests
@app.route(route="get_resume")
def handle_request(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing API request.')

    try:
        # Extract api_type and optional resume ID from query string
        api_type = req.params.get('api_type')
        resume_id = req.params.get('resume_id')  # For fetching specific resume data

        if not api_type or api_type != "get-resume":
            return func.HttpResponse("Invalid or missing 'api_type'. Use 'get-resume'.", status_code=400)

        if not resume_id:
            return func.HttpResponse("Please provide 'resume_id' in the query string.", status_code=400)

        # Increment visitor counter
        visitor_count = get_and_update_visitor_count()

        # Fetch resume data
        resume_data = get_resume_data(resume_id)
        if resume_data is None:
            return func.HttpResponse(f"Resume with ID '{resume_id}' not found.", status_code=404)

        # Create combined response
        response = {
            "visitorCount": visitor_count,
            "resumeData": resume_data
        }

        return func.HttpResponse(
            body=json.dumps(response, indent=2),
            status_code=200,
            mimetype="application/json"
        )

    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"Cosmos DB error: {str(e)}")
        return func.HttpResponse("Error interacting with Cosmos DB.", status_code=500)

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return func.HttpResponse("An unexpected error occurred.", status_code=500)
