from django.shortcuts import render, redirect
from tracker.forms import UserForm
from tracker.models import User

# Create your views here.
def new_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
                #TODO catch This
        else:
            form = UserForm()
        return render(request, 'index.html', {'form':form})
    else:
        form = UserForm()
        return render(request, 'index.html', {'form':form})

def show_user(request):
    users = User.objects.all()
    return render(request, "show.html", {'users':users})

def edit_user(request, username):
    user = User.objects.get(username=username)
    return render(request,'edit.html', {'user':user})

def update_user(request, username):
    user = User.objects.get(username=username)
    form = UserForm(request.POST, instance = user)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'user': user})

def destroy_user(request, username):
    user = User.objects.get(username=username)
    user.delete()
    return redirect("/show")

def show_skills(request, username):
    pass

def edit_skill(request, username):
    pass

def update_skill(request, username):
    pass

def destroy_skill(request, username):
    pass
