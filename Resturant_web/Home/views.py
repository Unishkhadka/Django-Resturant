from django.shortcuts import render 
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # messages.success(request, "Hello, this is a test message.")
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cmnt = request.POST.get('cmnt')
        contact = Contact(name=name, phone=phone, email=email, cmnt=cmnt, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
    return render(request, 'contact.html')
    # return HttpResponse("Hello guys.")

def about(request):
     return render(request, 'about.html')
     # return HttpResponse("This is about page.")

def services(request):
     return render(request, 'services.html')
    # return HttpResponse("This is services page.")
