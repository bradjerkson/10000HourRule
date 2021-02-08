from collections import defaultdict
import datetime
import csv
import re
import getpass
import dill

#exec(open("./filename").read())

class App:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password, email):
        if username not in self.users:
            self.users[username] = User(username, password, email)
        else:
            raise NameError('User already exists')

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            raise NameError('User does not exist')



    def remove_user(self, username, password):
        if username in self.users:
            self.users[username] = None
        else:
            raise NameError('User does not exist')

    def import_csv(self, username, filename):
        if username in self.users:
            curr = self.users[username]
            curr.import_csv(filename)
        else:
            raise NameError('User does not exist')

    def export_master_csv(self):
        pass

    def import_evernote_format(self, username, filename):
        if username in self.users:
            curr = self.users[username]
            curr.import_evernote_format(filename)
        else:
            raise NameError('User does not exist')

class User:
    #hi
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.skills = {}
    def update_email(self, new_email):
        self.email = new_email

    def update_password(self, new_password):
        self.password = new_password

    def add_skill(self, skill_name, hours=0, add=True):
        if skill_name not in self.skills:
            try:
                new_skill = Skill(skill_name)
                self.skills[skill_name] = new_skill
                self.skills[skill_name].update_hours(hours)
            except:
                raise NameError("Skill creation issue")
        else:
            try:
                if(add):
                    self.skills[skill_name].update_hours(hours)
                else:
                    self.skills[skill_name].update_hours(-hours)
            except:
                raise NameError("Skill update issue")
    def delete_skill(self, skill_name):
        if skill_name in self.skills:
            self.skills.pop(skill_name)
        else:
            raise NameError('No skill found')
    def rename_skill(self, skill_name, new_name):
        if skill_name in self.skills:
            self.skills[skill_name].rename(skill_name, new_name)
        else:
            raise NameError('No skill found')
    def list_skills(self):
        print("Skills of: ", self.username)
        for skill in self.skills:
            self.skills[skill].print_skill()

    def import_csv(self, filename):
        """
        Will import csv in the following structure:
        skill_name | date | hours
        """
        try:
            with open(filename, 'rb') as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        self.add_skill(row[0], hours)
                    except:
                        print("errors with reading row in CSV file")
                        continue
        except:
            print("CSV reading errors")

    def import_evernote_format(self, filename, username):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    #Capture items in brackets
                    attr = re.search(r"\[(\w+)\]", line)
                    parsed_line = line.strip().split(':')
                    name = parsed_line[0]
                    val = parsed_line[1].rstrip(" (Total")
                    print(name, val)
                    try:
                        self.add_skill(name, hours=float(val))
                    except:
                        print("Errors with adding skill in Text file")
                        continue
        except:
            print("errors with reading Evernote text file")


    def merge_skills(self, skill1, skill2):
        pass

    def export_csv(self):
        filename = self.username + ".csv"
        fieldnames = ['skill_name', 'date', 'hours']
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, fieldnames=fieldnames)
            writer.writeheader()
            for skill in self.skills:
                writer.writerow([skill, '' , self.skills[skill].hours])
        print("CSV has been outputted")



class Skill:
    def __init__(self, name):
        self.name = name
        self.hours = 0
        self.hist = {}
        self.tags = []
        self.rankings = {"Beginner":10, "Novice":25, "Apprentice":50, "Journeyman":100, "Competent":500, "Proficient":1000, "Competent":2500, "Expert":5000, "Master":7500, "Doctor":10000 }
        #e.g. KMs
        self.attributes = {}
    def update_hours(self, hours):
        self.hours += hours
        self.hist[datetime.datetime.now()] = hours
    def get_skill(self, name):
        if name == self.name:
            return {name : self.hours}
        else:
            raise NameError('No skill found')
    def rename_skill(self, name, new_name):
        if name == self.name:
            self.name = new_name
    def print_skill(self):
        print("Skill: " + self.name + " | Hours: " + str(self.hours))


class Tag:
    def __init__(self, tagname):
        self.tagname = tagname


def test_driver():
    user = "Brad Jackson"
    pw = "Welcome123"
    email = "bradley_jackson@ymail.com"
    file = "history.txt"
    environment = App()
    environment.add_user(user, pw, email)
    brad = environment.get_user(user)
    brad.import_evernote_format(file, user)
    brad.list_skills()
    return (environment, brad)


def user_process(app):
    newUser = check_new_user()
    if(newUser):
        return pull_user(app, True)
    else:
        return pull_user(app, False)

def commence_new():
    app = App()
    start(app)

def resume():
    app = load_saved_app()
    start(app)

def start(app):
    user = user_process(app)
    while True:
        menu = input("[U]ser | [S]kills | [I]mport | [E]xport | [L]ogout | [Q]uit")
        if menu.lower() == 'u':
            pass
        elif menu.lower() == 's':
            skill_menu(user)
        elif menu.lower() == 'i':
            filename = input("please enter the filename (plus file format) to import")
            try:
                user.import_csv(filename)
            except:
                print("Please provide a real filename")
        elif menu.lower() == 'e':
            user.export_csv()
        elif menu.lower() == 'l':
            user = user_process(app)
        elif menu.lower() == 'q':
            exit()
        else:
            print("Please enter a correct menu input")

def skill_menu(user):
    skill_menu = input("[L]ist Skills | [R]ename Skill | [D]elete Skill | [A]dd Skill")
    if skill_menu.lower()=='l':
        user.list_skills()
    elif skill_menu.lower()=='r':
        skill_name = input("Please enter your skill name: ")
        user.add_skill(skill_name)
        #TODO: Sanitise this input
        new_skill_name = input("Rename skill to?: ")
        skill = "Rename " + skill_name + " to " + new_skill_name + ", are you sure?"
        rename_confirm = input(skill)
        if rename_confirm.lower() in ['y', 'yes']:
            user.rename_skill(skill, new_skill_name)
            print("Skill renamed")

    elif skill_menu.lower()=='d':
        skill_name = input("Please enter your skill name: ")
        skill = "Delete " + skill_name + ", are you sure?"
        deletion_confirm = input(skill)
        if deletion_confirm.lower() in ['y', 'yes']:
            user.delete_skill(skill_name)
            print("Skill deleted")
        else:
            "Skill was NOT removed"
    elif skill_menu.lower()=='a':
        skill_name = input("Please enter your skill name: ")
        user.add_skill(skill_name)
    else:
        print("Please enter a correct skill menu input")

def user_menu(user):
    user_menu = input("[U]pdate email | [C]hange password")
    if(user_menu).lower()=='u':
        update_email(user)
    elif(user_menu).lower() == 'c':
        pass

def update_email(user):
    email = input("Please enter your new email address: ")
    email_input = "Delete " + email + ", are you sure?"
    email_confirm = input(email_input)
    if email_confirm.lower() in ['y', 'yes']:
        user.update_email(email)

def update_password(user):
    password = input("Please enter your new email address: ")
    password_input = "Delete " + password + ", are you sure?"
    password_confirm = input(password_input)
    if password_confirm.lower() in ['y', 'yes']:
        user.update_password(password)

def check_new_user():
    while True:
        print("Welcome to 10,000 Hour Rule")
        newUser = input("Are you a new user? (Y/N): ")
        if newUser.lower() in ['y', 'yes']:
            return True
        elif newUser.lower() in ['no', 'n', 'nope']:
            return False
        else:
            print("Please enter either Yes or No")

def pull_user(app, new=True):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = getpass.getpass(prompt="Please enter your password")
    if new:
        app.add_user(name, password, email)
        user = app.get_user(name)
    else:
        user = app.get_user(name)
    return user

def save_state(app):
    dill.dump(app, file=open("app.pickle", "wb"))

def load_state(app):
    dill_file = open("app.pickle", "rb")
    app = dill.load(dill_file.read())
    return app
