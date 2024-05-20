import os

from django.conf.global_settings import MEDIA_ROOT
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/home.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from AI_hub.settings import BASE_DIR

def upload_view(request):
    if request.method == 'POST':
        # Get the uploaded file object
        uploaded_file = request.FILES['file']
        filename = uploaded_file.name

        # Handle the file (e.g., save it locally)
        with open(os.path.join(BASE_DIR,"media", filename), 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        return HttpResponse('File uploaded successfully!')

    return render(request, 'home/upload_form.html')
