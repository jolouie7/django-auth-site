from django.urls import path
from .views import RegisterView, GetUserView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('get-user/', GetUserView.as_view()),
]
