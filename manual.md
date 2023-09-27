# BigHead Solutions LLC Website Deployment Guide

This guide provides step-by-step instructions on how to deploy the BigHead Solutions LLC website to Azure. The website is built using Python and Flask framework.

## Prerequisites

Before you begin, make sure you have the following:

- An Azure account
- Azure CLI installed on your local machine
- Python 3.x installed on your local machine
- Git installed on your local machine

## Step 1: Clone the Repository

1. Open a terminal or command prompt.
2. Change to the directory where you want to clone the repository.
3. Run the following command to clone the repository:

   ```
   git clone https://github.com/your-username/bighead-solutions-website.git
   ```

## Step 2: Create an Azure Web App

1. Open the Azure portal (https://portal.azure.com).
2. Sign in with your Azure account.
3. Click on "Create a resource" and search for "Web App".
4. Click on "Web App" and then click on "Create".
5. Fill in the required details for the web app, such as the name, resource group, and app service plan.
6. Click on "Review + create" and then click on "Create" to create the web app.

## Step 3: Deploy the Website to Azure

1. Open a terminal or command prompt.
2. Change to the directory where you cloned the repository.
3. Run the following command to log in to Azure:

   ```
   az login
   ```

4. Follow the instructions to authenticate with your Azure account.
5. Run the following command to set the Azure subscription:

   ```
   az account set --subscription <subscription-id>
   ```

   Replace `<subscription-id>` with your Azure subscription ID.

6. Run the following command to deploy the website to Azure:

   ```
   az webapp up --sku F1 --name <web-app-name> --location <location>
   ```

   Replace `<web-app-name>` with the name of your Azure web app, and `<location>` with the desired Azure region.

7. Wait for the deployment to complete. This may take a few minutes.

## Step 4: Configure Verbose Logging

1. Open the Azure portal (https://portal.azure.com).
2. Sign in with your Azure account.
3. Navigate to your web app.
4. Click on "Configuration" under the "Settings" section.
5. Scroll down to the "Application settings" section.
6. Click on "New application setting" and add the following key-value pair:

   - Key: `FLASK_ENV`
   - Value: `development`

7. Click on "Save" to save the configuration.

## Step 5: Verify the Website

1. Open a web browser.
2. Enter the URL of your Azure web app.
3. You should see the main page of the BigHead Solutions LLC website.

## Conclusion

Congratulations! You have successfully deployed the BigHead Solutions LLC website to Azure. The website is now live and accessible to users.