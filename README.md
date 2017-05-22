#Oauth authorization is done by executing the following steps: 

- STEP 1:  I have placed an Authorize button through which request parameter's 
`redirect_uri, response_type, client_id, scope` are passed to this API https://drchrono.com/o/authorize/. In response I will be getting a value in code parameter. 
 
- STEP 2: now, I need to use the code value which was sent as an response ASAP to get the access_token. with this piece of code I was able to make call to o/token API. 

``` 
response = requests.post('https://drchrono.com/o/token/', data={
            'code': secretkeys.oauth_code,
            'grant_type': 'authorization_code',
            'redirect_uri': secretkeys.redirect_uri,
            'client_id': secretkeys.client_id,
            'client_secret': secretkeys.client_secret,
        })
```

- With the above code I was able to  get my access_token. now with the access token I can make the required API calls to get the JSON data. 

- In the mean time once i get the access token I start a countdown for 48 hours. After 48 hours access_token expires. so using the following code I am exchanging the old token with new token 

```
response = requests.post('https://drchrono.com/o/token/', data={
            'refresh_token': secretkeys.REFRESH_TOKEN,
            'grant_type': 'refresh_token',
            'client_id': secretkeys.client_id,
            'client_secret': secretkeys.client_secret,
            'redirect_uri' : secretkeys.redirect_uri,
        })
```

- I am able to get the current user information by this piece of code and displaying the username.

```
response = requests.get('https://drchrono.com/api/users/current', headers={
        'Authorization': 'Bearer %s' % secretkeys.ACCESS_TOKEN,
    });
```

<img width="1440" alt="screen shot 2017-05-21 at 7 02 27 pm" src="https://cloud.githubusercontent.com/assets/14867067/26290408/1c40877a-3e5c-11e7-9c7b-63f7677a44de.png">


# drchrono Hackathon

### Requirements
- [pip](https://pip.pypa.io/en/stable/)
- [python virtual env](https://packaging.python.org/installing/#creating-and-using-virtual-environments)

### Setup
``` bash
$ pip install -r requirements.txt
$ python manage.py runserver
```

`social_auth_drchrono/` contains a custom provider for [Python Social Auth](http://psa.matiasaguirre.net/) that handles OAUTH for drchrono. To configure it, set these fields in your `drchrono/settings.py` file:

```
SOCIAL_AUTH_DRCHRONO_KEY
SOCIAL_AUTH_DRCHRONO_SECRET
SOCIAL_AUTH_DRCHRONO_SCOPE
LOGIN_REDIRECT_URL
```
