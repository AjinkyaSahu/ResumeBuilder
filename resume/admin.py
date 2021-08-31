from resume.models import *
from django.contrib import admin

# Register your models here.

admin.site.register([Resume,
                     Educations,
                     Work,
                     Certificates,
                     Hobbies, Skills, Links]
                    )
