from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from WaterForceUserApp.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index_page(request):
    our_features_slider = OurFeaturesSliderHome.objects.all()
    client_sliders = ClientSlider.objects.all()
    return render(request,"index.html",{'our_features_slider':our_features_slider,'client_sliders':client_sliders})

def about_page(request):
    about_page_sliders = AboutUsPageSlider.objects.all()
    return render(request,"about.html",{'about_page_sliders':about_page_sliders})


def gallery_page(request):
    gallery_imgs = Gallery.objects.all()
    return render(request,"gallery.html",{'gallery_imgs':gallery_imgs})

def services_page(request):
    services = Services.objects.all()
    return render(request,"services.html",{'services':services})

def contact_page(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']
        obj = Contact(
            fullname = fullname,
            email = email,
            mobile = mobile,
            message = message,
        )
        obj.save()
        if email and message:
            try:
                send_mail('email','message')
            except BadHeaderError:
                message.error('Can Not Send Mail')
            return('contact_page')
        return redirect('contact_page')
    
    return render(request,"contact.html")

def client_slider_form(request):
    return render(request,"clientsliderform.html")





# ======================= page not found ===========================

def error_404(request, exception):
    data = {"name": "somthing error"}
    return render(request,'404.html', data)


# @api_view(['GET','PUT','PATCH','DELETE'])
# def client_slider(request):
#     try:
#         if request.method == 'GET':

class ClientSliderApi(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def get(self,request,*args,**kwargs):
        clientsliderdata = ClientSlider.objects.all()
        serializer = ClientSliderSerializer(clientsliderdata,many=True,)
        # print(serializer.data)
        # print(clientsliderdata)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        print("FILES:", request.FILES)  # Debug to check if files are received
        print("DATA:", request.data)
        parser_classes = (MultiPartParser, FormParser)
        serializer = ClientSliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data saved successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def post(self,request):
    #     clientsliderdata = ClientSlider.objects.all()
    #     serializer = ClientSliderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)
    
    def put(self, request, id):
        clientsliderdata = ClientSlider.objects.get(id=id)
        serializer = ClientSliderSerializer(clientsliderdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        clientsliderdata = ClientSlider.objects.get(id=id)
        clientsliderdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)