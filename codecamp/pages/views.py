import platform
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Welcome to Home Page!<h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>All contacts can be found here</h1>")
    context_dict = {
        "os": platform.system(),
        "kernel": platform.release(),
        "my_list": [1.2, 2.1, 2.2, 3.7],
    }
    return render(request, "contact.html", context_dict)
