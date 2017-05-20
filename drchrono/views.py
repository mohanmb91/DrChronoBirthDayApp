# Create your views here.
from StdSuites.AppleScript_Suite import seconds

from django.shortcuts import render;
import requests;

import secretkeys;
import refreshtoken;



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
    context = {'currentuser': username,"patients_data":patients};
    return render(request, template, context);



def get_access(request):
    link = "https://drchrono.com/o/authorize/?redirect_uri="+secretkeys.redirect_uri+"&response_type=code&client_id="+secretkeys.client_id+"&scope=patients:summary:read";
    context = {'currentuser': 'Anonymous user','authorizelink':link};
    template = "index.html";
    return render(request, template, context);

def wishpatient(request,id):
    pass;


def getpatients():
    patients = []
    patients_url = 'https://drchrono.com/api/patients_summary'
    while patients_url:
        data = requests.get(patients_url, headers={
            'Authorization': 'Bearer %s' % secretkeys.ACCESS_TOKEN,
        }).json()
        patientlist = data['results'];
        for each_patient in patientlist:
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