from django.shortcuts import render
from main.models import SiteInfo as information
from .models import Services
# Create your views here.
def list(request):
    title = "خدمات ما"
    info = information.objects.last()
    services = Services.objects.all()
    context = {
        "title" : title,
        "info" : info,
        "services" : services
    }
    return render(request , 'services/list.html' , context)        