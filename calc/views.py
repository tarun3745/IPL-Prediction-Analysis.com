from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.checks import messages
from django.shortcuts import render, redirect
import pickle
import joblib
import numpy as np
from email.message import EmailMessage

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# Create your views here.
from calc.decorator import unauthenticated_user
from calc.forms import CreateUserForm
from calc.models import Customer

@login_required(login_url='signin')
def home(request):

    context={'name':'dear user'}
    return render(request,'accounts/winWT.html',context)


@login_required(login_url='signin')
def add(request):

    model=pickle.load(open('pred_win.pkl','rb'))
    number1=int(request.POST.get('num1'))
    number2=int(request.POST.get('num2'))
    number3=int(request.POST.get('num3'))
    number4=int(request.POST.get('num4'))
    number5=int(request.POST.get('num5'))
    
    test=[number1,number2,number3,number4,number5]
    test=np.asarray(test)
    test=test.reshape(1,-1)
    result=model.predict(test)
    result=result[0]
    if result:
        result="HOME TEAM WIL WIN THE MATCH"
    else:
        result="HOME TEAM WILL LOSE THE MATCH"
    

    
    

    return render(request, 'accounts/winWT.html', {'result': result})

@login_required(login_url='signin')
def home2(request):

    context={'name':'dear user'}
    return render(request,'accounts/winWOT.html',context)



@login_required(login_url='signin')
def add2(request):

    model=pickle.load(open('pred_win_noToss.pkl','rb'))
    number1=int(request.POST.get('num1'))
    number2=int(request.POST.get('num2'))
    number3=int(request.POST.get('num3'))
    number4=int(request.POST.get('num4'))
   
    
    test=[number1,number2,number3,number4]
    test=np.asarray(test)
    test=test.reshape(1,-1)
    result=model.predict(test)
    result=result[0]
    
    if result:
        result="HOME TEAM WIL WIN THE MATCH"
    else:
        result="HOME TEAM WILL LOSE THE MATCH"
 
    return render(request, 'accounts/winWOT.html', {'result': result})


@login_required(login_url='signin')
def home3(request):

    context={'name':'dear user'}
    return render(request,'accounts/score.html',context)


@login_required(login_url='signin')
def add3(request):
    print("test")

    model=joblib.load(open('tree_model.pkl','rb'))
    print("test")

    batting_team=str(request.POST.get('num1'))
    bowling_team=str(request.POST.get('num2'))
    number3=int(request.POST.get('num3'))
    number4=int(request.POST.get('num4'))
    number5=int(request.POST.get('num5'))
    number6=int(request.POST.get('num6'))
    number7=int(request.POST.get('num7'))
    prediction_array=[]
    if batting_team == 'Chennai Super Kings':
        prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
    elif batting_team == 'Delhi Daredevils':
        prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
    elif batting_team == 'Kings XI Punjab':
        prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
    elif batting_team == 'Kolkata Knight Riders':
        prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
    elif batting_team == 'Mumbai Indians':
        prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
    elif batting_team == 'Rajasthan Royals':
        prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
    elif batting_team == 'Royal Challengers Bangalore':
        prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
    elif batting_team == 'Sunrisers Hyderabad':
        prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
  # Bowling Team
    if bowling_team == 'Chennai Super Kings':
        prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
    elif bowling_team == 'Delhi Daredevils':
        prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
    elif bowling_team == 'Kings XI Punjab':
        prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
    elif bowling_team == 'Kolkata Knight Riders':
        prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
    elif bowling_team == 'Mumbai Indians':
        prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
    elif bowling_team == 'Rajasthan Royals':
        prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
    elif bowling_team == 'Royal Challengers Bangalore':
        prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
    elif bowling_team == 'Sunrisers Hyderabad':
        prediction_array = prediction_array + [0,0,0,0,0,0,0,1]

    



    prediction_array =  prediction_array + [number3, number4, number5, number6, number7]
    print(prediction_array)

    print("------------------------")
    prediction_array = np.array([prediction_array])
    pred = model.predict(prediction_array)
    result = ""

    result= "The Predicted score is : {}".format(pred[0]) 
    print(result)
    print(type(pred))
    return render(request, 'accounts/score.html', {'result': result})


    

def signout(request):
    logout(request)
    return redirect('signup')




@login_required(login_url='signin')
def home4(request):

    context={'name':'dear user'}
    return render(request,'accounts/mom.html',context)


@login_required(login_url='signin')
def add4(request):

   
    team1=request.POST.get('num1')
    team2=request.POST.get('num2')
    if team2=='csk':
        result = 'Suresh Raina'
    elif team2=='srh':
        result = 'David Warner'
    elif team2=='mi':
        result = 'Rohit Sharma'
    elif team2=='rcb':
        result = 'Virat Kohli'
    elif team2=='dc':
        result = 'Rishab Pant'
    elif team2=='pbks':
        result = 'KL Rahul'
    elif team2=='RR':
        result = 'Sanju Samson'
    elif team2=='kkr':
        result = 'Andre Russell'
    
    return render(request, 'accounts/mom.html', {'result': result})




@login_required(login_url='signin')
def home5(request):

    context={'name':'dear user'}
    return render(request,'accounts/feedback.html',context)


@login_required(login_url='signin')
def add5(request):

   
    email=request.POST.get('num1')
    feed=request.POST.get('num2')
    num=request.POST.get('num3')

    msg = MIMEMultipart()
    msg['Subject'] = 'You Got A Feed back from '+email
    msg['From'] = 'editorial.iplprediction@gmail.com'
    msg['To'] = 'editorial.iplprediction@gmail.com'

    text = MIMEText("Feed: "+feed + "\n \n contact number:" + num + "\n Email: " + email)
    msg.attach(text)
    #image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    #msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('editorial.iplprediction@gmail.com', 'IPL@Predict')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
   
    result = 'Feedback submitted successfully'
    
    return render(request, 'accounts/feedback.html', {'result': result})

@unauthenticated_user
def singup(request):
    formSet=CreateUserForm()
    if request.method=="POST":
        formSet=CreateUserForm(request.POST)
        if formSet.is_valid():
            user=formSet.save()
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                name=user.username,
                email=user.email
            )
            return redirect('signin')
    context={'formSet':formSet}
    return render(request,'accounts/signup.html',context)


@unauthenticated_user
def signin(request):

    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("winWT")
        else:
            context = {'message':'wrong pass or username'}
            return render(request, 'accounts/signin.html', context)

    context={}
    return render(request,'accounts/signin.html',context)



