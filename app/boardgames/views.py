from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from boardgames.models import BoardGame, BoardGameForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "upload.html")

def add(request):
    if request.method == "POST":
        form = BoardGameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = BoardGameForm()
    return render(request, "add.html", {
        "form": form
    })

def index(request):
    #get last 10 games:
    games = BoardGame.objects.all().order_by('-id')[:10]
    return render(request, "index.html", {'games': games})
