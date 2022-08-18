from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "frontend.html")


def create(request):
    if request.method == "POST":
        link = request.POST.get("link")
        uid = str(uuid.uuid4())[:7]
        new_url = url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


# Create your views here.
