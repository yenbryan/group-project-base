import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from slides.forms import ProfileForm
from slides.models import Profile, Slide, Action, Question


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def test(request):
    return render(request, 'test.html')


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
        student = Profile.objects.get(username=request.user.username)
        current_slide = Slide.objects.get(url=data['slide'])
        Action.objects.get_or_create(need_help=True, profile=student, slide=current_slide)
        return HttpResponse(content_type='application/json')


@csrf_exempt
def new_done(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student = Profile.objects.get(username=request.user.username)
        current_slide = Slide.objects.get(url=data['slide'])
        Action.objects.get_or_create(done=True, profile=student, slide=current_slide)
        return HttpResponse(content_type='application/json')


@csrf_exempt
def new_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student = Profile.objects.get(username=request.user.username)
        current_slide = Slide.objects.get(url=data['slide'])
        Question.objects.get_or_create(profile=student, slide=current_slide, body=data['text'])
        return HttpResponse(content_type='application/json')


def teacher(request, week, day, am_pm):
    deck = Slide.objects.filter(week=week, day=day, am_pm=am_pm)
    return HttpResponse(deck)
