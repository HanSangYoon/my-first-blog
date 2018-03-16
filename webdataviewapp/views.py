from django.shortcuts import render

# Create your views here.
def start_show_data(request):
    return render(request, 'webdataviewapp/index.html', {})
