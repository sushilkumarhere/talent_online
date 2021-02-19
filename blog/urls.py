from django.conf import settings
from django.conf.urls.static import static
from . import views, admin
from django.urls import path

urlpatterns = [
    # main Site URLs

    path('', views.PostList, name='home'),
    path('blogs', views.blog, name='blog'),
    path('contactus/', views.contactus, name='contactus'),
    path('course/', views.Course1, name='course'),
    path('register/', views.registrations2, name='register'),
    path('distance/', views.distance_edus, name='distance_edu'),
    path('appservice/', views.service_app, name='service_app'),
    path('appservice/gsmsfeatures', views.gsmsfeatures, name='gsmsfeatures'),
    path('appservice/usermanual', views.usermanual, name='usermanual'),
    path('developer/', views.developer, name='developer'),
    path('SignOut/', views.signout, name='SignOut'),


    # Admin Site URLs
    path('cpanel/', views.cpanel, name='cpanel'),
    path('cpanel/sites/', views.SiteHomeView, name='sites'),
    path('cpanel/sitesUpload/', views.SiteHomeUpload, name='SiteUpload'),
    path('cpanel/SiteDelete/<int:set_id>', views.SiteHomeDelete, name='DeleteSiteS'),
    path('cpanel/SiteUpdate/<int:set_id>', views.SiteHomeUpdate, name='UpdateSiteS'),
    path('cpanel/cdistace/', views.cdistance, name='cpanel_distance'),
    path('cpanel/CourseCreate/', views.DistanceCourseCreate, name='CourseCreate'),
    path('cpanel/CourseUpdate/<int:course_id>', views.DistanceCourseUpdate, name='CourseUpdate'),
    path('cpanel/CourseDelete/<int:course_id>', views.DistanceCourseDelete, name='CourseDelete'),
    path('cpanel/cabout/', views.Services, name='Services'),
    path('cpanel/ServiceCreate/', views.CreateService, name='CreateService'),
    path('cpanel/ServiceUpdate/<int:service_id>', views.ServicesUpdate, name='ServiceUpdate'),
    path('cpanel/ServiceDelete/<int:service_id>', views.ServicesDelete, name='ServiceDelete'),
    path('cpanel/contactus/', views.CContactus, name='CContactus'),
    path('cpanel/ContactusCreate/', views.ContactUs_create, name='Contactus_create'),
    path('cpanel/contactusUpdate/<int:contus_id>', views.ContusUpdate, name='UpdateContUs'),
    path('cpanel/UserLeads/', views.UserLeads, name='UserLeads'),
    path('cpanel/User/', views.NewUsers, name='NewUser'),
    path('cpanel/UpdateUser/', views.update_user_profile, name='userprofile'),





    # Post Detail Site URLs
    path('<slug:slug>/', views.PostDetail, name='post_detail'),
    path('test/', views.test, name='test'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
