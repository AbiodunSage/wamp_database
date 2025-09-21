from django.shortcuts import render
from .forms import SampleModelForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SampleModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = SampleModelForm()  # Clear the form after saving
    else:
        form = SampleModelForm()

    return render(request, 'index.html',{'form': form})