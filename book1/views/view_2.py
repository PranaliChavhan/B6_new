from django.http import HttpResponse

def view_c(request):
    return HttpResponse("In view_c")

def view_d(response):
    return HttpResponse("In view_d")