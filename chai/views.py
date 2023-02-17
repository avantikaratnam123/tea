from django.shortcuts import render, redirect
from . models import Contact,Product

# Create your views here.
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def home(request):
    item = Product.objects.all()
    return render(request,'home.html',{"item":item})


def contact_us(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        msg=request.POST['message']
        Contact.objects.create(name=name,email=email,subject=subject,message=msg)
        return redirect('/contact/')
