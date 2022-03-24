from email.policy import default
from hashlib import blake2b
from re import T
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.dispatch import receiver
import os


def validate_image(fieldfile_obj):
    
    filesize = fieldfile_obj.file.size
    kilobyte_limit = 300.0
    if filesize > kilobyte_limit*1024:
        raise ValidationError("Max file size that can be uploaded is %sKB" % str(kilobyte_limit))


def validate_file_size(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    kilobyte_limit = 1024*1024  #1024 byte X 1024 = 1MB
    if filesize > kilobyte_limit:
        raise ValidationError("Max file size that can be uploaded is %sKB" % str(kilobyte_limit))
    else:
        return fieldfile_obj

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/post/' , default="Null")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class contactus_query(models.Model):
    Name = models.CharField(max_length=50)
    ContactNo = models.IntegerField()
    Email = models.EmailField()
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.Name


class Course(models.Model):
    CourseName = models.CharField('Course Name', max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    CourseDetail = models.TextField('Course Detail', max_length=1000, default=True)
    Eligibility = models.CharField(max_length=255)
    CourseDuration_min = models.CharField('Duration Minimum', max_length=50)
    CourseDuration_max = models.CharField('Duration Maxium', max_length=50)
    AnnualFee = models.IntegerField('Annual Fee')
    CourseImage = models.ImageField(upload_to='images/course/',validators=[validate_image], 
    blank=True,help_text='Maximum file size allowed is 100KB')

    def delete(self, using=None, keep_parents=False):
        #self.song.storage.delete(self.song.name)         #file delete
        self.CourseImage.storage.delete(self.CourseImage.name)  # image delete when delete items
        super().delete()

# Deletes old file from filesystem when corresponding `MediaFile` object is updated with new file. Model:Course
@receiver(models.signals.pre_save, sender=Course)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).CourseImage
    except sender.DoesNotExist:
        return False

    new_file = instance.CourseImage
    if old_file == "":
        pass
    else:
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)

# Deletes file from filesystem when corresponding `MediaFile` object is deleted. Model:Course
@receiver(models.signals.post_delete, sender=Course)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.CourseImage:
        if os.path.isfile(instance.CourseImage.path):
            os.remove(instance.CourseImage.path)

     

course = (('B.A','B.A'),('BBA', 'BBA'), ('B.Com', 'B.Com'),('M.A', 'M.A'),('M.Sc.', 'M.Sc.'),('MBA', 'MBA'),('MCA', 'MCA'),('Diploma', 'Diploma'),('Others', 'Others'))
university = (('Subharti University, Meerut','Subharti University, Meerut'), ('JNU , Jaipur', 'JNU , Jaipur'),('Himalayan Garhwal University' , 'HGU'),('Others', 'Others') )
gender = (('MALE','MALE'),('FEMALE','FEMALE'))
class StuRegistrations(models.Model):
    Fname_reg = models.CharField("First Name",max_length=100)
    Lname_reg = models.CharField("Last Name",max_length=100)
    Address_reg = models.CharField("Address",max_length=1000)
    Adhar_reg = models.IntegerField("Adhar No.",)
    gender_reg = models.CharField("Gender",choices = gender,  max_length=50, default='male')
    Email_reg = models.EmailField("E-Mail Address")
    Phone_reg = models.IntegerField("Phone")
    Course_reg = models.CharField("Course",choices = course,max_length=100)
    Uni_reg = models.CharField("University",choices = university,max_length=100)
    date_reg = models.DateTimeField(auto_now=True)


class services(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True , blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/services/')

    def delete(self, using=None, keep_parents=False):
        #self.song.storage.delete(self.song.name)         #file delete
        self.CourseImage.storage.delete(self.image.name)  # image delete when delete items
        super().delete()

    # Deletes old file from filesystem when corresponding `MediaFile` object is updated with new file. Model:Course
@receiver(models.signals.pre_save, sender=services)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    new_file = instance.image
    if old_file == "":
        pass
    else:
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)

# Deletes file from filesystem when corresponding `MediaFile` object is deleted. Model:Course
@receiver(models.signals.post_delete, sender=services)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
