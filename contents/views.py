from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

class HomeView(TemplateView):
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super(HomeView,self).dispatch(request,*args,**kwargs)

    template_name='home.html'

