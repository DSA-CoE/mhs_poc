# Django Admin Honeypot

It is common knowledge that `/admin` is the endpoint to access the admin page of a Django app. To monitor any malicious attempts to log into this endpoint, we can setup a [honeypot](<https://en.wikipedia.org/wiki/Honeypot_(computing)>) admin page while the real admin page URL is kept secret amongst those with access.

This is made possible by [django-admin-honeypot](https://github.com/dmpayton/django-admin-honeypot).

This template has already have this set up. Few things to note/modify based on your own specific requirements:

## Setting up your secret admin page URL

In `config/settings/base.py` there is a variable `ADMIN_URL` which specifies the endpoint for the real admin page. Configure this to set up your own agreed endpoint name for the real admin page.

## Email admins on attempted log in through the 'fake' admin

In `config/settings/base.py` there is a variable `ADMIN_HONEYPOT_EMAIL_ADMINS` (which is set to `True`) that toggles the app to email all `ADMINS` of the application if there's an attempt of a break-in login through the 'fake' honeypot admin login page.
