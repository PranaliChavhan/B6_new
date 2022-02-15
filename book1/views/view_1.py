from django.http import HttpResponse

def view_a(request):
    return HttpResponse("In view_a")

def view_b(request):
    return HttpResponse("In view_b")