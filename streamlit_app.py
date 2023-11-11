import streamlit as st
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

def download_file_from_google_drive(file_id):
    """Downloads a file from Google Drive.

    Args:
        file_id: The ID of the file to download.

    Returns:
        A bytes object containing the contents of the file.
    """

    service = build('drive', 'v3')

    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False

    
while done is
 
False:
        _, done = downloader.next_chunk()

    return fh.getvalue()

# Get the ID of the CSV file on Google Drive from the user
file_id = st.text_input("Enter the ID of the CSV file on Google Drive:")

# Download the CSV file from Google Drive
csv_bytes = download_file_from_google_drive(file_id)

# Create a Pandas DataFrame from the CSV bytes
df = pd.read_csv(csv_bytes)

# Display the head of the DataFrame
st.write(df.head())