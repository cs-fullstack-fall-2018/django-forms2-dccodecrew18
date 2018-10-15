from django.shortcuts import render


from .models import FormModel # the class


def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context) # oh so this points to the templates they made not the app since index there.