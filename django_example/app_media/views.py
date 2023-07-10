from django.shortcuts import render
from app_media.forms import UploadFileForm,UploadFileFormHomework
from django.views import View
from django.http import HttpResponse


# Create your views here.

def UploadFile(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            answer_strng = f'filename: {file.name}\nsize: {file.size}'
            print(request.FILES)
            return HttpResponse(content=answer_strng, status=200)
    else:
        upload_file_form = UploadFileForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'upload_file.html', context=context)

def UploadFileHomework(request):
    banned_words = ['Эти','слова','запрещены']
    if request.method == 'POST':
        upload_file_form = UploadFileFormHomework(request.POST,request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            file_cont = file.read()
            for word in file:
                print(word)
        return HttpResponse(content="ХУХ",status=200)
    else:
        upload_file_form = UploadFileFormHomework()

    context = {
        'form':upload_file_form
    }
    return render(request,'upload_file2.html',context=context)