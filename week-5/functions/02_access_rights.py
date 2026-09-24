def access_rights(user_role):
    role = user_role.lower()
    if role == "admin":
        return "full"
    elif role == "user":
        return "limited"
    elif role == "guest":
        return "view"
    else:
        return "unknown"


user_role = input("Enter the user role (admin, user, guest): ")
print(access_rights(user_role))
