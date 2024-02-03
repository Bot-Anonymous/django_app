import pywhatkit
import time
import pyautogui
from django.shortcuts import render
number=""
message=""
hour=0
min=0
count=0
def handler(a,b,c,d):
    global count
    if count<1:
        pywhatkit.sendwhatmsg(a,b,c,d)
        time.sleep(5)
        pyautogui.press("enter")
    count+=1
def page(request):
    global number,message,hour,min
    dict=request.GET
    number=dict.get('number')
    message=dict.get('message')
    hour=dict.get('hr')
    min=dict.get('min')
    if number!=None:
        handler(number,message,int(hour),int(min))
    return render(request,'index.html')
