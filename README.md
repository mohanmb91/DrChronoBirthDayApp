# Oauth authorization:

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

# Building Home Page

- STEP 1: with the following piece of code I was able to fetch the patients summary JSON data. 
```
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
```
- Step 2: With the help of bootstrap I have designed the following page. As you can see the patients data are sorted based on most recent upcoming birthday's from today (may -21-2017). 
<img width="1435" alt="screen shot 2017-05-21 at 10 25 27 pm" src="https://cloud.githubusercontent.com/assets/14867067/26293904/e8d1ae0a-3e74-11e7-8a1e-2eb2ec67be91.png">
- STEP 3: On click of the Wish button, I am transferring the user_id as an parameter in URL and loading the particular user details into a page and thus, allowing the logged in user to send email for the patient. Below is the following image that gives us a clear picture on how the wish page for Amenda looks like. 
<img width="1378" alt="screen shot 2017-05-21 at 7 04 15 pm" src="https://cloud.githubusercontent.com/assets/14867067/26290551/43c95f00-3e5d-11e7-8024-ba5adab6aeea.png">

# Send Email for the patient. 

- With the following code I am able to send email to the patient. 
```
def sendEmail(request):
email = request.POST['email'];
message = request.POST['BirthDayMessage'];
subject = request.POST['subject'];
send_mail(subject, message,settings.EMAIL_HOST_USER,[email],fail_silently=False);
return redirect('/home')
```

- To do this I need patient's email which will not be provided for the Interview candidate's like me. which leaves me with one choice, to get email address from the user itself. To test my email functionality I have selected Patient Amenda to wish her and decided to use my email instead.
<img width="1354" alt="screen shot 2017-05-21 at 7 05 33 pm" src="https://cloud.githubusercontent.com/assets/14867067/26290734/8e507ecc-3e5e-11e7-9e9f-d1ec7ad13c8b.png">

# Hurray successfully I got the Email. 

<img width="976" alt="screen shot 2017-05-21 at 7 06 15 pm" src="https://cloud.githubusercontent.com/assets/14867067/26290765/d2f450ee-3e5e-11e7-8ab1-357115bc2f87.png">

### Requirements
- [pip](https://pip.pypa.io/en/stable/)
- [python virtual env](https://packaging.python.org/installing/#creating-and-using-virtual-environments)

### Setup
``` bash
$ pip install -r requirements.txt
$ python manage.py runserver
```
# Note: 
- I have not checked in my secretkeys.py which has my client Id and client screct and also this file maintains access_code as well. To run this project create your own secretkeys.py and assign values to these valiables.
```
secret_key = '';
client_id = '';
client_secret ='';
redirect_uri = '';
ACCESS_TOKEN = None;
REFRESH_TOKEN = None;
oauth_code = None;
ACCESS_TOKEN_EXPIRES_IN = None;

GMAIL_ID = '';
GMAIL_PASSWORD = '';
```
