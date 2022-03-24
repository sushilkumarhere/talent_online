from django.contrib import admin
from django.contrib.admin.models import LogEntry
from blog.models import Post, StuRegistrations, Course, services, contactus_query


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'image')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class courseAdmin(admin.ModelAdmin):
    list_display = ('CourseName', 'Eligibility', 'CourseDetail', 'AnnualFee', 'CourseImage')
    list_filter = ("CourseName",)
    search_fields = ['CourseName', 'CourseDetail']


class serviceAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image',)
    list_filter = ("title",)


class contactus_query(admin.ModelAdmin):
    list_display = ('Name', 'Address', 'ContactNo', 'Email', 'comment')
    search_fields = ('Name', 'Address', 'ContactNo', 'Email', 'comment')
    list_filter = ("Name",)


class course_register(admin.ModelAdmin):
    list_display = (
        'date_reg', 'Fname_reg', 'Lname_reg', 'Adhar_reg', 'Email_reg', 'Phone_reg', 'Course_reg', 'Uni_reg')
    search_fields = (
        'date_reg', 'Fname_reg', 'Lname_reg', 'Adhar_reg', 'Email_reg', 'Phone_reg', 'Course_reg', 'Uni_reg')


class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = 'action_time'

    # to filter the resultes by users, content types and action flags
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
    ]


admin.site.register(Post, PostAdmin)
#admin.site.register(ContactUs)
admin.site.register(StuRegistrations, course_register)
admin.site.register(Course, courseAdmin)
admin.site.register(services, serviceAdmin)
admin.site.register(LogEntry)



admin.site.site_header = 'Talent Online Classes'
