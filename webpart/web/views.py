from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from PIL import Image
from base64 import decodebytes
import base64

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# Create your views here.
#def index(request):
    #return HttpResponse("Hello, world!")

def getRandomClass(request):
    return HttpResponse("todo")

@csrf_exempt
def guessImage(request):
    image_data = str(request.body)
    format, imgstr = image_data.split(';base64,')
    print(format)
    ext = format.split('/')[-1]
    print(ext)
    data = ContentFile(base64.b64decode(imgstr))
    myfile = "profile-temp." + ext
    fs = FileSystemStorage()
    filename = fs.save(myfile, data)
    #fs = FileSystemStorage()
    #filename = fs.save(myfile, data)
    #data = request.body
    ##print(data)
    #imgdata = decode_base64(data)
    #imgdata += "=" * ((4 - len(imgdata) % 4) % 4)  # ugh
    #filename = 'some_image.png'  # I assume you have a way of picking unique filenames
    #with open(filename, 'wb') as f:
        #f.write(imgdata)

    #print(request.body[0:22])
    #print(request.body)
    #data = request.body
    #print(type(data))
    #imgdata = base64.b64decode(request.body[:22])
    #filename = 'some_image.png'  # I assume you have a way of picking unique filenames
    #with open(filename, 'wb') as f:
       #f.write(imgdata)

    #start = 0
    #end = 3
    #toRemove = request.body[start:end]
    #print(toRemove)
    #imgdata = base64.b64decode(request.body[:-1])
    #filename = 'some_image.png'  # I assume you have a way of picking unique filenames
    #with open(filename, 'wb') as f:
        #f.write(imgdata)

    #KIND OF RABOTAET
    #imgdata = base64.b64decode(request.body[:27])
    #filename = 'some_image.png'  # I assume you have a way of picking unique filenames
    #with open(filename, 'wb') as f:
        #f.write(imgdata)


    #img_data = request.body
    #print(img_data[0:30])
    #image = Image.frombytes('RGBA', (200, 200), decodebytes(img_data))
    #image.save("foo.png")
    return HttpResponse("prinyal!")

import base64
import re

def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    #data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    print(len(data))
    if missing_padding:
        data += b'='* (4 - missing_padding)

    print("LOL")
    print(len(data))

    return base64.b64decode(data, altchars)