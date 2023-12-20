from django.urls import path
from . import views
#from .views import ActaPdf
from django.conf import settings
from django.conf.urls.static import static

app_name= 'cssapp'
urlpatterns = [
    path('', views.acta_list, name='acta_list'),
    path('acta/<int:pk>/', views.acta_detail, name='acta_detail'),
    path('acta/new/', views.acta_new, name='acta_new'),
    path('acta/<int:pk>/edit/', views.acta_edit, name='acta_edit'),
    #path('acta/<int:pk>/pdf', ActaPdf.as_view(),name='acta_pdf'),
    path('acta/<int:pk>/pdf/', views.actacss_pdf,name='acta_pdf'),
    #path('acta/<int:pk>/edit/firmacss', views.acta_firmacss, name='acta_firmacss'),
    #path('acta/<int:pk>/edit/firmacont', views.acta_firmacont, name='acta_firmacont')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
