# Send Email for the patient. 

- With the following code I am able to send email to the patient. 
 `def sendEmail(request):
    email = request.POST['email'];
    message = request.POST['BirthDayMessage'];
    subject = request.POST['subject'];
    send_mail(subject, message,settings.EMAIL_HOST_USER,[email],fail_silently=False);
    return redirect('/home')`

- To do this I need patient's email which will not be provided for the Interview candidate's like me. which leaves me with one choice, to get email address from the user itself. To test my email functionality I have selected Patient Amenda to wish her and decided to use my email instead.
<img width="1354" alt="screen shot 2017-05-21 at 7 05 33 pm" src="https://cloud.githubusercontent.com/assets/14867067/26290734/8e507ecc-3e5e-11e7-9e9f-d1ec7ad13c8b.png">

# Hurray successfully I got the Email. 

<img width="976" alt="screen shot 2017-05-21 at 7 06 15 pm" src="https://cloud.githubusercontent.com/assets/14867067/26290765/d2f450ee-3e5e-11e7-8ab1-357115bc2f87.png">

# drchrono Hackathon

### Requirements
- [pip](https://pip.pypa.io/en/stable/)
- [python virtual env](https://packaging.python.org/installing/#creating-and-using-virtual-environments)

### Setup
``` bash
$ pip install -r requirements.txt
$ python manage.py runserver
```
