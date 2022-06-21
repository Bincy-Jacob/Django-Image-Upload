from django.urls import path
from galleryapp import views

urlpatterns=[
    path('',views.Home),
    path('imgupload/',views.ImgUpload,name='imgupload'),
]