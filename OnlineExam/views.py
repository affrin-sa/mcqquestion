from django.shortcuts import render
from OnlineExam.models import Exam
import pyodbc

def examonline(request):
        results=pyodbc.connect('Driver={sql server};'
                               'Server=DESKTOP-BS7S5FS;'
                               'DataBase=OnlineExam;'
                               'Trusted_Connection=yes;')
        cursor=results.cursor()
        cursor.execute('select * from MCQ1')
        results=cursor.fetchall()
        return render(request, 'Index.html', {"Exam":results})

