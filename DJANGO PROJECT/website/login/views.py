from django.shortcuts import render
import mysql.connector as sql

em = ''
pwd = ''

# Create your views here.
def loginaction(request):
    global em, pwd
    if request.method == 'POST':
        m = sql.connect(host="localhost", user="root", password="root", database="website")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == 'email':
                em = value
            if key == 'password':
                pwd = value
        query = "select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(query)
        data = tuple(cursor.fetchall())
        print(data)
        if data == ():
            return render(request,'error.html')
        else:
            return render(request,'welcome.html',{'data':data})
        
    return render(request,'login_page.html')