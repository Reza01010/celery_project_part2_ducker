from django.shortcuts import render
from .tasks import add


def view(request):
    from datetime import timedelta


    result = add.apply_async(args=[3, 5], countdown=5)
    print('\n"-_-"' * 20, result, '\n"-_-"' * 20)

    return render(request, template_name='w.html')



