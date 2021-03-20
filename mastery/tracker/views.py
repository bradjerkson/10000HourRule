from django.shortcuts import render, redirect
from tracker.forms import UserForm, SkillForm
from tracker.models import User, Skill

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
    user = User.objects.get(id=username)
    try:
        skills = user.skill_set.all()
        print(skills.count())
    #try:
    #    skills = Skill.objects.get(skill_username=username)
    except Skill.DoesNotExist:
        skills = None
    return render(request, "show_skill.html", {'skills':skills, 'skill_username':username})

def new_skill(request, username):
    skill = Skill.objects.get()
    user = User.objects.get(id=username)

    if request.method == "POST":
        form = SkillForm(request.POST)
        print("Posted!")

        if form.is_valid():
            print("Valid Form!")
            print(form)
            print(form.cleaned_data)
            skill = Skill.objects.create_skill( \
                skill_name = form.cleaned_data['skill_name'], \
                skill_hours = form.cleaned_data['skill_hours'], \
                skill_username = user)
            """
            skill.skill_name = form.cleaned_data['skill_name']
            skill.skill_hours = form.cleaned_data['skill_hours']
            skill.skill_username = username
            """
            try:
                skill.save()
                return redirect('/show_skills/' + username)
            except Exception as e:
                print(e)
            """
            form.clean()
            try:
                form.save()
                return redirect('/show_skills/' + username)
            except Exception as e:
                print(e)
                #return redirect('/new_user')
                #return redirect ('/oops')
                #pass
                #TODO catch This
            """
        else:
            form = SkillForm()
        return render(request, 'new_skill.html', {'form':form, 'skill_username':username})
    else:
        form = SkillForm()
        return render(request, 'new_skill.html', {'form':form, 'skill_username':username})


def edit_skill(request, username):
    pass

def update_skill(request, username):
    pass

def destroy_skill(request, username):
    pass

def oops(request):
    return redirect('/oops')
