from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import email
import pickle
import os



# Define the Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    # Check if token.pickle exists (it stores access tokens)
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If credentials are invalid or missing, prompt login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials for next use
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def list_emails():
    creds = authenticate_gmail()  # ✅ Ensure authentication before using Gmail API
    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(userId='me', maxResults=50).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No emails found.")
        return

    print("\n📩 **Filtered Emails (Business & Professional)** 📩\n")

    important_senders = ["linkedin.com", "naukri.com", "indeed.com", "glassdoor.com", "yourcompany.com"]
    important_subjects = ["Meeting", "Job Offer", "Invoice", "Interview", "Business Proposal"]

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = msg_data['payload']
        headers = payload['headers']

        sender = subject = snippet = "Unknown"

        for header in headers:
            if header['name'] == 'From':
                sender = header['value']
            if header['name'] == 'Subject':
                subject = header['value']

        snippet = msg_data.get('snippet', '')

        if any(sender.lower().endswith(domain) for domain in important_senders) or \
           any(keyword.lower() in subject.lower() for keyword in important_subjects):
            print(f"📧 **From:** {sender}")
            print(f"📌 **Subject:** {subject}")
            print(f"📝 **Snippet:** {snippet[:100]}...")  
            print("-" * 50)

if __name__ == '__main__':
    list_emails()
