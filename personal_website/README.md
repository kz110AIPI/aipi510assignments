# Personal Website with Flask on Google Cloud Platform (GCP)

This project is a personal website built using Flask to showcase education, work experience, skills, and publications. The website is deployed on Google Cloud Platform (GCP) for easy access and professional presentation.

## Table of Contents
1. [Features](#features)
2. [Getting Started](#getting-started)
3. [Running the Application Locally](#running-the-application-locally)
4. [Deployment on Google Cloud Platform (GCP)](#deployment-on-google-cloud-platform-gcp)

---

## Features
- Organized layout with sections for Home, Education, Experience, Skills, and Publications.
- Responsive design elements for compatibility across different screen sizes.
- Deployed on Google Cloud Platform, making the website accessible globally.

---


## Getting Started

### Prerequisites
- **Python 3.11**: Make sure Python is installed on your system. [Download Python here](https://www.python.org/downloads/).
- **Google Cloud SDK**: Required to deploy and manage the project on GCP. [Install the Google Cloud SDK](https://cloud.google.com/sdk/docs/install).

### Installation
1. Clone the repository:
   
   git clone Git Repository Link
   cd your-repo-name

2. Install dependencies:
    pip install -r requirements.txt

3. Running the Application Locally
To test the website locally:

4. Start the Flask application:

python app.py

5. Open your browser and navigate to http://127.0.0.1:5000 to view the website.

## Deployment on Google Cloud Platform (GCP)
1. Steps for Deploying on Google App Engine
Set up your GCP Project:

2. Go to the Google Cloud Console.
Create a new project or select an existing one.
Enable Google App Engine and set the region.

3. Deploy the App:

Authenticate your GCP account by running:

gcloud config set project [YOUR_PROJECT_ID]

gcloud app deploy

This command will upload the project files to GCP and deploy the app on App Engine.

4. Visit Your Website:

Once deployed, you can access your website at https://[YOUR_PROJECT_ID].appspot.com.