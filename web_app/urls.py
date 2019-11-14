from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'web_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('contact/',views.contact,name='contact'),
    path('projects/',views.projects,name='projects'),
    path('summary/',views.summary,name='summary'),
    path('prolists/',views.prolists,name='Project Lists'),
]
