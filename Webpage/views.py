from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def resume(request):
    return render(request,'Webpage/CV_Template.html',{})

def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'Bhagyashree_Aher_Resume.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Resume_BhagyashreeAher.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')
