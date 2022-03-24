from django.shortcuts import render, get_object_or_404, redirect
from .forms import Frm_StuRegistration
from .models import Post,  contactus_query, StuRegistrations, Course, services
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth.models import User
import os
from django.contrib import messages

# this is the Blog post List View


def Home(request):
    service = services.objects.all()
    choices = {'cr': service}
    return render(request, 'home.html', choices)


def blog(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    choices = {'post_list': post_list, }
    return render(request, 'Blogs.html', choices)

# this is the Blog post Detail View


def PostDetail(request, slug):
    post_detail = get_object_or_404(Post, slug=slug)
    template = 'post_detail.html'
    choices = {'post': post_detail, }
    return render(request, template, choices)

# this is the Service Detail Page View


def courseDetail(request, slug):
    course_detail = get_object_or_404(Course, slug=slug)
    template = 'courseDetail.html'
    choices = {'ser': course_detail,}
    return render(request, template, choices)


def contactus_query(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        recepient = request.POST.get('email')
        subject = request.POST.get('Subject')
        phone = request.POST.get('Phone_No')
        message = request.POST.get('message')
        mailto = 'sushilkumar.here@gmail.com'
        if message == '' or recepient == '' or phone == '':
            error = "all fields are required mandetory"
            return render(request, 'error.html', {'error': error})
        send_mail(subject, message, EMAIL_HOST_USER, [
                  recepient, mailto], fail_silently=False)

        #form = contactus_query(Name=fname,  ContactNo=phone, Email=recepient, comment=message)
        # form.save()
        return render(request, 'thanks.html', {'fname': fname})

    return render(request, 'contactus.html')


# this is the Registration Page View
def registrations2(request):
    upload = Frm_StuRegistration()  # Create_scrap_Form is a form
    if request.method == 'POST':
        upload = Frm_StuRegistration(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            messages.success(request, "Item Added successful.")
            return redirect('register')
        else:
            messages.error(request, "Item Unsuccessful")
    
    choices = {'upload_form': upload}
    return render(request, 'register.html', choices)


# this is the Distance Course Page View
def distance_edus(request):
    courses = Course.objects.all()
    choices = {'cr': courses}
    return render(request, 'distance_course.html', choices)
