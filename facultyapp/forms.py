from django import forms
from .models import BlogPost, AddCourse, Marks
from adminapp.models import StudentList
# blog/forms.py
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

class AddCourseForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=StudentList.objects.all(),
        empty_label="Select Student"
    )

    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'course', 'marks']
        labels = {
            'student': 'Student id',
            'course': 'Course',
            'marks': 'Marks Obtained',
        }
