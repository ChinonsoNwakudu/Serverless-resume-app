<<<<<<< HEAD
# serverless-resume-app
My personal resume website using serverless technologies, with backend APIs to fetch and update the resume data.

### My frontend is live here

# First Steps (Static Resume Website)
My frontend folder contains my static website. The static resume website is built using HTML and CSS. It is hosted on Azure Blob Storage with static website hosting enabled.

### Steps to Deploy:
=======
# Serverless-resume-app
My personal resume website using serverless technologies, with backend APIs to fetch and update the resume data.

### Project Structure
```
serverless-resume-app/
├── .github/
│   └── workflows/
│        └── deploy.yml   # GitHub Actions pipeline
├── api/
│   └── function_app/     # Azure Functions (backend)
├── frontend/
│   ├── index.html        # Static HTML for resume
│   └── style.css         # CSS for styling
└── README.md             # Project documentation
```
### Tools & Technologies:

1. Azure Functions for serverless backend.
2. Cosmos DB to store resume data.
3. Blob Storage for static website hosting.
4. Azure API Management to expose APIs.
5. GitHub Actions for CI/CD pipeline.
6. Infrastructure as Code (IaC) using Terraform or ARM templates.


### My frontend is live here

### First Steps (Static Resume Website)
My frontend folder contains my static website. The static resume website is built using HTML and CSS. It is hosted on Azure Blob Storage with static website hosting enabled.

#### Steps to Deploy:
>>>>>>> function app files and CI/CD pipeline
1. Created a storage account in [Azure](https://aka.ms/azureportal).
2. Enabled static website hosting.
3. Uploaded my frontend files: `index.html`, `main.js` and `css files` to the `$web` container.
4. Accessed the website using the **Primary Endpoint URL**.
<<<<<<< HEAD
- For more details on how to deploy a static website to Azure storage, check out my [Medium](https://medium.com/@ChinonsoNwakudu/deploy-a-static-website-on-azure-storage-8e03ff35a621) blog!
=======
- For more details on how to deploy a static website to Azure storage, check out my [Medium](https://medium.com/@ChinonsoNwakudu/deploy-a-static-website-on-azure-storage-8e03ff35a621) blog!

###
>>>>>>> function app files and CI/CD pipeline
