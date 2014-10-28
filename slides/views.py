import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
# @login_required
# def profile(request):
#     return render(request, 'profile.html')


# Registration
# from slides.forms import ProfileForm, UpdateProfileForm
from django.views.decorators.csrf import csrf_exempt
from slides.forms import ProfileForm
from slides.models import Profile, Action


@login_required
def profile(request):
    return render(request, 'profile.html')


# def edit_account(request):
#     args = {}
#
#     if request.method == 'POST':
#         form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
#         form.actual_user = request.user
#         if form.is_valid():
#             password1 = form.cleaned_data['password1']
#             password2 = form.
#             form.save()
#             return HttpResponseRedirect(reverse('update_profile_success'))
#     else:
#         form = UpdateProfileForm()
#
#     args['form'] = form

# def edit_account(request):
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST, request.FILES)
#         user = request.user
#         if form.is_valid():
#             image = form.cleaned_data['image']
#             real_name = form.cleaned_data['real_name']
#             password1 = form.cleaned_data['password1']
#             password2 = form.cleaned_data['password2']
#             email = form.cleaned_data['email']
#             if password1 == password2 and password1 != "":
#                 user.password = user.set_password(password1)
#                 user.email = email
#                 user.image = image
#                 user.real_name = real_name
#                 user.save()
#                 return redirect("slides_home")
#     else:
#         form = UserChangeForm()
#     return render(request, 'edit_account.html',
#         {'form': form}
#     )

def edit_account(request):
    # if request.method == 'POST':
    #     user = request.user
    #     form = UserChangeForm(request.POST, request.FILES, instance=user)
    #     if form.is_valid():
    #         image = form.cleaned_data['image']
    #         real_name = form.cleaned_data['real_name']
    #         password1 = form.cleaned_data['password1']
    #         password2 = form.cleaned_data['password2']
    #         email = form.cleaned_data['email']
    #         if password1 == password2 and password1 != "":
    #             user.password = user.set_password(password1)
    #             user.email = email
    #             user.image = image
    #             user.real_name = real_name
    #             user.save()
    #             return redirect("slides_home")
    # else:
    #     form = UserChangeForm()
    return render(request, 'edit_account.html',
        # {'form': form}
    )

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
