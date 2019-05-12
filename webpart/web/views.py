from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from .recognition import recognize, get_classes
from PIL import Image
from base64 import decodebytes
import base64
import random

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# Create your views here.
#def index(request):
    #return HttpResponse("Hello, world!")

def getRandomClass(request):
    classes = get_classes()

    return HttpResponse(classes[random.randint(0, len(classes) - 1)])

@csrf_exempt
def guessImage(request):
    image_data = str(request.body)
    format, imgstr = image_data.split(';base64,')
    #print(format)
    ext = format.split('/')[-1]
    #print(ext)
    data = ContentFile(base64.b64decode(imgstr))
    myfile = "inputPics/profile-temp." + ext
    fs = FileSystemStorage()
    filename = fs.save(myfile, data)
    print(filename)
    guessedClasses = recognize(filename)
    print(guessedClasses)
    return HttpResponse(guessedClasses)
