from django.contrib import admin
from .models import Post, user_register, AboutUs, SiteSetting, ContactUs, registrations, Course


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'image')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}



class UserRegister(admin.ModelAdmin):
    list_display = ('Name', 'Address', 'ContactNo', 'Email', 'comment')
    search_fields = ('Name', 'Address', 'ContactNo', 'Email', 'comment')
    list_filter = ("Name",)


class course_register(admin.ModelAdmin):
    list_display = (
        'date_reg', 'Fname_reg', 'Lname_reg', 'Adhar_reg', 'Email_reg', 'Phone_reg', 'Course_reg', 'Uni_reg')
    search_fields = (
        'date_reg', 'Fname_reg', 'Lname_reg', 'Adhar_reg', 'Email_reg', 'Phone_reg', 'Course_reg', 'Uni_reg')


admin.site.register(Post, PostAdmin)
admin.site.register(user_register, UserRegister)
admin.site.register(AboutUs)
admin.site.register(SiteSetting)
admin.site.register(ContactUs)
admin.site.register(registrations, course_register)
admin.site.register(Course)

admin.site.site_header = 'Talent Online Classes'
