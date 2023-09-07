from django.shortcuts import render, redirect

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def livestream(request):
    return render(request, 'livestream.html')

def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/livestreaming?roomID=" + roomID)
    return render(request, 'joinroom.html')