from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    print(request.POST.get('name'))
    print(request.POST.get('phone'))
    print(request.POST.get('message'))

    return render(request, 'catalog/contacts.html')
