from django.urls import path, include
from .views import RegisterApi, LogoutView


urlpatterns = [
      path('register', RegisterApi.as_view()),
      path('logout/', LogoutView.as_view()),
]
