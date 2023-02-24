from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.core.mail import send_mail
from .models import Dog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    dogs = Dog.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        content = request.POST.get("content")
        telephone_number = request.POST.get("telephone_number")
        send_mail(f"{name} contacting", content + "\r" + telephone_number, email, [], fail_silently=True)
        messages.success(request, "Thank you for contacting Us")
    dogs = Paginator(dogs, 20)
    page = request.GET.get("page")
    page_obj = dogs.get_page(page)
    return render(request, 'home.html', {"page_obj": page_obj, "dogs":dogs})

def detail(request, pk, name):
    dog = get_object_or_404(Dog, pk=pk, name=name)
    return render(request, 'detail.html', {'dog': dog})

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')
