from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MediaFileForm
from .models import MediaStore

def upload_file(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = MediaFileForm()
    return render(request, 'upload_file.html', {'form': form})

def file_list(request):
    files = MediaStore.objects.all()
    return render(request, 'file_list.html', {'files': files})

def download_file(request, file_number):
    media_file = MediaStore.objects.get(file_number=file_number)
    response = HttpResponse(media_file.file_data, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{media_file.file_name}.{media_file.file_extension}"'
    return response
