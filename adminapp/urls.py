from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('printpagecall/', views.printpagecall, name='printpagecall'),
    path('printpagelogic/', views.printpageLogic, name='printpagelogic'),
    path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
    path('exceptionpagelogic/', views.exceptionpagelogic, name='exceptionpagelogic'),
    path('randomcall/', views.randomcall, name='randomcall'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),
    path('calculatecall/',views.calcualtorcall,name='calculatecall'),
    path('calculatelogic/', views.calculatorlogic, name='calculatelogic'),
    path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
    path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('UserRegisterPageCall',views.UserRegisterPageCall,name='UserRegisterPageCall'),
    path('UserRegisterLogic',views.UserRegisterLogic,name='UserRegisterLogic'),
    path('logout/', LogoutView.as_view(next_page='projecthomepage'), name='logout'),
    path('UserLoginPage/', views.UserLoginPageCall, name='UserLoginPage'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('add_student/',views.add_student,name="add_student"),
    path('studentlist/',views.student_list,name="studentlist"),
    path('upload_file/,',views.upload_file,name="upload_file"),
    path('feedback/', views.feedback_view, name='feedback'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('edit_contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('search_contact/', views.search_contacts, name='search_contacts'),
    path('send_contact_email/<int:contact_id>/', views.send_contact_email, name='send_mail'),
    ]
