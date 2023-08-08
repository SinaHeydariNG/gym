from django.shortcuts import render , HttpResponse , redirect
from .models import Contact
from .forms import PostForm
from main.models import SiteInfo as information
from django.contrib import messages

# Create your views here.

def add(request):
    title = "تماس با ما"
    add_message = PostForm()

    context =  {
        'title' : title,
        'add_message' : add_message

    }
    return render(request , 'contact/add.html' , context)



def submit_message(request):
    if request.method == "POST":
        my_form = PostForm(request.POST)
        if my_form.is_valid():
            new_meesage = Contact.objects.create(
                name = my_form.cleaned_data['name'],
                email = my_form.cleaned_data['email'],
                phone = my_form.cleaned_data['phone'],
                message = my_form.cleaned_data['message'],
            )
            new_meesage.save()
            messages.success(request,"پیام شما با موفقیت ارسال شد!")
            return redirect("main:home")
        else:
            messages.error(request,"مشکلی در ارسال پیام پیش آمد")
            return redirect("main:home")
    else:
        messages.info(request,"مشکلی در ارسال درخواست شما پیش آمد")
        return redirect("main:home")
    


def contact(request):
    title = "تماس با ما"
    info = information.objects.last()
    add_message = PostForm()
    context = {
        "title" : title,
        "info" : info,
        "add_message" : add_message
    }
    return render(request , 'contact/contact.html' , context)        