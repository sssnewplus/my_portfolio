from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from urllib.parse import quote
import json


# func to gen whatsapp url
def generate_whatsapp_url(phone_number, message):
    base_url = "https://wa.me/"
    encoded_message = quote(message)
    return f"{base_url}{phone_number}?text={encoded_message}"


# blog view
def blog(request):
    posts = {
        "posts" : Post.objects.all()
    }
    return render(request, 'myapp/blog_home.html', posts)

# generic views
def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

# asking for mentorship post
def milky_way(request):
    if request.method == 'POST':
        # grab form data
        data = {
            'name' : request.POST.get('name'),
            'email' : request.POST.get('email'),
            'phone' : request.POST.get('phone'),
            'goals' : request.POST.get('goals'),
            'experience' : request.POST.get('backgrounds'),
            'weakness' : request.POST.get('weaknesses'),
            'learning_style' : request.POST.get('learning_style'),
            'mode_of_communication' : request.POST.get('communication'),
            'challenges' : request.POST.get('challenges'),
            'feedback' : request.POST.get('feedback'),
            'carrier' : request.POST.get('carrier'),
            'resources' : request.POST.get('resources')
        }
        message = json.dumps(data)
        phone_number = "2347030678099"
        whatsapp_url = generate_whatsapp_url(phone_number, message)
        return HttpResponseRedirect(whatsapp_url)
    return render(request, 'myapp/milky_way.html')