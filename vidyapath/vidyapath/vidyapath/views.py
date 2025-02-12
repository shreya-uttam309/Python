from django.shortcuts import render, redirect
from django.http import HttpResponse
from vidyapath_project.models import Registration
from vidyapath_project.models import Notice
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from django.contrib import messages



def home(request):
    all_members=Notice.objects.all()
    return render(request, 'home.html',{'all':all_members})

def register(request):
    return render(request, 'register.html')

def contact(request):
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'aboutus.html')

def adminlogin(request):
    return render(request,'adminlogin.html')

def admindashboard(request):
    all_members=Registration.objects.all()
    return render(request,'admindashboard.html',{'all':all_members})

def notice(request):
    all_notices = Notice.objects.all()
    all_batches = Registration.objects.values_list('batch', flat=True).distinct()  # Fetch distinct batch values

    if request.method == "POST":
        description = request.POST.get("description")
        batch = request.POST.get("batch")

        if description and batch:
            notice = Notice.objects.create(description=description, batch=batch)

            # Fetch students from the selected batch
            students = Registration.objects.filter(batch=batch)
            recipient_list = [student.email for student in students]

            if recipient_list:
                send_mail(
                    subject="New Notice Published",
                    message=f"A new notice has been posted for Batch {batch}:\n\n{description}",
                    from_email="shreyauttam97@gmail.com",
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
                messages.success(request, f"Notice added and email sent to Batch {batch} successfully!")
            else:
                messages.warning(request, f"Notice added, but no students found for Batch {batch}.")

            return redirect("notice")

    return render(request, "notice.html", {'all': all_notices, 'all_batches': all_batches})


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

def update_notice(request,id):
    mem=Notice.objects.get(id=id)
    return render(request,'update_notice.html',{'mem':mem})

def delete1(request,id):
    mem1=Notice.objects.get(id=id)
    mem1.delete()
    return redirect('notice')

def delete(request,id):
    mem=Registration.objects.get(id=id)
    mem.delete()
    return redirect('admindashboard')

def update_notice1(request,id):
    x=request.POST['description']
    mem=Notice.objects.get(id=id)
    mem.description=x
    mem.save()
    return redirect('notice')

def chatbot(request):
    return render(request, 'chatbot.html')

def placement(request):
    return render(request, 'placement.html')

def learningdev(request):
    return render(request, 'learningdev.html')

def placementg(request):
    return render(request, 'placementg.html')

def login(request):
    return render(request, 'login.html')

