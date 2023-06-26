from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *


class Booklist(GenericAPIView,ListModelMixin):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)
    
    
class BookCreate(GenericAPIView,CreateModelMixin):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args,**kwargs)
    

class BookRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    
class BookUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args,**kwargs)
    

class BookDelete(GenericAPIView,DestroyModelMixin):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args,**kwargs)
    
    
