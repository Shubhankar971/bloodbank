from django.shortcuts import render,HttpResponse,redirect
from .models import bloodbank
from django.contrib.auth.models import User
# Create your views here.
def hi(request):
    return HttpResponse("hi!!")
def create(request):
    if request.method=='POST':
        n=request.POST['pname']
        mail=request.POST['pemail']
        num=request.POST['contactno']
        Not=request.POST['note']
        #print(n,'-',mail,'-',num,'-',Not)
        b=bloodbank.objects.create(name=n,email=mail,num=num,note=Not)
        b.save()
        return redirect('/')
       # return HttpResponse("Data added successfully!!")
    else:
        return render(request,'create.html')
def Home(request):
    b=bloodbank.objects.all()
    print(b)
    context={}
    context['data']=b
    return render(request,'index.html')
    #return HttpResponse("Data fetched successfully!!")
def delete(request,aid):#3
    #print("ID is deleted: ",rID)
    b=bloodbank.objects.get(id=aid)
    b.delete()
    return redirect('/')
   # return HttpResponse("ID is deleted: "+rID)
def edit(request,aid):
    # print("ID is edited: ",rID)
    # return HttpResponse("ID is edited: "+rID)
    if request.method=='POST':
        n=request.POST['pname']
        mail=request.POST['pemail']
        num=request.POST['contactno']
        Not=request.POST['note']
        b=bloodbank.objects.filter(id=aid)
        b.edit(name=n,email=mail,note=Not)
        return redirect('/')
        #return HttpResponse(n +"-"+ mail)
    else:
        b=bloodbank.objects.get(id=aid)
        print(b)
        #return HttpResponse(b)
        context={}
        context['data']=b
        return render(request,'edit.html',context)
        #return redirect('/')
def view_details(request):
    return render(request,'view_details.html')
def register(request):
    if request.method=='POST':
        ufname=request.POST['ufname']
       
        uemail=request.POST['uemail']
        upass=request.POST['upass']
        u=User.objects.create(password=upass,pname=ufname,email=uemail)
        u.save()
        return HttpResponse("User created successfully!!")
    else:
        return render(request,'register.html')
        