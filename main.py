from app import auth, views, models

def display_menu():
    print("""
=== Welcome to the Blogging Platform ===
1. Register
2. Login
3. Exit
""")
    
    choice = input("Choose an option: ")
    return choice

def user_menu(username):
    print(f"\nWelcome back, {username}!")
    print("1. View Posts\n2. Create Post\n3. Edit Post\n4. Delete Post\n5. Logout\n")

    choice = input("Choose an option: ")
    return choice

def run():
    while True:
        choice = display_menu()
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            auth.register_user(username, password)
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if auth.login_user(username, password):
                while True:
                    user_choice = user_menu(username)
                    
                    if user_choice == '1':
                        views.view_posts(username)
                    elif user_choice == '2':
                        views.create_post(username)
                    elif user_choice == '3':
                        views.edit_post(username)
                    elif user_choice == '4':
                        views.delete_post(username)
                    elif user_choice == '5':
                        print("Logging out...\n")
                        break
                    else:
                        print("Invalid choice. Try again.")
            
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run()
