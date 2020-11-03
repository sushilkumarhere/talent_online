from django.db import models

from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/post/')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class user_register(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=500)
    ContactNo = models.IntegerField()
    Email = models.EmailField()
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.Name


class Course(models.Model):
    CourseName = models.CharField('Course Name', max_length=255)
    CourseDetail = models.TextField('Course Detail', max_length=1000, default=True)
    Eligibility = models.CharField(max_length=255)
    CourseDuration_min = models.CharField('Course Duration Minimum', max_length=50)
    CourseDuration_max = models.CharField('Course Duration Minimum', max_length=50)
    AnnualFee = models.IntegerField('Annual Fee')
    CourseImage = models.ImageField(upload_to='images/course/', default='null')


class AboutUs(models.Model):
    about_head = models.CharField(max_length=50, default='About ...')
    about = models.TextField(max_length=10000)
    about_img = models.ImageField(upload_to='images/about_img/')


class SiteSetting(models.Model):
    Firm = models.CharField(max_length=50, default='Company Name')
    FirmLogo = models.ImageField(upload_to='images/site_sett_img/')
    main_slider_mission = models.CharField(max_length=500, default='About')
    main_slider_img = models.ImageField(upload_to='images/site_sett_img/', default='nul')


class ContactUs(models.Model):
    Address1 = models.TextField(max_length=1000, default='Address')
    Address2 = models.TextField(max_length=1000, default='Address')
    State = models.CharField(max_length=100)
    Distt = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)
    Email = models.EmailField('Email Address')
    Phone = models.IntegerField(default=91)


class registrations(models.Model):
    Fname_reg = models.CharField(max_length=100)
    Lname_reg = models.CharField(max_length=100)
    Address_reg = models.CharField(max_length=1000)
    Adhar_reg = models.IntegerField()
    gender_reg = models.CharField(max_length=6, default='male')
    Email_reg = models.EmailField('Email Address')
    Phone_reg = models.IntegerField()
    Course_reg = models.CharField(max_length=100)
    Uni_reg = models.CharField(max_length=100)
    date_reg = models.DateTimeField(auto_now=True)


class services(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/services/')
