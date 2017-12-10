
from .views import *
from django.conf.urls import url

urlpatterns = [

    url(r'^$', LandingView.as_view(), name='landing'),
]
