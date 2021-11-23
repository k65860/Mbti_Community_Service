from django.http import request
from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from .models import Write
from .forms import WriteForm

# Create your views here.

def login(request):
    return render(request, 'login.html')

def main(request):
    return render(request, 'main.html')

def counsel(request):
    return render(request, 'counsel.html')

def talk(request):
    return render(request, 'talk.html')

def talk2(request):
    return render(request, 'talk2.html')

def main(request):
    return render(request, 'main.html')

def home(request):
    blogs = Blog.objects
    return render(request, 'main.html', {'blogs' : blogs})

def aaa(request):
    all_write = Write.objects.all()
    return render(request, 'aaa.html',{'all_write':all_write})

def create(request):
    if request.method == "POST":
        create_form = WriteForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('aaa')
    else:
        create_form = WriteForm()
    return render(request,'create.html',{'create_form':create_form})

def detail(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)
    return render(request,'detail.html',{'my_write':my_write})

def update(request, write_id):
    my_write = get_object_or_404(Write,id=write_id)
    if request.method == "POST":
        update_form = WriteForm(request.POST, instance= my_write)
        if update_form.is_valid():
            update_form.save()
            return redirect('aaa')
    else:
        update_form = WriteForm(instance=my_write)
    return render(request,'update.html',{'update_form':update_form})

def delete(request, write_id):
    my_write = get_object_or_404(Write,id = write_id)
    my_write.delete()
    return redirect('aaa')


