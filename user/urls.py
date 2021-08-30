

from user.views import UserHome
from django.urls.conf import path


urlpatterns = [
    path("", UserHome, name="usersHome")
]
