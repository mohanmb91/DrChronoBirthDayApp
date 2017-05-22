from __future__ import print_function;
import secretkeys;
import time;
import requests;
import threading;


def refreshtoken(isRefresh):
    response = "";
    if(isRefresh):
        response = requests.post('https://drchrono.com/o/token/', data={
            'refresh_token': secretkeys.REFRESH_TOKEN,
            'grant_type': 'refresh_token',
            'client_id': secretkeys.client_id,
            'client_secret': secretkeys.client_secret,
            'redirect_uri' : secretkeys.redirect_uri,
        })
        data = response.json();
        print (data);
        print("old Access Token {0}".format(secretkeys.ACCESS_TOKEN));
        secretkeys.ACCESS_TOKEN = data['access_token'];
        secretkeys.REFRESH_TOKEN = data['refresh_token'];
        secretkeys.ACCESS_TOKEN_EXPIRES_IN = data['expires_in'];
        print("new Access Token {0}".format(secretkeys.ACCESS_TOKEN));
    else:
        response = requests.post('https://drchrono.com/o/revoke_token/', data={
            'client_id': secretkeys.client_id,
            'client_secret': secretkeys.client_secret,
            'token': secretkeys.ACCESS_TOKEN,
        });
        data = response.json();
        print (data);




def countdown_refresh_accesstoken(t):
    t = threading.Timer(t, refreshtoken(True));
    t.daemon = True;
    t.start();


