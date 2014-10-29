import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, ObjectDoesNotExist
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
def new_action(request, action):
    if request.method == 'POST':
        data = json.loads(request.body)
        student = Profile.objects.get(username=request.user.username)
        week = int(data['week'])
        am_pm = int(data['am_pm'])
        slide_number = int(data['slide_number'])
        new_slides = Slide.objects.filter(week=week, day=data["day"])
        print new_slides
        day = data['day']
        our_url = "week"+str(week)+"/"+day+"/#/"+str(slide_number)
        print our_url
        current_slide = Slide.objects.get(url=our_url)
        print current_slide
        # HELP
        if int(action) == 1:
            Action.objects.get_or_create(need_help=True, profile=student, slide=current_slide)
        # DONE
        elif int(action) == 2:
            try:
                help_action = Action.objects.get(need_help=True, profile=student, slide=current_slide)
                help_action.done = True
                help_action.need_help = False
                help_action.save()
            except ObjectDoesNotExist:
                Action.objects.get_or_create(done=True, profile=student, slide=current_slide)
        # QUESTION
        elif int(action) == 3:
            Question.objects.get_or_create(profile=student, slide=current_slide, body=data['text'])

    return HttpResponse(content_type='application/json')


def teacher(request, week, day, am_pm):
    deck = Slide.objects.filter(week=int(week), day=str(day))
    deck.filter(am_pm=am_pm)
    data = {
        "deck": deck
    }
    return render(request, "teacher.html", data)

def teacher_help(request):
    students = Profile.objects.all()
    help = Action.objects.filter(need_help=True, done=False)
    data = {'help': help, 'students': students}
    return render(request, 'teacher/help.html', data)


def teacher_done(request):
    students = Profile.objects.all()
    done = Action.objects.filter(done=True)
    data = {'done': done, 'students': students}
    return render(request, 'teacher/done.html', data)


def teacher_question(request):
    students = Profile.objects.all()
    question = Question.objects.all()
    data = {'question': question, 'students': students}
    return render(request, 'teacher/questions.html', data)


@csrf_exempt
def change_action(request, action):
    if request.method == 'POST':
        data = json.loads(request.body)
