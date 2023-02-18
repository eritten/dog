from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.core.mail import send_mail
from .models import Dog
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def home(request):
    return render(request, 'home.html')

def detail(request, pk, name):
    dog = get_object_or_404(Dog, pk=pk, name=name)
    return render(request, 'detail.html', {'dog', dog})
@api_view(["POST"])
def contact(request):
    name = request.data.get("name")
    email = request.data.get("email")
    content = request.data.get("content")
    telephone_number = request.data.get("telephone_number")
    send_mail()
    return Response({"status": "sent"})
