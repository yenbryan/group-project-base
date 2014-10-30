import json
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# @login_required
# def profile(request):
#     return render(request, 'account.html')


# Registration
# from slides.forms import ProfileForm, UpdateProfileForm
from django.views.decorators.csrf import csrf_exempt
from slides.forms import ProfileForm, UpdateUserImageForm
from slides.models import Profile


@login_required
def account(request):
    if request.method == 'POST':
        imageform = UpdateUserImageForm(request.POST, request.FILES, instance=request.user)
        if imageform.is_valid():
            imageform.save()
    else:
        imageform = UpdateUserImageForm()
    return render(request, 'account.html', {
        'imageform': imageform,
    })


@csrf_exempt
def edit_name(request):
    status = None
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            request.user.real_name = data
            request.user.save()
            status = "success"
    response = status
    return HttpResponse(json.dumps(response),
                        content_type='application/json')


@csrf_exempt
def edit_email(request):
    status = None
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            validate_email(data)
            request.user.email = data
            request.user.save()
            status = "success"
        except ValidationError:
            pass
    response = status
    return HttpResponse(json.dumps(response),
                        content_type='application/json')


@csrf_exempt
def edit_password(request):
    status = None
    if request.method == 'POST':
        data = json.loads(request.body)
        if not data[0] == data[1]:                    #check passwords are correctly repeated
            status = "mismatch"
        elif data[0]:
            user = request.user
            user.set_password(data[1])
            user.save()
            status = "success"
            update_session_auth_hash(request, user)
    response = status
    return HttpResponse(json.dumps(response),
                        content_type='application/json')


@csrf_exempt
def edit_photo(request):
    status = None
    if request.method == 'POST':
        data = json.loads(request.body)
        request.user.photo = data
        request.user.save()
        status = "success"
    response = status
    return HttpResponse(json.dumps(response),
                        content_type='application/json')


def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            form.save()
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("slides_home")
    else:
        form = ProfileForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


@csrf_exempt
def new_help(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print data