def register_freelancer(name):
    return "Freelancer " + name + " registered"

print(register_freelancer("Aisha"))

def search_freelancer(name, skill):
    return "Searching for " + name + " with skill " + skill

print(search_freelancer("Aisha", "Python"))

def search_freelancer(name, skill, location):
    return name + " | " + skill + " | " + location

print(search_freelancer("Aisha", "Python", "Mumbai"))
