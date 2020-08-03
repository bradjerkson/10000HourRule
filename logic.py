from collections import defaultdict
import datetime
import csv

class App:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password, email):
        if username not in self.users:
            self.users[username] = User(username, password, email)
        else:
            raise NameError('User already exists')


    def remove_user(self, username, password):
        pass

    def import_csv(self, username, filename):
        if username in self.users:
            curr = self.users[username]
            curr.import_csv(filename)
        else:
            raise NameError('User does not exist')

    def export_master_csv(self):
        pass

class User:
    #hi
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.skills = {}
    def update_email(self, new_email):
        self.email = new_email

    def add_skill(self, skill_name, date, hours=0, add=True):
        if skill_name not in self.skills:
            new_skill = Skill(skill_name)
            self.skills[skill_name] = new_skill
            self.skills[skill_name].update_hours(hours)
        else:
            if(add):
                self.skills[skill_name].update_hours(hours)
            else:
                self.skills[skill_name].update_hours(-hours)
    def delete_skill(self, skill_name):
        if skill_name in self.skills:
            self.skills.pop(skill_name)
        else:
            raise NameError('No skill found')
    def rename_skill(self, skill_name):
        if skill_name in self.skills:
            self.skills[skill_name].rename(skill_name)
        else:
            raise NameError('No skill found')
    def list_skills(self):
        print("Skills of: ", username)
        for skill in self.skills:
            skill.print_skill()

    def import_csv(self, filename):
        """
        Will import csv in the following structure:
        skill_name | date | hours
        """
        with open(filename, 'rb') as file:
            reader = csv.reader(file)
            for row in reader:
                add_skill(row[0], date, hours)


    def export_csv(self):
        pass



class Skill:
    def __init__(self, name):
        self.name = name
        self.hours = 0
        self.hist = {}
    def update_hours(self, hours):
        self.hours += hours
        self.hist[datetime.datetime.now()] = hours
    def get_skill(self, mame):
        if name == self.name:
            return {name : self.hours}
        else:
            raise NameError('No skill found')
    def print_skill(self):
        print("Skill: " + self.name + "| Hours: " + self.hours)
