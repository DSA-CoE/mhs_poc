from datetime import datetime

from django.http import HttpResponseRedirect
from django.urls import reverse


class BlockExpiredAccounts:
    """
    Django middleware to handle page access according to account expiry date.
    If a user's account_expiry field is less than today's date, redirect to account expiry page.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        expiry_path = reverse("account_expired")
        logout_path = reverse("logout")

        # If an account is logged in
        if request.user.is_authenticated and request.path not in [
            expiry_path,
            logout_path,
        ]:
            expiry_date = request.user.account_expiry
            todays_date = datetime.today().date()

            if todays_date > expiry_date:
                return HttpResponseRedirect(expiry_path)

        return self.get_response(request)
