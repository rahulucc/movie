from django.shortcuts import render
from .models import movie

# Create your views here.
def home(request):
    if request.method=="GET":
        db=movie.objects.all()
        return render(request,'home.html',{'db':db})


