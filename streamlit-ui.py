import os
from bs4 import BeautifulSoup
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv, find_dotenv
from weasyprint import HTML
import pdfkit

# Load environment variables from .env file
load_dotenv(find_dotenv('credential.env'), override=True)

# Function to convert HTML to PDF using WeasyPrint
def convert_url_to_pdf(url, output_path):
    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'encoding': "UTF-8",
        'no-outline': None
    }
    try:
        pdfkit.from_url(url, output_path, options=options)
        print(f"PDF created successfully: {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to upload PDF to Azure Blob Storage
def upload_to_azure_blob(file_path, container_name, blob_name, connection_string):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"Uploaded {file_path} to Azure Blob Storage")
    except Exception as e:
        print(f"Error uploading PDF to Azure Blob Storage: {e}")
        raise

# Main function
def main():
    url = "https://www.mobil.co.th/th-th/our-products#t=https%3A%2F%2Fwww.mobil.co.th%2Fth-th%2Four-products&sort=relevancy"  # Replace with your target URL
    output_pdf = "output2.pdf"
    
    convert_url_to_pdf(url, output_pdf)

if __name__ == "__main__":
    main()
