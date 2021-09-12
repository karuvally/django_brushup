import platform
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Welcome to Home Page!<h1>")
    context_dict = {
        "karyam_list": ["പാചകം", "വാചകം", "ഓട്ടം", "ചാട്ടം"]
    }
    return render(request, "home.html", context_dict)

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>All contacts can be found here</h1>")
    context_dict = {
        "os": platform.system(),
        "kernel": platform.release(),
        "my_list": [1.2, 2.1, 2.2, 3.7],
        "processor": platform.processor()
    }
    return render(request, "contact.html", context_dict)
