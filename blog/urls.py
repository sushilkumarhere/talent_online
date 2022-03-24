from django.conf import settings
from django.conf.urls.static import static
from . import views, admin
from django.urls import path

urlpatterns = [
    # main Site URLs
    
    path('', views.Home, name='home'),
    path('contactus_query/', views.contactus_query, name='contactus_query'),
    path('distcourse/', views.distance_edus, name='distance_edu'),
    path('blogs', views.blog, name='blog'),    
    path('register/', views.registrations2, name='register'), 
    path('<slug:slug>/', views.courseDetail, name='courseDetail'),   
    # Post Detail Site URLs 
    #path('<slug:slug>/', views.PostDetail, name='post_detail'),
   
      
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
