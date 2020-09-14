from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.validators import validate_email,ValidationError
from django.contrib.auth import authenticate,login,logout

class BaseView(View):
    @staticmethod
    def response(data={},message='',status=200):
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
        if not username:
            return self.response(message='아이디를 입력해 주세요',status=400)

        password=request.POST.get('password','')
        if not password:
            return self.response(message='비밀번호를 입력해 주세요',status=400)

        email=request.POST.get('email','')
        if not email:
            return self.response(message='올바른 이메일을 입력해주세요.',status=400)

        try:
            user=User.objects.create_user(username,email,password)
        except IntegrityError:
            return self.response(message='이미 존재하는 아이디입니다.',status=400)

        return self.response({'user.id':user.id})

class UserLoginView(BaseView):
    def post(self,request):
        username=request.POST.get('username','')
        if not username:
            return self.response(message='아이디를 입력해주세요',status=400)
        password=request.POST.get('password','')
        if not password:
            return self.response(message='비밀번호를 입력해주세요.',status=400)

        user=authenticate(request,username=username,password=password)
        if user is None:
            return self.response(message='입력 정보를 확인해주세요.',status=400)
        login(request,user) 

        return self.response

class UserLogoutView(BaseView):
    def get(self,request):
        logout(request)
        return self.response()
        