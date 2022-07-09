from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_view(request):

    context_dict = {'text': 'hello world', 'number': 100}

    return render(request, 'app_two/home.html', context=context_dict)


@login_required
def relative_url_templates_view(request):

    return render(request, 'app_two/relative_url_templates.html')
