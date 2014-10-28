from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from lms import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url("^$", TemplateView.as_view(template_name="index.html"), name="slides_home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/$', 'slides.views.profile', name='profile'),
    url(r'^test/$', 'slides.views.test', name='test'),
    url(r'^register/$', 'slides.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

# ajax call
    url(r'^edit/name/$', 'slides.views.edit_name', name='edit_name'),
    url(r'^edit/email/$', 'slides.views.edit_email', name='edit_email'),
    # url(r'^help/(?P<student_real_name>\w+)/(?P<current_slide>\w+)/$', 'slides.views.new_help', name='new_help'),
    url(r'^help/', 'slides.views.new_help', name='new_help'),

    # Week 1 - OO Python
    url("^week1/1/$", TemplateView.as_view(template_name="week1/1.html"), name="week1_day1"),
    url("^week1/2/$", TemplateView.as_view(template_name="week1/2.html"), name="week1_day2"),
    url("^week1/3/$", TemplateView.as_view(template_name="week1/3.html"), name="week1_day3"),
    url("^week1/4_am/$", TemplateView.as_view(template_name="week1/4_am.html"), name="week1_day4_am"),
    url("^week1/4_pm/$", TemplateView.as_view(template_name="week1/4_pm.html"), name="week1_day4_pm"),

    # Week 2 - DB Intro + Introductory Django
    url("^week2/1_am/$", TemplateView.as_view(template_name="week2/1_am.html"), name="week2_day1_am"),
    url("^week2/1_pm/$", TemplateView.as_view(template_name="week2/1_pm.html"), name="week2_day1_pm"),
    url("^week2/2_am/$", TemplateView.as_view(template_name="week2/2_am.html"), name="week2_day2_am"),
    url("^week2/2_pm/$", TemplateView.as_view(template_name="week2/2_pm.html"), name="week2_day2_pm"),
    url("^week2/3_am/$", TemplateView.as_view(template_name="week2/3_am.html"), name="week2_day3_am"),
    url("^week2/3_pm/$", TemplateView.as_view(template_name="week2/3_pm.html"), name="week2_day3_pm"),
    url("^week2/4_am/$", TemplateView.as_view(template_name="week2/4_am.html"), name="week2_day4_am"),
    url("^week2/4_pm/$", TemplateView.as_view(template_name="week2/4_pm.html"), name="week2_day4_pm"),
    url("^week2/5_am/$", TemplateView.as_view(template_name="week2/5_am.html"), name="week2_day5_am"),
    url("^week2/5_pm/$", TemplateView.as_view(template_name="week2/5_pm.html"), name="week2_day5_pm"),

    # Start Project Cheatsheet
    url("^start_project_cheatsheet/$", TemplateView.as_view(template_name="start_project.html"), name="start_project"),

    # Week 3 - Introductory Django
    url("^week3/1_am/$", TemplateView.as_view(template_name="week3/1_am.html"), name="week3_day1_am"),
    url("^week3/1_pm/$", TemplateView.as_view(template_name="week3/1_pm.html"), name="week3_day1_pm"),
    url("^week3/2_am/$", TemplateView.as_view(template_name="week3/2_am.html"), name="week3_day2_am"),
    url("^week3/2_pm/$", TemplateView.as_view(template_name="week3/2_pm.html"), name="week3_day2_pm"),
    url("^week3/3_am/$", TemplateView.as_view(template_name="week3/3_am.html"), name="week3_day3_am"),
    url("^week3/3_pm/$", TemplateView.as_view(template_name="week3/3_pm.html"), name="week3_day3_pm"),
    url("^week3/lab/$", TemplateView.as_view(template_name="week3/lab.html"), name="week3_lab"),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
