# from django.http.response import HttpResponse, HttpResponseRedirect
# from django.urls import reverse


# Create your views here.
# def index(request):
#     return HttpResponseRedirect(reverse('web:test_redirect'));
#
# # RESPONSE REDIRECT
# def test(request):
#     return HttpResponse("Hello Django Again from test redirect");

from django.shortcuts import render
from web.models import AboutClass, RegistrationClass, IssueClass, WhyClass, FrClass,NopClass
from django.http.response import HttpResponse
from web.forms import RegistrationForm
from web.functions import generate_form_errors
import json
from django.urls import reverse


def index(request):

    _about_instances = AboutClass.objects.all()
    _issue_instances = IssueClass.objects.all()
    _why_instances = WhyClass.objects.all()
    _fr_instances = FrClass.objects.all()
    _nop_instances = NopClass.objects.all()

    _form = RegistrationForm
    context = {
        "app_title": "Home",
        "about_instances": _about_instances,
        "issue_instances": _issue_instances,
        "why_instances": _why_instances,
        "fr_instances": _fr_instances,

        "form": _form,
        "is_home": True,
    }
    return render(request, 'web/index.html', context)



def about(request):
    _about_instances = AboutClass.objects.all()
    context = {
        "app_title": "About",
        "about_instances": _about_instances,
        "is_about": True,
    }
    return render(request, 'web/about.html', context);


def registration(request):
    if request.method == "POST":
       #HTML FORM SUBMISSION
        _name = request.POST.get('name')
        _email = request.POST.get('email')
        _phone = request.POST.get('phone')
        _education = request.POST.get('education')
        _dob = request.POST.get('dob')
        _message = request.POST.get('message')
        RegistrationClass.objects.create(
            name=_name, email=_email, phone=_phone, education=_education, dob=_dob, message=_message
        )

        '''   DJANGO FORM SUBMISSION   '''
        _form = RegistrationForm(request.POST)
        if _form.is_valid():
            _form.save()
            response_data = {
                'status': "true",
                'title': "Successfully submitted",
                'message': "message successfully submitted",
            }
        else:
            message = generate_form_errors(_form, formset=False)
            response_data = {
                'status': "false",
                'stable': "true",
                'title': "Form validation error",
                'message': message,
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        return HttpResponse("invalid request!")


def issue(request):
    _issue_instances = IssueClass.objects.all()
    context = {
        "app_title": "Issue",
        "issue_instances": _issue_instances,
        "is_about": True,
    }
    return render(request, 'web/issue.html', context);


def why(request):
    _why_instances = WhyClass.objects.all()
    context = {
        "app_title": "Why",
        "why_instances": _why_instances,
        "is_about": True,
    }
    return render(request, 'web/why.html', context);


def fr(request):
    _fr_instances = FrClass.objects.all()
    context = {
        "app_title": "fr",
        "fr_instances": _fr_instances,
        "is_about": True,

    }
    return render(request,'fr.html',context)


def nop(request):
    _nop_instances = NopClass.objects.all()
    context = {
        "app_title": "nop",
        "fr_instances": _nop_instances,
        "is_about": True,

    }
    return render(request,'nop.html',context)

