def shutdown(choice):
    if choice == "yes":
        print("Shutting down...")
    elif choice == "no":
        print("Abort shutdown.")
    else:
        print("Sorry.")

user_input = input("Do you want to shut down? (yes/no): ").lower()
shutdown(user_input)