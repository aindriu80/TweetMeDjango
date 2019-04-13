from django.shortcuts import render

# retrieve
# GET -- Template home.html
def home(request):
    return render(request, "home.html", {})