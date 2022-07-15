"""guide_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('guides/', views.guides, name='guides'),
    path('submitted', views.submitted, name='submitted'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('no-of-stud', views.no_of_stud, name='no-of-stud'),
    path('project-details-1', views.project_details_1, name='project-details-1'),
    path('project-details-2', views.project_details_2, name='project-details-2'),
    path('select-guide/', views.select_guide, name='select-guide'),
    path('guide-selected/<int:id>', views.guide_selected, name='guide-selected'),
    # /*****************/
    # reset  password urls
    path('password_reset', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    # /*****************/
    # otp verify
    path('verify', views.verify, name='verify'),
    path('verify1', views.verify1, name='verify1'),
    # # selected 2 mail
    path('mail1', views.mail1, name='mail1'),
    path('credits', views.credits, name='credits'),
    path('search/', views.search, name='search'),
    path('temp-team-1/', views.temp_team_1, name='temp-team-1'),
    path('temp-team-2/', views.temp_team_2, name='temp-team-2'),

]
