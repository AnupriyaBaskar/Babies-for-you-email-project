from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import mysql.connector as sql
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        un=username
        em=email
        pwd=password
        con=sql.connect(host="localhost",user="root",passwd='anupriya17',port="3308",database="babiesforyou")
        cursor=con.cursor()
        cursor.execute("insert into authentication values('{}','{}','{}')".format(un,em,pwd))
        cursor.execute('commit')
        con.close()

        mydict = {'username': username}
        html_template = 'register_email.html'
        html_message = render_to_string(html_template,context=mydict)
        subject = 'Welcome to Babies for you'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
        message.content_subtype = 'html'
        message.send()
        return redirect("success")
    else:
        return render(request, 'index.html')
    
def success(request):
   if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        em1=email
        pwd1=password
        con=sql.connect(host="localhost",user="root",passwd='anupriya17',port="3308",database="babiesforyou")
        cursor=con.cursor()
        cursor.execute("select * from authentication where email='{}' and password='{}'".format(em1,pwd1))
        row=cursor.fetchone()
        if row==None:
            return render(request,'error.html')
        else:
           return render(request,'services.html')
   return render(request,'success.html')




def aboutus(request):
   return render(request,'about.html')

                                      



# Create your views here.
