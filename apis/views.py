from django.http import JsonResponse
from django.views import View

class BaseVIew(view):
    @staticmethod
    def response(data={},message,status=200):
        result ={
            'data':data,
            'message':message,
        }
        return JsonResponse(result,status)
# Create your views here.
