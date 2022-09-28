from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .showtop import showTop


# Create your views here.
def showTopHashtag(request):
    word = "apple"
    data = {
        "Topword" : showTop(word)
    }
    if request.method == "GET":
        return render(request, 'crawling/crawling.html', {'data':data})