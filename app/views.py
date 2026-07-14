from django.shortcuts import render
from .models import Joke
# Create your views here.

def homePage(request):
    jokes = Joke.objects.all()

    latest_joke = Joke.objects.order_by('created_at').first()

    context = {'latest_joke': latest_joke}
    
    return render(request, "app/home.html", context)