from django.shortcuts import render
from .models import Contact
from .models import Gallery
from .models import Upload
from .models import Saying, Update
saying = Saying.objects.all()
updates = Update.objects.all()

def index(request):
    return render(request, 'base/index.html', {'saying': saying, 'updates': updates})


def gallery(request):
    pictures = Gallery.objects.all()
    context = {'pictures': pictures, 'saying': saying, 'updates': updates}
    return render(request, 'base/gallery.html', context)


def about(request):
    context = {'saying': saying, 'updates': updates}
    return render(request, 'base/about.html', context)


def uploads(request):
    uploads = Upload.objects.all()
    line = '_'*30
    context = {'saying': saying, 'updates': updates,
               'uploads' : uploads, 'line': line}
    return render(request, 'base/uploads.html', context)


def contact(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts, 'saying': saying, 'updates': updates}
    return render(request, 'base/contact.html', context)
