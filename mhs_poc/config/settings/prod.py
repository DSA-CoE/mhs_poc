# Ensure that CSRF cookies are only sent with an HTTPS connection.
# Docs: https://docs.djangoproject.com/en/3.1/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True

# Ensure that session cookies are only sent with an HTTPS connection.
# Docs: https://docs.djangoproject.com/en/3.1/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True

# Prevent rendering of the page if a Cross-site Scripting (XSS) attack is detected.
# Docs: https://docs.djangoproject.com/en/3.1/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Redirect all non-HTTPS requests to HTTPS.
# Docs: https://docs.djangoproject.com/en/3.1/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = True

# Block connection for the given time period
# if not properly serving HTTPS resources, or if certificate expires.
# Docs: https://docs.djangoproject.com/en/3.1/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_SECONDS = 86400  # 1 day
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Elasticsearch Config
ELASTICSEARCH_CONFIG = {
    "host": "localhost",
    "port": 9200,
    "username": "",
    "password": "",
}

# Enable brute force login lock
AXES_ENABLED = True
AXES_FAILURE_LIMIT = 5
