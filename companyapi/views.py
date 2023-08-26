from django.http import HttpResponse

def home_page(request):
    return HttpResponse("i am devin patel devloper ")