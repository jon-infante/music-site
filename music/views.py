from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello World, you are at the music app homepage.')

def classical_songs(request):
    return HttpResponse("Hello Classical!")
