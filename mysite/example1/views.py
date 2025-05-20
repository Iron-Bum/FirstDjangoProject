from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    return render(request,'second_task/function_task.html')


def test_value(request, name):
    value = {'name': name}
    return render(request,'second_task/index.html', value)


class Index2(TemplateView):
    template_name = 'second_task/class_task.html'
