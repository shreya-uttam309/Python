from django.shortcuts import render, redirect
from django.http import HttpResponse
from vidyapath_project.models import Registration
from vidyapath_project.models import Notice




def home(request):
    all_members=Notice.objects.all()
    return render(request, 'home.html',{'all':all_members})

def register(request):
    return render(request, 'register.html')

def contact(request):
    return render(request,'contact.html')

def adminlogin(request):
    return render(request,'adminlogin.html')

def admindashboard(request):
    all_members=Registration.objects.all()
    return render(request,'admindashboard.html',{'all':all_members})

def notice(request):
    all_members=Notice.objects.all()
    if request.method == "POST":
         description = request.POST["description"]
         
         notices=Notice(
             description=description
         )
         notices.save()
         return redirect('notice')
    
    return render(request,'notice.html',{'all':all_members})

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        batch = request.POST['batch']
        roll_no = request.POST['rollNo']
        smart_card_id = request.POST['smartCardId']
        email = request.POST['email']
        password = request.POST['password']

        # Save data to the database
        new_user=Registration(
            name=name,
            batch=batch,
            rollNo=roll_no,
            smartCardId=smart_card_id,
            email=email,
            password=password
        )
        new_user.save()
        return redirect('home')  # Redirect to the home page after registration

    return render(request, 'register.html')

def update_notice(request):
    return render(request,'update_notice.html')

def delete(request,id):
    mem=Notice.objects.get(id=id)
    mem.delete()
    return redirect("/")

