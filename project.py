# docs
# create_project(user_email):            # Lets a logged-in user create a project
# view_projects():                       # Displays all projects
# manage_user_projects(user_email):      # Allows owner to edit/delete their projects
# edit_project(all_projects, project):   # Handles editing project fields
# delete_project(all_projects, project): # Deletes a selected project
# search_projects_by_date():             # Filters projects based on start date
# load_projects(), save_projects(), is_valid_date()


import uuid
import json
from datetime import datetime

PROJECTS_FILE = "data/projects.json"

def load_projects():
    with open(PROJECTS_FILE, "r") as f:
        return json.load(f)

def save_projects(projects):
    with open(PROJECTS_FILE, "w") as f:
        json.dump(projects, f)

def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

projects = load_projects()

def create_project(user_email):
    print("\n--- Create New Project ---")
    #Title
    for i in range(3):
        title = input("Title: ")
        if not title:
            print("❌ Title cannot be empty.")
            continue
        if any(p["title"].lower() == title.lower() for p in projects):
            print("❌ A project with this title already exists.")
            continue
        break
    else:
        print("⚠️ Too many failed attempts. Returning to menu.")
        return

    #Details
    details = input("Details (Optional): ")

    #Target
    for i in range(3):
        target_input = input("Target Amount (EGP): ")
        if target_input.isdigit():
            target = int(target_input)
            if target >= 1000:
                break
            else:
                print("❌ Amount must be at least 1000 EGP.")
        else:
            print("❌ Please enter a valid integer amount.")
    else:
        print("⚠️ Too many failed attempts. Returning to menu.")
        return

    #Dates
    for i in range(3):
        start_date = input("Start Date (YYYY-MM-DD): ")
        end_date = input("End Date (YYYY-MM-DD): ")
        if not is_valid_date(start_date) or not is_valid_date(end_date):
            print("❌ One or both dates are invalid.")
            continue
        if start_date > end_date:
            print("❌ Start date cannot be after end date.")
            continue
        break
    else:
        print("⚠️ Too many failed attempts. Returning to menu.")
        return

    #Category
    categories = ["Health", "Education", "Environment", "Technology", "Other"]
    print("\nCategories:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    for i in range(3):
        cat_choice = input("Choose category number: ")
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            category = categories[int(cat_choice) - 1]
            break
        print("❌ Invalid choice. Try again.")
    else:
        print("⚠️ Too many failed attempts. Using 'Other'.")
        category = "Other"

    new_project = {
        "id": str(uuid.uuid4()),
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date,
        "category": category,
        "owner": user_email,
        "donations": 0.0
    }
    projects.append(new_project)
    save_projects(projects)
    print("✅ Project created successfully!")
    input("\n🔁 Press Enter to return to the menu...")
    
def view_projects():
    print("\n--- All Projects ---")
    

    if not projects:
        print("📭 No projects found.")
    else:
        for  p in projects:
            
            print(f"Title: {p['title']}")
            print(f"Details: {p['details']}")
            print(f"Target: {p['target']} EGP")
            print(f"Start: {p['start_date']} | End: {p['end_date']}")
            print(f"Category: {p.get('category', 'N/A')}")
            print(f"Donated: {p.get('donations', 0)} EGP")

    input("\n🔁 Press Enter to return to the menu...")

def manage_user_projects(user_email):
    user_projects = [p for p in projects if p["owner"] == user_email]

    if not user_projects:
        print("\n📭 You have no projects.")
        input("\n🔁 Press Enter to return to the menu...")
        return

    print("\n--- Your Projects ---")
    for i, project in enumerate(user_projects, 1):
        print(f"\n[{i}] {project['title']} | Target: {project['target']} EGP")

    for i in range(3):
        choice_input = input("\nChoose a project number to manage: ")
        if choice_input.isdigit():
            choice = int(choice_input) - 1
            if 0 <= choice < len(user_projects):
                break
        print("❌ Invalid input. Please enter a valid project number.")
    else:
        print("⚠️ Too many failed attempts. Returning to menu.")
        input("\n🔁 Press Enter to return to the menu...")
        return

    selected = user_projects[choice]
    print(f"\nManaging: {selected['title']}")
    print("1. Edit Project")
    print("2. Delete Project")

    action = input("Choose an action: ")
    if action == "1":
        edit_project(projects, selected)
    elif action == "2":
        delete_project(projects, selected)
    else:
        print("❌ Invalid action.")
        input("\n🔁 Press Enter to return to the menu...")

def edit_project(all_projects, project):
    print("\n--- Edit Project ---")

    # Title
    new_title = input(f"New Title ({project['title']}): ")
    title_to_set = new_title or project["title"]
    if title_to_set != project["title"]:  
        existing_titles = [p["title"] for p in all_projects if p != project]
        if title_to_set in existing_titles:
            print("❌ Title already exists. Keeping old title.")
        else:
            project["title"] = title_to_set

    # Details
    project["details"] = input(f"New Details ({project['details']}): ") or project["details"]

    # Target 
    new_target = input(f"New Target ({project['target']}): ")
    if new_target.isdigit() and int(new_target) >= 1000:
        project["target"] = int(new_target)
    elif new_target:
        print("❌ Invalid target. Must be an integer ≥ 1000. Keeping old value.")

    # Start Date
    start = input(f"New Start Date ({project['start_date']}): ")
    if start:
        if is_valid_date(start):
            project["start_date"] = start
        else:
            print("❌ Invalid date format. Keeping old start date.")

    # End Date
    end = input(f"New End Date ({project['end_date']}): ")
    if end:
        if is_valid_date(end):
            project["end_date"] = end
        else:
            print("❌ Invalid date format. Keeping old end date.")

    save_projects(all_projects)
    print("✅ Project updated.")
    input("\n🔁 Press Enter to return to the menu...")

def delete_project(all_projects, project):
    all_projects.remove(project)
    save_projects(all_projects)
    print("🗑️ Project deleted successfully.")
    input("\n🔁 Press Enter to return to the menu...")

def search_projects_by_date():
    print("\n--- Search Projects by Start Date ---")
    date = input("Enter a date (YYYY-MM-DD): ")
    

    matched = [p for p in projects if p["start_date"] == date]

    if not matched:
        print("❌ No projects found with that start date.")
        
    else:
        for i, p in enumerate(matched, 1):
            print(f"\n📌 Project {i}:")
            print(f"Title: {p['title']}")
            print(f"Details: {p['details']}")
            print(f"Target: {p['target']} EGP")
            print(f"Start: {p['start_date']} | End: {p['end_date']}")
            print(f"Category: {p.get('category', 'N/A')}")
            print(f"Donated: {p.get('donated', 0)} EGP")

    input("\n🔁 Press Enter to return to the menu...")

def donate_to_project():
    
    if not projects:
        print("📭 No projects to donate to.")
        input("\n🔁 Press Enter to return to the menu...")
        return

    print("\n--- Available Projects ---")
    for i, p in enumerate(projects, 1):
        collected = p.get("donations", 0)
        print(f"[{i}] {p['title']} | Target: {p['target']} | Collected: {collected}")

    try:
        choice = int(input("Choose project to donate to: ")) - 1
        if choice < 0 or choice >= len(projects):
            print("❌ Invalid project number.")
            input("\n🔁 Press Enter to return to the menu...")
            return
        project = projects[choice]
    except:
        print("❌ Invalid input.")
        input("\n🔁 Press Enter to return to the menu...")
        return

    target = project["target"]
    collected = project.get("donations", 0)
    remaining = target - collected

    if remaining <= 0:
        print("✅ This project has already reached its target.")
        input("\n🔁 Press Enter to return to the menu...")
        return

    print(f"💰 You can donate up to {remaining} EGP.")
    
    for i in range(3):
        amount_input = input("Enter donation amount: ")
        if amount_input.isdigit():
            amount = int(amount_input)
            if 0 < amount <= remaining:
                project["donations"] = collected + amount
                save_projects(projects)
                print(f"💰 Thanks! You donated {amount} EGP.")
                return
            else:
                print(f"❌ Amount must be between 1 and {remaining} EGP.")
        else:
            print("❌ Invalid amount. Must be a positive number.")
    
    print("⚠️ Too many failed attempts.")
    input("\n🔁 Press Enter to return to the menu...")


