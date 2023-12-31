from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    
        {'id': 1, 'name': 'ATX ONE'},
        {'id': 2, 'name': 'ATX EMISSOR'},
        {'id': 3, 'name': 'ATX SALES'},
    
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room= None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)