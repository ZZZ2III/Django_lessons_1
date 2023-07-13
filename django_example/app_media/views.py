from django.shortcuts import render, redirect
from app_media.forms import UploadFileForm, UploadFileFormHomework, MultiFileForm
from django.views import View
from app_media.models import DocumentForm, File
from django.http import HttpResponse
from django.utils.encoding import smart_str


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
    banned_words = ['эти', 'слова', 'запрещены']
    if request.method == 'POST':
        upload_file_form = UploadFileFormHomework(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            file_cont = file.chunks()
            cleared_word_spl = ''
            for word in file_cont:
                cleared_word = smart_str(word)
                cleared_word_spl = cleared_word.strip().split()
                for j in cleared_word_spl:
                    if j.lower() in banned_words:
                        print(j.lower())
                        return HttpResponse(content='Слова из скрытого пула, отображать не будем!!!')

            return HttpResponse(content=f"{cleared_word_spl}", status=200)
    else:
        upload_file_form = UploadFileFormHomework()

    context = {
        'form': upload_file_form
    }
    return render(request, 'upload_file2.html', context=context)


def UploadFileToFolder(request):
    if request.method == 'POST':
        upload_file_from = DocumentForm(request.POST, request.FILES)
        if upload_file_from.is_valid():
            upload_file_from.save()
            return redirect('/')
        else:
            print(upload_file_from.errors)
    else:
        upload_file_from = DocumentForm()

    return render(request, 'file_form_upload.html', context={'form': upload_file_from})


def UploadMultipleFiles(request):
    if request.method == 'POST':
        form = MultiFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = File(file=f)
                instance.save()
            return redirect('/')
    else:
        form = MultiFileForm()

    return render(request, 'upload_files.html', context={'form': form})
