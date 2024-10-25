from django.http import HttpResponse

def index(request):
    return HttpResponse(content="Hello, world! You are at the index of Receipts NH.")
