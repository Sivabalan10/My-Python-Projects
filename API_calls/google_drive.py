import os
import io
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

# If modifying these scopes, delete the token.pickle file.
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    """Authenticate and return a Google Drive API service instance."""
    creds = None
    # Load credentials from token.pickle if available
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If no valid credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for future use
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('drive', 'v3', credentials=creds)

def create_folder(service, folder_name, parent_id=None):
    """Create a folder on Google Drive."""
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    if parent_id:
        file_metadata['parents'] = [parent_id]
    folder = service.files().create(body=file_metadata, fields='id').execute()
    print(f"Folder '{folder_name}' created with ID: {folder.get('id')}")
    return folder.get('id')

def upload_file(service, file_path, mime_type, parent_id=None):
    """Upload a file to Google Drive."""
    file_metadata = {'name': os.path.basename(file_path)}
    if parent_id:
        file_metadata['parents'] = [parent_id]
    media = MediaFileUpload(file_path, mimetype=mime_type)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File '{file_path}' uploaded with ID: {file.get('id')}")
    return file.get('id')

def download_file(service, file_id, destination):
    """Download a file from Google Drive."""
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(destination, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        if status:
            print(f"Download {int(status.progress() * 100)}%.")
    fh.close()
    print(f"File downloaded to {destination}")

def delete_file(service, file_id):
    """Delete a file or folder from Google Drive."""
    service.files().delete(fileId=file_id).execute()
    print(f"Deleted item with ID: {file_id}")

def main():
    # Authenticate and build the Drive service
    service = authenticate()

    # Example operations:

    # 1. Create a folder
    folder_id = create_folder(service, 'MyTestFolder')

    # 2. Upload a file into the folder (ensure 'test.txt' exists in your directory)
    file_id = upload_file(service, 'test.txt', 'text/plain', parent_id=folder_id)

    # 3. Download the file
    download_file(service, file_id, 'downloaded_test.txt')

    # 4. Delete the uploaded file
    delete_file(service, file_id)

    # 5. Delete the folder
    delete_file(service, folder_id)

if __name__ == '__main__':
    main()
