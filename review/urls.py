from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'review'

urlpatterns = [
    path('review', review, name='review'),
    path('create', review_create, name='review_create'),
    path('detail/<int:pk>', review_detail, name='review_detail'),
    path('update/<int:pk>', review_update, name='review_update'),
    path('delete/<int:pk>', review_delete, name='review_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)