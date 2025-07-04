from auth import register, login
from project import (
    create_project,
    view_projects,
    manage_user_projects,
    search_projects_by_date,
    donate_to_project
)


def guest_menu():
    tries = 0
    while True:
        print("\n--- Crowd-Funding App ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register()
            tries = 0  
        elif choice == "2":
            user = login()
            if user:
                tries = 0
                user_menu(user)
        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break
        else:
            tries += 1
            print("❌ Invalid choice. Try again.")

            if tries >= 3:
                print("⚠️ Too many invalid attempts. Exiting program.")
                break





def user_menu(user):
    tries = 0
    while True:
        print(f"\n--- Welcome {user['first_name']} ---")
        print("1. Create Project")
        print("2. View All Projects")
        print("3. Manage My Projects")
        print("4. Search Projects by Start Date")
        print("5. Donate to a Project")
        print("6. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            create_project(user["email"])
            tries = 0
        elif choice == "2":
            view_projects()
            tries = 0
        elif choice == "3":
            manage_user_projects(user["email"])
            tries = 0
        elif choice == "4":
            search_projects_by_date()
            tries = 0
        elif choice == "5":
            donate_to_project()
            tries = 0
        elif choice == "6":
            print("🔒 Logged out successfully.")
            break
        else:
            tries += 1
            print("❌ Invalid choice.")

            if tries >= 3:
                print("⚠️ Too many invalid attempts. Logging out.")
                break


# Entry point of the app
if __name__ == "__main__":
    guest_menu()
