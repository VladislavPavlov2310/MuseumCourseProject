from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_list, name='home'),
    path('collection/', views.collection_list, name='collections'),
    path('add-work/', views.work_add, name='create_work'),
    path('add-collection/', views.collection_add, name='create_collection'),
    path('work/<int:pk>/', views.work_detail, name='work_detail'),
    path('collection/<int:pk>', views.collection_detail, name='collection_detail'),
    path('delete/<int:pk>', views.work_delete, name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
