from django.shortcuts import render , redirect , HttpResponse
from .models import SiteInfo as information , About
from services.models import Services
from contact.models import Contact
from contact.forms import PostForm
# Create your views here.



def home(request):
    title = "Home"
    info = information.objects.last()
    services = Services.objects.all()
    add_message = PostForm()
    feedbacks = Contact.objects.filter(activate = True)
    context = {
        "title" : title,
        "info" : info,
        "services" : services,
        "add_message" : add_message,
        "feedbacks" : feedbacks
    }
    return render(request , 'main/home.html' , context)



def about(request):
    title = "درباره ما"
    info = information.objects.last()
    about = About.objects.last()
    context = {
        "title" : title,
        "info" : info,
        "about" : about
    }
    return render(request , 'main/about.html' , context)    