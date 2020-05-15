from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm


# Create your views here.

def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'app10/index.html', params)

# create model

def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect('app10:index')

    params = {
        'title': 'Hello maeda san',
        'form': FriendForm(),
    }
    return render(request,'app10/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect('app10:index')

    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'app10/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend.delete()
        return redirect('app10:index')

    params={
        'title': 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'app10/delete.html', params)