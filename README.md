# Building Home Page

- STEP 1: with the following piece of code I was able to fetch the patients summary JSON data. 
> `def getpatients():
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
    return patients;`

- Step 2: With the help of bootstrap I have designed the following page. As you can see the patients data are sorted based on most recent upcoming birthday's from today (may -21-2017).  

<img width="1435" alt="screen shot 2017-05-21 at 10 25 27 pm" src="https://cloud.githubusercontent.com/assets/14867067/26293904/e8d1ae0a-3e74-11e7-8a1e-2eb2ec67be91.png">

- STEP 3: On click of the Wish button, I am transferring the user_id as an parameter in URL and loading the particular user details into a page and thus, allowing the logged in user to send email for the patient. Below is the following image that gives us a clear picture on how the wish page for Amenda looks like. 

<img width="1378" alt="screen shot 2017-05-21 at 7 04 15 pm" src="https://cloud.githubusercontent.com/assets/14867067/26290551/43c95f00-3e5d-11e7-8024-ba5adab6aeea.png">

# drchrono Hackathon

### Requirements
- [pip](https://pip.pypa.io/en/stable/)
- [python virtual env](https://packaging.python.org/installing/#creating-and-using-virtual-environments)

### Setup
``` bash
$ pip install -r requirements.txt
$ python manage.py runserver
```
