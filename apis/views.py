from django.http import JsonResponse
from django.views import View

class BaseView(view):
    @staticmethod
    def response(data={},message,status=200):
        result ={
            'data':data,
            'message':message,
        }
        return JsonResponse(result,status)

class UserCreateView(BaseView):
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super(UserCreateView,self).dispatch(request,*args,**kwargs)
    
    def post(self,request):
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        email=request.POST.get('email','')

        user=User.objects.create_user(username,email,password)

        return self.response({'user.id':user.id})