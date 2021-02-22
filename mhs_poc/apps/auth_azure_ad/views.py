from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def account_expired_view(request):
    return render(request, template_name="auth/pages/account_expired.html")
