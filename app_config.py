import os

CLIENT_ID = "15992c9e-f146-4863-b4cc-dd56c87635a7" # Application (client) ID of app registration

CLIENT_SECRET = "jpC8Q~Kr67PugFQsieU8XlqLCzfheAwuD0E4ldiD" # Placeholder - for use ONLY during testing.
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET") 
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/9fbb6e1b-461f-4bb4-8682-f983c2b5e297"

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/me/messages?$select=subject'  # This resource requires no admin consent
# ENDPOINT = "https://graph.microsoft.com/v1.0/me/drive/items/133FAAFED94B0D4B!125/workbook/worksheets"  # This resource requires no admin consent
# ENDPOINT = "https://graph.microsoft.com/v1.0/teams"  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All", "Mail.Read", "Mail.ReadBasic", "Mail.ReadWrite", "MailboxSettings.Read", "MailboxSettings.ReadWrite", "Files.Read", "Files.Read.All", "Files.ReadWrite", "Files.ReadWrite.All", "Team.Create"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
