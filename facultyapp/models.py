
from django.db import models
from adminapp.models import StudentList,User

class AddCourse(models.Model):
    COURSE_CHOICES =[
        ('AOOP' , 'ADVANCED OBJECT ORIENTED PROGRAMMING'),
        ('PFSD', 'PYTHON FULL STACK DEVELOPMENT'),
    ]
    SECTION_CHOICES=[
        ('S11','SECTION S11'),
        ('S12', 'SECTION S12'),
        ('S13', 'SECTION S13'),
        ('S14', 'SECTION S14'),
        ('S15', 'SECTION S15'),
        ('S16', 'SECTION S16'),
        ('S17', 'SECTION S17'),
    ]
    student = models.ForeignKey(StudentList, on_delete= models.CASCADE)
    course=models.CharField(max_length=50, choices = COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    def __str__(self):
        return f'{self.student.Register_Number} - {self.course} ({self.section})'

# blog/models.py
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['publication_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

class Marks(models.Model):
    COURSE_CHOICES =[
        ('AOOP' , 'ADVANCED OBJECT ORIENTED PROGRAMMING'),
        ('PFSD', 'PYTHON FULL STACK DEVELOPMENT'),
    ]

    student = models.ForeignKey(StudentList, on_delete= models.CASCADE)
    course=models.CharField(max_length=50, choices = COURSE_CHOICES)
    marks=models.IntegerField()
    def __str__(self):
        return f"{self.student.name} - {self.course} - Marks: {self.marks}"