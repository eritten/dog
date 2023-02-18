from django.contrib import admin
from django.urls import path
from home.views import home, detail

urlpatterns = [
path('', home, name='home'),
path('detail/<int:pk>/<str:name>/', detail, name='detail'),
    path('admin/', admin.site.urls),
]
