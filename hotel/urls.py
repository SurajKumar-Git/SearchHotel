from django.urls import path
from .views import GetHotelsApiView

urlpatterns = [
    path("", GetHotelsApiView.as_view(), name="hotels")
]