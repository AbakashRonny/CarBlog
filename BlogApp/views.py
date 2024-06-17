from django.shortcuts import render,redirect
from .models import BlogPostModel
from .forms import BlogPostForm
# Create your views here.

def car_blog(request):
    data=BlogPostModel.objects.all()
    d={'data':data}
    return render(request,'BlogApp/blog.html',d)

def add_blog(request):
    if request.method=='POST':
        form=BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')

    form=BlogPostForm()
    d={'form':form}
    return render(request,'BlogApp/add_blog.html',d)

def description(request,id):
    data=BlogPostModel.objects.get(id=id)
    d={'data':data}
    return render(request,'BlogApp/description.html',d)


