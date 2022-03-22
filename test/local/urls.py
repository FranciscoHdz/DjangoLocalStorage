from django.urls import path
from local.views import *

urlpatterns =[
    path('',index.as_view(),name="index")
]