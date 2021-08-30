from resume.views import resumeHome
from django.urls.conf import path


urlpatterns = [
    path("", resumeHome, name="usersHome")
]
