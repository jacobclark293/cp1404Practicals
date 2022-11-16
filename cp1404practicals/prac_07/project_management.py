"""
CP1404
Time estimate: 2.5 hours
"""

MENU = "choose"
HEADER = "Name  Start Date  Priority"
FILENAME = "projects.txt"


def main():
    projects = load_projects(FILENAME)
    print(MENU)
    in_file = open("projects.txt", 'r')
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            filename = input("Enter filename: ")
            load_projects(filename)
        elif choice == 'S':
            filename = input("Enter filename: ")
            save_projects(filename)
            print("Save Projects")
        elif choice == 'D':
            display_projects(in_file)
        elif choice == 'F':
            print("Filter")
        elif choice == 'A':
            print("Update")
        elif choice == "U":
            print("Update")
        else:
            print("Invalid")
        print(MENU)
        choice = input(">>> ").upper()
    print("exit")


def load_projects(filename):
    projects = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            line = line.strip()
            parts = line.split(' ')
            projects.append(parts)
    print(projects)


def save_projects(projects, filename):
    with open(filename, 'w') as in_file:
        print(HEADER, file=out_file)
        for project in projects:
            print(f"{project.name}\t")
    pass


def display_projects(projects):
    """Display in two groups: incomplete projects; completed projects, both sorted """
    print("Incomplete")
    incomplete_projects = [project for project in projects if not project.is_complete]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", project)
    print("Complete")
    complete_projects = [project for project in projects if project.is_complete()]
    complete_projects.sort()
    for project in complete_projects:
        print(" ", project)

    complete_projects[0].name = "test"


def filter_projects():
    pass


def add_project():
    pass


def update_projects(projects):
    for i, project in enumerate(projects):
        print(i, project)
    index = int(input("Project choice "))
    project = projects[index]
    print(project)
    try:
        percent_complete = int(input("new percent: "))
        project.percent_complete = percent_complete
    except ValueError:
        pass
    try:
        priority = int("New Priority: ")
        project.priority = priority
        
    except ValueError:
        pass



main()
