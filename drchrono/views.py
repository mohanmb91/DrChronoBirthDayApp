# Create your views here.
from django.shortcuts import render
import datetime, requests
import settings;


def get_code(request):
    code = "";

    code = request.GET.get('code', 'NotFound');
    template = "index.html";

    if (code != 'NotFound'):
        response = requests.post('https://drchrono.com/o/token/', data={
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': 'http://127.0.0.1:8000/',
            'client_id': 'IuGRAtJPk75wnuLOS8Wy90bC6DOm1B8t5Yyvm9pA',
            'client_secret': 'fejjegW0rUu2CJE12IeB5JGf7BDu6YhoVTdSvCHmyJX2JngJvRRB5xwJVhWmDQ7cxQ2JlNw7TeyLbpTLSigpm0vjp6WAQpFNlzsUJtZULxzrkpcm0BB3Z9dDly2zOfTZ',
        })
        response.raise_for_status()
        data = response.json()

        access_token = data['access_token']
        settings.ACCESS_TOKEN = access_token;
        refresh_token = data['refresh_token']
        context = {'codeKey': code, 'access_token': access_token, 'refresh_token': refresh_token};

        response = requests.get('https://drchrono.com/api/users/current', headers={
            'Authorization': 'Bearer %s' % access_token,
        })
        response.raise_for_status()
        data = response.json()


        # You can store this in your database along with the tokens
        username = data['username']
        print username;

        headers = {
            'Authorization': 'Bearer %s' % access_token,
        }

        patients = []
        patients_url = 'https://drchrono.com/api/patients_summary'
        while patients_url:
            data = requests.get(patients_url, headers=headers).json()
            patients.extend(data['results'])
            patients_url = data['next']  # A JSON null on the last page
        print patients;
        return render(request, template, context);
    else:
        context = {'codeKey': code};
        return render(request, template, context);

