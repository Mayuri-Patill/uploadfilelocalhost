from django.shortcuts import render,HttpResponse

from .forms import UploadFilesForm


# Create your views here.

#def index(request):
    #context = {
     #   'form': UploadFilesForm()
    #}

    #return render(request,'index.html',context)



def index(request):
    if request.method == 'POST':
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('')
    else:
        form = UploadFilesForm()

    context = {'form': form}
    return render(request, 'index.html', context)
