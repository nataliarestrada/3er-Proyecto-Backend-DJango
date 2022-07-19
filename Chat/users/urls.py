from .views import login_view, signup_view, logout
from django.urls import path

urlpatterns = [
    path('login/', login_view),
    path('signup/', signup_view),
    path('logout/', logout)
]