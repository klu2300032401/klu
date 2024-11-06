from django.urls import path
from . import views

app_name = 'studentapp'
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('studentHomePage/', views.StudentHomePage, name='studentHomePage'),
    path('view-marks/',views.view_mark,name='view_marks'),
]
