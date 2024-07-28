from django.contrib.auth import login, authenticate, logout
from utils.validators import register_errors, create_user
from django.views.decorators.http import require_POST
from utils.emails import send_email_register
from utils.messages import error_message
from django.shortcuts import redirect


# Create your views here.
@require_POST
def register_user(request):
    user = request.user
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    password_confirm = request.POST.get("password_confirm")

    if register_errors(request, username, email, password, password_confirm):
        return redirect("inicio")

    user = create_user(user, username, email, password)

    send_email_register(username, email)

    login(request, user)

    return redirect("inicio")


@require_POST
def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)

    if user == None:
        error_message(request, "account_not_exist")
        return redirect("inicio")

    login(request, user)

    return redirect("inicio")


def log_out_user(request):
    logout(request)

    return redirect("inicio")
