from django.shortcuts import render, redirect, HttpResponse
from .models import Password_manager

#! Read 
def read(request):
    pass_name = Password_manager.objects.all()
    print(pass_name)
    
    return render(request, "pass.html",{"pass_name":pass_name})

#! Create 
def create(request):
    if request.POST:
        
        App_pass=request.POST["App_pass"]
        User_pass=request.POST["User_pass"]
        email_pass=request.POST["email_pass"]
        password_pass=request.POST["password_pass"]
        
        Password_manager.objects.create(App_pass=App_pass,User_pass=User_pass,email_pass=email_pass,password_pass=password_pass)
        print(App_pass,User_pass,email_pass,password_pass)
        return redirect(read)
#! Search
def search(request):
    query = request.GET.get('Search_bar')
    if query:
        pass_name = Password_manager.objects.filter(App_pass__icontains=query)
    else:
        pass_name = Password_manager.objects.all()
    return render(request, "pass.html", {"pass_name": pass_name})




#! Update
def update(request,id):
    pass_name = Password_manager.objects.get(id=id)
    print(pass_name)
    if request.POST:
        App_pass=request.POST["App_pass"]
        User_pass=request.POST["User_pass"]
        email_pass=request.POST["email_pass"]
        password_pass=request.POST["password_pass"]
        
        pass_name.App_pass=App_pass
        pass_name.User_pass=User_pass
        pass_name.email_pass=email_pass
        pass_name.password_pass=password_pass
        pass_name.save()
        print(App_pass,User_pass,email_pass,password_pass)
        return redirect(read)
    else:
        return render(request,'pass.html')

#! Delete
def delete(request,id):
    if request.POST:
        pass_name = Password_manager.objects.get(id=id)
        pass_name.delete()
        return redirect(read)
    return render(request,'pass.html')

def viewpage(request):
    return render(request, "viewspass.html")