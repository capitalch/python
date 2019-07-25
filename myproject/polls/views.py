from django.http import HttpResponse

from utils import getcomments

def index(request):
    output = getcomments.getComments()
    return HttpResponse(output)
