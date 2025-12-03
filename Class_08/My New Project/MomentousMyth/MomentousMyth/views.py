from django.shortcuts import render


def home(request):
    return render(request,"home.html")


def entry1(request):
    a = 2000
    b = 200
    c = a*b
    return render(request, "entry1.html",{"c":c})

def entry2(request):
    list1 = [10,20,30]
    print(list1)
    list1.append(40)
    print(list1)
    list1.append(50)
    print(list1)
    list1.append(60)
    print(list1)
    list1.append(80)
    print(list1)
    list1.append(70)
    print(list1)
    return render(request,"entry2.html",{"list1":list1})

def entry3(request):
    if request.methond == "GET":
        return render(request,"entry3.html")
    else:
        n = request.POST.get("n")
        result = int(x)*int(x)
        print("result",result)
        return render(request, "entry3.html",{"result":result})
    
    
    # else:
    #     n = request.POST.get("n")
    #     print("x".x)
    #     return render(request, "entry3.html",{"result":result})
    
def Registrate(request):
      return render(request, "Registrate.html",)
  
def reg1(request):
      if request.method=="POST":
          eid=request.POST["eid"]
          ename=request.POST["ename"]
          
from django.shortcuts import render
from django.http import HttpResponse
# from django.models import 
def regData(request):
    if request.method=='POST',
    eid1=int(request.POST['eid'])
    ename1=request.POST['ename']
    esal1=request.POST['esal']
    eadd1=request.POST['eadd']
    unm1=request.POST['unm']
    pw1=request.POST['pw']
    user = user.objects.create_user(username=unm1, password=pw1)
    
    user.save()
    form Registrate(eid=eid1,ename=ename1,esal=esal1, pw=pw1)
    form.save()
          