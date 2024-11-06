from django.core.mail import send_mail
from django.shortcuts import render, redirect
from adminapp.models import User
from facultyapp.models import Marks
def FacultyHomePage(request):
    return render(request,'facultyapp/FacultyHomePage.html')
from django.shortcuts import render, redirect
from .forms import AddCourseForm, MarksForm
def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:FacultyHomePage')
    else:
        form = AddCourseForm()
    return render(request, 'facultyapp/add_course.html', {'form': form})
from django.views.generic.edit import FormView
from .forms import AddCourseForm
class AddCourseView(FormView):
    template_name = 'facultyapp/add_course.html'
    form_class = AddCourseForm
    success_url = '/facultyapp/facultyHomePage/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
from .models import AddCourse
from adminapp.models import StudentList
def view_student_list(request):
    course = request.GET.get('course')
    section = request.GET.get('section')
    student_courses = AddCourse.objects.all()
    if course:
        student_courses = student_courses.filter(course=course)
    if section:
        student_courses = student_courses.filter(section=section)
    students = StudentList.objects.filter(id__in=student_courses.values('student_id'))
    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES
    context = {
        'students': students,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }
    return render(request, 'facultyapp/view_student_list.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm
def create_post_page_call(request):
    return render(request, 'facultyapp/Blogpost.html')
def createpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:post_list')
    else:
        form = BlogPostForm()
    return render(request, 'facultyapp/Blogpost.html', {'form': form})
def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'facultyapp/post_detail.html', {'posts': posts})
def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'facultyapp/post_list.html', {'post': post})
def post_marks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            marks_instance = form.save(commit=False)
            marks_instance.save()
            student = marks_instance.student
            student_user = student.user
            user_email = student_user.email
            subject = 'Marks Entered'
            message = f'Hello, {student_user.first_name}  marks for {marks_instance.course} have been entered. Marks: {marks_instance.marks}'
            from_email = 'deepikareddymandapati@gmail.com'
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)
            return render(request, 'facultyapp/post_marks.html')
    else:
        form = MarksForm()
    return render(request, 'facultyapp/post_marks.html', {'form': form})