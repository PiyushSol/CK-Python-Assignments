# import re

# def validate_ip_regex(ip):
#     pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
    
#     if re.match(pattern, ip):
#         print("Valid IPv4 Address")
#     else:
#         print("Invalid IPv4 Address")


# ip = input("Enter IP Address: ")
# validate_ip_regex(ip)

# def validate_ip_no_regex(ip):
    
#     parts = ip.split(".")
    
#     if len(parts) != 4:
#         print("Invalid IP: Should contain exactly 4 parts")
#         return
    
#     for part in parts:
        
#         if not part.isdigit():
#             print("Invalid IP: Contains non-numeric value")
#             return
        
#         num = int(part)
        
#         if num < 0 or num > 255:
#             print("Invalid IP: Number must be between 0 and 255")
#             return
    
#     print("Valid IPv4 Address")


# ip = input("Enter IP Address: ")
# validate_ip_no_regex(ip)


# def validate_email_regex(email):
    
#     pattern = r'^[a-z0-9._-]+@gmail\.com$'
    
#     if re.match(pattern, email):
#         print("Valid Gmail Address")
#     else:
#         print("Invalid Gmail Address")


# email = input("Enter Email: ")
# validate_email_regex(email)


def validate_email_no_regex(email):
    
    if "@gmail.com" not in email:
        print("Invalid Email: Must contain @gmail.com")
        return
    
    username, domain = email.split("@")
    
    if domain != "gmail.com":
        print("Invalid Email: Domain must be gmail.com")
        return
    
    allowed = "abcdefghijklmnopqrstuvwxyz0123456789._-"
    
    for ch in username:
        if ch not in allowed:
            print("Invalid Email: Username contains invalid characters")
            return
    
    print("Valid Gmail Address")


email = input("Enter Email: ")
validate_email_no_regex(email)