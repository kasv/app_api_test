from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path("", views.ApplicationsAPIView.as_view()),
    path("<int:pk>/", views.SingleApplicationAPIView.as_view()),
    path("test/<str:api_key>/", views.JSONApplicationAPIView.as_view()),
]
