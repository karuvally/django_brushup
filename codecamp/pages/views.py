from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Welcome to Home Page!<h1>")
    render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>All contacts can be found here</h1>")
