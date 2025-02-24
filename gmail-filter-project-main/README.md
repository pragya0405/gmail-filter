# Gmail Filter Project  

A Python-based tool that uses the Gmail API to filter and retrieve important emails based on business and professional preferences. It ensures secure authentication via OAuth 2.0 and allows customization of filters for better email management.  

##  Features  

- **Gmail API Integration** – Access and filter emails from Gmail.  
- **Keyword-based Filtering** – Extract emails based on specific business-related keywords.  
- **OAuth 2.0 Authentication** – Secure login via Google OAuth.  
- **Automated Email Sorting** – Categorize important emails for better management.  

## Setup Instructions  

### ✅ Prerequisites  

- Install **Python (3.x)**  
- Install required dependencies:  
  pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
    

### Enable Gmail API & Get Credentials  

1. Go to **Google Cloud Console** → Create a new project.  
2. Enable **Gmail API** under "APIs & Services".  
3. Create **OAuth Credentials (OAuth Client ID)**.  
4. Download `credentials.json` and place it in your project folder.  
5. **Do not push this file to GitHub** to prevent exposing sensitive information.  

### Secure Credentials Handling  

- Add `credentials.json` and `token.json` to your `.gitignore` file:  
  credentials.json
  token.json
  
## ▶ Run the Project  

1. Clone or download the repository.  
2. Move to the project directory.  
3. Run the script:  
   python gmail_filter.py
4. The tool will authenticate with Gmail and fetch filtered emails.  

## Technologies Used  

- **Python**  
- **Google Gmail API**  
- **OAuth 2.0 Authentication**  

##  Author  

Developed by **Pragya**  
GitHub: [pragya0405](https://github.com/pragya0405)  



