from django.urls import path
from . import views

app_name = 'facultyapp'

urlpatterns = [
    path('facultyHomePage/', views.FacultyHomePage, name='facultyHomePage'),
    path('add_course/', views.AddCourseView.as_view(), name='add_course'),  # Use CBV for add_course
    path('view_student_list/', views.view_student_list, name='view_student_list'),
    path('create/', views.createpost, name='create_post'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post_marks/',views.post_marks,name='post_marks'),
]
