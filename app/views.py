from django.shortcuts import render

# Create your views here.
def index(request):
    test = str()
    return render(request, 'index.html')