from django.http import HttpResponse
from .models import Movies_Info
def welcome_page(request):
    messag = f"<html> <h1>welcome to MoviesListApp </h1>" \
            f"<p>MoviesListApp has {Movies_Info.objects.count()}</p>"\
            f" </html>"
    return HttpResponse(messag)