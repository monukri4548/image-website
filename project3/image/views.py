from django.shortcuts import render
from .forms import Imageform
from .models import images
# Create your views here.
def home(request):
    if request.method=="POST":
        form=Imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=Imageform()
    img=images.objects.all()
    return render(request,'image/home.html',{'img':img,'form':form})