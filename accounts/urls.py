from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
  path('signup/', views.SignUpView.as_view(), name='signup')
  # path('login/', LoginView.as_view(template_name = 'index.html',), name = 'login')

]