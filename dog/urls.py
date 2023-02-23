from django.contrib import admin
from django.urls import path
from home.views import home, detail, privacy, terms
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('privacy/', privacy, name='privacy'),
path('terms/', terms, name='terms'),
path('', home, name='home'),
path('detail/<int:pk>/<str:name>/', detail, name='detail'),
    path('admin/', admin.site.urls),
]
#if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
