from django.shortcuts import render

# Create your views here.

def bookingRoom(request):
    context = {}
    return render(request, 'booking/room.html', context)