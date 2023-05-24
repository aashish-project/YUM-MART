from django.http import HttpResponse

from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    user=request.user

    return HttpResponse(f'{user}')