from django.contrib import admin
from django.urls import path
from core import views
from core.views import front


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front, name='front'),
    path('register/', views.register_request, name="register"),
]
