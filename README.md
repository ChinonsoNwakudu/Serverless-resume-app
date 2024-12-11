# Serverless Resume API
This project is a Serverless Resume API that provides a JSON representation of my resume. It also tracks the number of times the JSON resume has been accessed. The application uses Azure technologies such as Azure Cosmos DB for storage, Azure Function App for backend logic, and GitHub Actions for Continuous Integration/Continuous Deployment (CI/CD).

#### View the JSON Resume API 
👉 [Click here to view the API](https://nonsoresumeapp.azurewebsites.net/api/get_resume?code=Ki0Aq2oiYZj5pZWWVhXsaZNe1tNT6UK2EPEF3Q6DewvaAzFuSfpehA%3D%3D&&api_type=get-resume&resume_id=1)

### Project Structure
```
serverless-resume-app/
├── .github/
│   └── workflows/
│        └── deploy.yml       # GitHub Actions pipeline
├── api/
│   └── function_app/         # Azure Functions (backend)
         └── function_app.py  # Main Function code
         └── host.json        # Dependencies
└── README.md             # Project documentation
```
### Features
1. JSON Resume API: Displays your resume in JSON format.
2. Visitor Counter: Tracks and displays the number of times the resume JSON is accessed.
3. Serverless Architecture: Built on Azure Functions for scalability and cost efficiency.
4. CI/CD Pipeline: Automated deployments using GitHub Actions.


### Architecture Overview:

1. Azure Cosmos DB: Stores the JSON resume and visitor count.
2. Azure Function App: Handles API requests for fetching the JSON resume and updating the visitor counter.
3. GitHub Actions: Automates the deployment of the Function App and other resources.

### Prerequisites
Before you begin, ensure you have the following:
1. An active Azure Subscription.
2. Azure CLI installed on your local machine.
3. Python 3.9+ installed. (3.11 is recommended)
4. A GitHub account with a repository for this project containing Python code.

### Setup Guide
#### 1. Create the Azure Resources
##### a. Create an Azure Cosmos DB Instance
1. Log in to the [Azure Portal](https://aka.ms ).
2. Search for Cosmos DB and create a new account with the following settings:
    - API: Core (SQL) API.
    - Region: Select a region close to you or based on your preferences
3. Once created, create a database (e.g., ResumeDB) and a container (e.g., ResumeContainer).
     - Set a partition key (e.g., /id).

##### b. Create an Azure Function App
1. In the Azure Portal, create a Function App with the following settings:
     - Runtime stack: Python.
     - Operating System: Linux.
     - Plan type: Consumption (Serverless).
2. Configure the app to connect to the Cosmos DB instance:
     - Add a connection string for Cosmos DB in the Application Settings of the Function App.
##### b. Create an Azure Function App
1. In the Azure Portal, create a Function App with the following settings:
    - Runtime stack: Python.
    - Operating System: Linux.
    - Plan type: Consumption (Serverless).
2. Configure the app to connect to the Cosmos DB instance:
    - Add a connection string for Cosmos DB in the Application Settings of the Function App.
#### 2. Initialize the Project     
##### a. Clone the Repository   
```
  git clone <repository-url>
  cd <project-directory>
```
##### b. Install Dependencies
```
   pip install -r requirements.txt
```
#### 3. Write the Function App Code   
##### a. JSON Resume API
- Create an HTTP-triggered Azure Function to:
   1. Retrieve the JSON resume from Cosmos DB.
   2. Increment the visitor count in the database.
   3. Return the JSON resume along with the visitor count.

An Example of my python code for my function app is above (function_app.py).

#### 4. Deploy Using GitHub Actions

##### a. Generate a Workflow File from Azure Deployment Center

1. Open the Azure Portal and navigate to your Function App.

2. Under the Deployment section in the left menu, select Deployment Center.

3. Choose GitHub as your source control provider.

4. Authenticate with your GitHub account and select your repository and branch.

5. Choose the Python stack and follow the prompts to generate the workflow file.

6. The generated file will be committed to your GitHub repository under .github/workflows/.

A sample workflow is above in my ```.github/workflows/ ``` folder in my repo above.

##### b. Add Secrets to GitHub

- Add the following secrets to your GitHub repository:

    - AZURE_CREDENTIALS: JSON credentials for Azure service principal.

    - COSMOS_DB_CONNECTION_STRING: Connection string for Cosmos DB.

A sample workflow is above in my ```.github/workflows/ ``` folder in my repo above.

#### 5. Test the API

1. Access your Function App's endpoint in a browser or API client (e.g., Postman):

2. Verify that the JSON resume and visitor count are displayed.


## Future Enhancements
- Add a frontend to display the JSON resume and visitor counter visually.

- Implement caching for better performance.

- Add authentication to restrict access to the API.

## Contributing
Contributions are welcome! Please create a pull request for any changes.

## License

This project is licensed under the MIT License.