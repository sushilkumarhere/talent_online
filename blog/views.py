from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import sitecreate, course_create, service_create
from .models import Post, AboutUs, SiteSetting, ContactUs, user_register, registrations, Course, services
from django.shortcuts import render, get_object_or_404, redirect
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth import logout


# this is the Blog post List View
def PostList(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    site_sett = SiteSetting.objects.all()
    cont = ContactUs.objects.get(pk=1)
    choices = {'post_list': post_list, 'site_sett': site_sett, 'cont_us': cont}
    return render(request, 'index.html', choices)


# this is the Blog post Detail View
def PostDetail(request, slug):
    post_detail = get_object_or_404(Post, slug=slug)
    template = 'post_detail.html'
    site_sett = SiteSetting.objects.all()
    choices = {'post': post_detail, 'site_sett': site_sett}
    return render(request, template, choices)


# this is the About Us Page View
def about(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        recepient = request.POST.get('email')
        message = request.POST.get('message')
        mailto = 'sushilkumar.here@gmail.com'
        if message == '' or recepient == '':
            error = "all fields are required mandetory"
            return render(request, 'error.html', {'error': error})
        send_mail('subject', message, EMAIL_HOST_USER, [recepient, mailto], fail_silently=False)
        form = user_register(Name=fname, Address=lname, ContactNo=phone, Email=recepient, comment=message)
        form.save()
        return render(request, 'thanks.html', {'fname': fname})
    site_sett = SiteSetting.objects.all()
    cont = ContactUs.objects.get(pk=1)
    abt = AboutUs.objects.get(pk=6)
    service = services.objects.all()
    choices = {'site_sett': site_sett, 'cont_us': cont, 'about1': abt, 'cr': service}
    return render(request, 'aboutus.html', choices)


# this is the Course Page View
def Course1(request):
    course = Course.objects.all()
    cont = ContactUs.objects.get(pk=1)
    site_sett = SiteSetting.objects.all()
    choices = {'course': course, 'site_sett': site_sett, 'cont_us': cont}
    return render(request, 'dde/course.html', choices)


# this is the Login Page View
@login_required
def cpanel(request):
    return render(request, 'cpanel/Chome.html')


# this is the Registration Page View
def registrations2(request):
    if request.method == 'POST':
        fname = request.POST.get('Fname')
        lname = request.POST.get('Lname')
        addr = request.POST.get('Address')
        adhar = request.POST.get('Adhar')
        gender = request.POST.get('gender')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        course = request.POST.get('Course')
        uni = request.POST.get('Uni')
        if fname == '' or adhar == '' or phone == '':
            error = "all fields are required mandetory"

        print(fname, lname, addr, adhar, phone, course, gender)
        form1 = registrations(Fname_reg=fname, Lname_reg=lname, Address_reg=addr, Adhar_reg=adhar, gender_reg=gender,
                              Email_reg=email, Phone_reg=phone, Course_reg=course, Uni_reg=uni)
        form1.save()
        return render(request, 'thanks.html', {'fname': fname, 'lname': lname})
    site_sett = SiteSetting.objects.all()
    cont = ContactUs.objects.get(pk=1)
    choices = {'site_sett': site_sett, 'cont_us': cont}
    return render(request, 'register.html', choices)


# this is the Distance Course Page View
def distance_edus(request):
    site_sett = SiteSetting.objects.all()
    cont = ContactUs.objects.get(pk=1)

    courses = Course.objects.all()

    choices = {'site_sett': site_sett, 'cont_us': cont, 'cr': courses}
    return render(request, 'dde/distance_course.html', choices)


# this is the CPanel Distance Course Page View
@login_required
def cdistance(request):
    courses = Course.objects.all()

    return render(request, 'cpanel/SiteCourse/Cdistance.html', {'cr': courses})


# this is the CPanel Distance Course Upload  Page View
@login_required
def DistanceCourseCreate(request):
    upload = course_create()  # course_create is a form
    if request.method == 'POST':
        upload = course_create(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('cpanel_distance')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'CourseCreate'}}">reload</a>""")
    else:
        return render(request, 'cpanel/SiteCourse/CdistanceCreate.html', {'upload_form': upload})


# this is the CPanel Course Update Page View
@login_required
def DistanceCourseUpdate(request, course_id, template_name='cpanel/SiteCourse/CdistanceUpdate.html'):
    post = get_object_or_404(Course, pk=course_id)  # Course is a  Model
    form = course_create(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('cpanel_distance')
    return render(request, template_name, {'form': form})


# this is the CPanel Course Delete  Page View
@login_required
def DistanceCourseDelete(request, course_id):
    ss_id = int(course_id)
    try:
        s = Course.objects.get(id=ss_id)  # Course is a  Model
    except Setting.DoesNotExist:
        return redirect('cpanel_distance')
    s.delete()
    return redirect('cpanel_distance')


@login_required
def developer(request):
    """ Developer """
    return render(request, 'cpanel/developer.html')


# this is the CPanel Site Setting List  Page View
@login_required
def SiteHomeView(request):
    site_sett = SiteSetting.objects.all()
    return render(request, 'cpanel/SiteHome/SiteHome.html', {'site_set1': site_sett})


# this is the CPanel Site Setting Upload  Page View
@login_required
def SiteHomeUpload(request):
    upload = sitecreate()  # form.py
    if request.method == 'POST':
        upload = sitecreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('sites')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'SiteUpload'}}">reload</a>""")
    else:
        return render(request, 'cpanel/SiteHome/SiteHomeCreat.html', {'upload_form': upload})


# this is the CPanel Site Setting Update Page View
@login_required
def SiteHomeUpdate(request, set_id, template_name='cpanel/SiteHome/SiteHomeUpdate.html'):
    post = get_object_or_404(SiteSetting, pk=set_id)
    form = sitecreate(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('sites')
    return render(request, template_name, {'form': form})


# this is the CPanel Site Setting Delete  Page View
@login_required
def SiteHomeDelete(request, set_id):
    ss_id = int(set_id)
    try:
        s = SiteSetting.objects.get(id=ss_id)
    except Setting.DoesNotExist:
        return redirect('sites')
    s.delete()
    return redirect('sites')


@login_required
def cabout(request):
    service = services.objects.all()

    return render(request, 'cpanel/SiteAbout/Cabout.html', {'cr': service})


@login_required
def CreateService(request):
    upload = service_create()  # service_create is a form
    if request.method == 'POST':
        upload = service_create(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('cpanel_about')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'CourseCreate'}}">reload</a>""")
    else:
        return render(request, 'cpanel/SiteAbout/CAboutCreate.html', {'upload_form': upload})


@login_required
def ServicesUpdate(request, service_id, template_name='cpanel/SiteAbout/CAboutUpdate.html'):
    post = get_object_or_404(services, pk=service_id)  # services is a  Model
    form = service_create(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('cpanel_about')
    return render(request, template_name, {'form': form})


@login_required
def ServicesDelete(request, service_id):
    ss_id = int(service_id)
    try:
        s = services.objects.get(id=ss_id)  # Service is a  Model
    except Setting.DoesNotExist:
        return redirect('cpanel_about')
    s.delete()
    return redirect('cpanel_about')


def signout(request):
    logout(request)
    return redirect('home')


def test(request):
    """ Developer """
    return render(request, 'test.html')
