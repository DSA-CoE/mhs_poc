from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home_view(request):
    return render(request, template_name="base/pages/home.html")


@login_required(login_url="/login/")
def profile_view(request):
    # user_profile_object = get_object_or_404(UserProfile, user=request.user)
    # team_object = user_profile_object.teams.get()
    # department_object = team_object.departments.get()

    context = {
        "email": request.user,
        # "team": team_object,
        # "department": department_object,
    }

    return render(request, "base/pages/profile.html", context)
