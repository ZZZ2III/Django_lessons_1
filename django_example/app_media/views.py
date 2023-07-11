from django.shortcuts import render
from app_media.forms import UploadFileForm, UploadFileFormHomework
from django.views import View
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
            cleared_word_spl = 'Empty'
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
