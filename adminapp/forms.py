import pytz
from django import forms
from .models import Task, StudentList


class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title']



class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    phone_number = forms.CharField(max_length=10, label='Phone Number',
                                   widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))
    comments = forms.CharField(
        max_length=150,
        widget=forms.Textarea(attrs={'placeholder': 'Enter your comments', 'maxlength': '150'}),  # Set the maxlength attribute in the widget
        label='Comments'
    )

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit():
            raise forms.ValidationError('Phone number should only contain digits.')
        return phone

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address']

from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search Contacts', max_length=100)
