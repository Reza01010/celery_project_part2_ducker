from django.shortcuts import render
from .tasks import add_
from datetime import timedelta

def view(request):



    # add.apply_async(args=[3, 5], countdown=5)
    add_.delay(4, 4)

    return render(request, template_name='w.html')



