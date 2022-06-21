from django.shortcuts import render
from galleryapp.form import ImageForm
from .models import ImageModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ImageSerializer

def Home(request):
    form=ImageForm()
    data = ImageModel.objects.all()
    if request.method == 'POST':  
        form = ImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save() 
            img_object = form.instance  
            return render(request, 'index.html', {'form': form, 'img_obj': img_object})
    return render(request, 'index.html', {'form': form,'data':data})  


# @api_view(['POST'])
# def ImgUpload(request):
#     if request.method == 'POST':  
#         serializer=ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('item added')

@api_view(['POST'])
def ImgUpload(request): 
    serializer=ImageSerializer(data=request.data)
    serializer.image=request.FILES.get('image')
    if serializer.is_valid():
        serializer.save()
        return Response('item uploaded')




