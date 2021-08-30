from views import Home
from django.urls.conf import path


urlpatterns = [
    path("", Home, name="Home")
]
