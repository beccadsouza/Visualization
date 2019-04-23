from django.contrib import admin
from django.conf.urls import url
from .views import home, get_data

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^data/', get_data)
]

