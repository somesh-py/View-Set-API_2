from django.shortcuts import render
from .models import Car
from rest_framework.views import APIView
from .serilizers import CarModelSerilizers
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Create your views here.


class CarAPI(APIView):
    def get(self,request,pk=None):
        if pk==None:
            data=Car.objects.all()
            serilizer=CarModelSerilizers(data,many=True)
            # json_data=JSONRenderer().render(serilizer.data)
            return Response(serilizer.data)
        else:
            data=Car.objects.get(id=pk)
            serilizer=CarModelSerilizers(data)
            # json_data=JSONRenderer().render(serilizer)
            return Response(serilizer.data)

    def post(self,request):
        serilizer=CarModelSerilizers(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data Created sucessfully'})
        
    def put(self,request,pk):
        data=Car.objects.get(id=pk)
        serilizer=CarModelSerilizers(data,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Data Updated Sucessfully'})
    
    def patch(self,request,pk):
        data=Car.objects.get(id=pk)
        serilizers=CarModelSerilizers(data,data=request.data)
        if serilizers.is_valid():
            serilizers.save()
            return Response({'msg':'Data Updated Sucessfully'})
    
    def delete(self,request,pk):
        data=Car.objects.filter(id=pk).delete()
        return Response({'msg':'Data deleted Sucessfilly'})