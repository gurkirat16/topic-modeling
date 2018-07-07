import os

from cvcv import MyCorpus


from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document, EngineData
from uploads.core.forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })


def search_engine_view(request):
    if request.method == 'GET':
        # Documents directory
        doc_dir = os.path.join('media', 'documents')

        # loop for all the files in the directory
        for filename in os.listdir(doc_dir):
            # Call MyCorpus for every file
            corpus = MyCorpus(os.path.join(doc_dir, filename))
            for key, value in corpus.dictionary.token2id.items():
                engine = EngineData(
                    word=key,
                    appear_time=value)
                engine.save()
