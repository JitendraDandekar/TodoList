from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        time = request.POST['time']
        todo = Todo.objects.create(title=title, description=description, time=time)
        todo.save()
        messages.info(request, 'Saved')
        return redirect('/')
    else: 
        lst = Todo.objects.all()
        return render(request, 'index.html',{'list': lst})

def delete(request, num):
    todo = Todo.objects.get(id=num).delete()
    messages.info(request, 'Deleted')
    return redirect('index')
