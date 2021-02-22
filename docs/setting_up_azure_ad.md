# How to set up Azure AD

To properly set up an Azure AD django app, there are several steps to be completed:

1. Set up an Azure AD app. Follow the steps outlined [here](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
2. In your Azure app, navigate to 'Certificates and Secrets'. Generate a new App ID and Key.
3. Populate the secrets.env.enc file with the following values:

```
MICROSOFT_AUTH_CLIENT_ID={The Client ID - obtained in the Azure AD app overview}
MICROSOFT_AUTH_CLIENT_SECRET={The client secret you generated}
MICROSOFT_AUTH_TENANT_ID={The tenant ID - obtained in the Azure AD app overview}
```

**IMPORTANT**: To have users log into the application via Azure AD properly, you **must** do the following:

1. **Their user account has to be created via Django admin first** (can't be improved in the future).
2. The user account's **email must match** the email in Azure AD.
