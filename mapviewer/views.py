import leafmap
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is Main Map viewer")
    #you can send variable value to front page in context
    context = {
        "Value1" : "Test value"
    }
    return render(request,'index.html', context)

#this is map2 viewer
# def map2(request):
#      return render(request,'map2.html')

def map2(request):
     m = leafmap.Map(center=(40, -100), zoom=4)
    #  html = "<html><body>It is now %s.</body></html>" % m
     return render(request, m)