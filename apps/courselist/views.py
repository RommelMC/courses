from django.shortcuts import render, redirect
from models import *
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    context={
        'courses': Course.objects.all()
    }
    print Course.objects.all()
    return render(request, 'courselist/index.html', context)

def destroy(request, id):
    context={
        'course': Course.objects.get(id=id)
    }
    return render(request, 'courselist/destroy.html', context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect(reverse('index'))

def add(request):
    if request.method=='POST':
        course = Course.objects.create(name=request.POST['name'])
        Description.objects.create(content=request.POST['desc'], course=course)
        return redirect(reverse('index'))

def comment(request, id):
    context={
        'comments': Course.objects.get(id=id).comments.all(), 'course':Course.objects.get(id=id)
    }
    return render(request, 'courselist/comments.html', context)

def addcomment(request, id):
    if request.method=='POST':
        Comment.objects.create(content=request.POST['comment'], course=Course.objects.get(id=id))
        return redirect(reverse('comment', kwargs={'id':id}))