from django.shortcuts import render

from catalog.forms import Form


# Create your views here.
def index(request):
    user_agent = request.META["HTTP_USER_AGENT"]
    with open('log.txt', 'a+') as file:
        file.write(str(user_agent))
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            with open('contactslog.txt', 'a+') as file:
                file.write(str(form))

    return render(request, 'catalog/contacts.html', )
