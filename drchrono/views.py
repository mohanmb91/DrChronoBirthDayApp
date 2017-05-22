# Create your views here.
from StdSuites.AppleScript_Suite import seconds

from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings

import requests;
import globaldata;
import secretkeys;
import refreshtoken;

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template




def get_home(request):
    template = "home.html";

    if (secretkeys.ACCESS_TOKEN == None ):
        secretkeys.oauth_code = request.GET.get('code');
        response = requests.post('https://drchrono.com/o/token/', data={
            'code': secretkeys.oauth_code,
            'grant_type': 'authorization_code',
            'redirect_uri': secretkeys.redirect_uri,
            'client_id': secretkeys.client_id,
            'client_secret': secretkeys.client_secret,
        })
        if(response.status_code == "401"):
            response = requests.post('https://drchrono.com/o/token/', data={
                'refresh_token': secretkeys.REFRESH_TOKEN,
                'grant_type': 'refresh_token',
                'client_id': secretkeys.client_id,
                'client_secret': secretkeys.client_secret,
            })

        if secretkeys.ACCESS_TOKEN == None :
            data = response.json();
            secretkeys.ACCESS_TOKEN = data['access_token']
            secretkeys.REFRESH_TOKEN = data['refresh_token']
            secretkeys.ACCESS_TOKEN_EXPIRES_IN = data['expires_in']
            refreshtoken.countdown_refresh_accesstoken(secretkeys.ACCESS_TOKEN_EXPIRES_IN)
    data = getcurrentuserinfo();
    username = data['username']
    patients = getpatients();
    template = get_template(template);

    context = {'currentuser': username,"patients_data":patients};
    html = template.render(Context(context));
    return HttpResponse(html);


def get_access(request):
    link = "https://drchrono.com/o/authorize/?redirect_uri="+secretkeys.redirect_uri+"&response_type=code&client_id="+secretkeys.client_id+"&scope=patients:summary:read";
    context = {'currentuser': 'Anonymous user','authorizelink':link};
    template = "index.html";
    return render(request, template, context);

def wishpatient(request,id):
    patient_data =  globaldata.patients_records[str(id)];
    context = {'patient':patient_data};
    template = "patientdetails.html";
    return render(request, template, context);


def getpatients():
    patients = []
    patients_url = 'https://drchrono.com/api/patients_summary'
    while patients_url:
        data = requests.get(patients_url, headers={
            'Authorization': 'Bearer %s' % secretkeys.ACCESS_TOKEN,
        }).json();
        patientlist = data['results'];
        for each_patient in patientlist:
            globaldata.patients_records[str(each_patient['id'])] = each_patient;
            patients.append(each_patient);
        patients_url = data['next'];
    return patients;



def getcurrentuserinfo():
    response = requests.get('https://drchrono.com/api/users/current', headers={
        'Authorization': 'Bearer %s' % secretkeys.ACCESS_TOKEN,
    });
    response.raise_for_status()
    data = response.json();
    return data;


def sendEmail(request):
    email = request.POST['email'];
    message = request.POST['BirthDayMessage'];
    subject = request.POST['subject'];
    send_mail(subject, message,settings.EMAIL_HOST_USER,[email],fail_silently=False);
    return redirect('/home')
