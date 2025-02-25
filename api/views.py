from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView

from rest_framework.response import Response

from api.serializers import LeadSerializer

from api.models import Lead

from rest_framework import authentication,permissions

# Create your views here.

class LeadListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes =[permissions.IsAdminUser]

    def get(self,request,*args,**kwargs):

        all_leads=Lead.objects.all()

        serializer_instance=LeadSerializer(all_leads,many=True)

        return Response(data=serializer_instance.data)
    

    def post(self,request,*args,**kwargs):

        serializer_instance=LeadSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        

class LeadRetrieveUpdateDestroyView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes =[permissions.IsAdminUser]

    def get(self,request,*args,**kwargs):
          
        id=kwargs.get("pk")

        qs=get_object_or_404(Lead,id=id)

        serializer_instance=LeadSerializer(qs,many=False)  #serialization

        return Response(serializer_instance.data)
    

    def delete(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        lead_instance=get_object_or_404(Lead,id=id)

        lead_instance.delete()

        return Response(data={"message":"deleted"})
    

    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        lead_instance=get_object_or_404(Lead,id=id)

        serializer_instance=LeadSerializer(data=request.data,instance=lead_instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)


      






