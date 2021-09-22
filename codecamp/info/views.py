from django.shortcuts import render

# Create your views here.
def info_home_view(request):
    return render(request, "info_home.html", {})
