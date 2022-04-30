import imp
from operator import ipow
from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import studentseriizer
from .models import Student
from .forms import studentform
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404,redirect

# class ProfileList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'show.html'

#     def get(self, request):
#         queryset = Student.objects.all()
#         return Response({'form': queryset})

#     def post(self, request, pk):
#         profile = get_object_or_404(Student, pk=pk)
#         serializer = studentseriizer(profile, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'profile': profile})
#         serializer.save()
#         return redirect('show.html')

class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    # def get(self, request):
    #     queryset = studentform()
    #     return Response({'form': queryset})

    def post(self, request, pk):
        profile = studentform(request.POST)
        serializer = studentseriizer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'form':serializer})



























    # if request.method ==  'GET':
    #     id=product_id
    #     if id is not None:
    #         prod = Student.objects.get(product_id=id)
    #         serilizer = studentseriizer(prod)
    #         return Response(serilizer.data)
    #     prod = Student.objects.all()
    #     serilizer = studentseriizer(prod,many=True)
    #     return Response(serilizer.data)

    # if request.method == 'POST':
    #     serilizer = Student(data = request.data)
    #     if serilizer.is_valid():
    #         serilizer.save()
    #         return Response(serilizer.data,status = status.HTTP_201_CREATED)
    #     return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)