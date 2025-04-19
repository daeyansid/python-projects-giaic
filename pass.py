import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Common password check
    common_passwords = ["password", "123456", "qwerty", "admin", "welcome", "password123", "abc123", "hello", "monkey", "1234567890", "12345678"]
    if password.lower() in common_passwords:
        feedback.append("❌ This is a commonly used password and can be easily guessed.")
        score = max(0, score - 1)  # Penalize common passwords
    
    # Print all feedback messages
    for message in feedback:
        print(message)
    
    # Strength Rating
    if score >= 4:
        print("✅ Strong Password!")
    elif score == 3:
        print("⚠️ Moderate Password - Consider adding more security features.")
    else:
        print("❌ Weak Password - Improve it using the suggestions above.")
    
    return score

def generate_strong_password(length=12):
    """Generate a strong random password"""
    if length < 8:
        length = 12  # Minimum safe length
    
    # Ensure we have all required character types
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*")
    
    # Fill the rest with random characters
    remaining_length = length - 4
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    rest = ''.join(random.choice(all_chars) for _ in range(remaining_length))
    
    # Combine all parts and shuffle
    all_parts = lowercase + uppercase + digit + special + rest
    password_list = list(all_parts)
    random.shuffle(password_list)
    return ''.join(password_list)

def main():
    print("\n" + "="*50)
    print("🔐 PASSWORD STRENGTH METER 🔐")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("1. Check password strength")
        print("2. Generate a strong password")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            password = input("\nEnter your password: ")
            score = check_password_strength(password)
        elif choice == '2':
            try:
                length = int(input("\nEnter desired password length (min 8): "))
                if length < 8:
                    print("Password length must be at least 8. Using default length of 12.")
                    length = 12
            except ValueError:
                print("Invalid input. Using default length of 12.")
                length = 12
            
            strong_password = generate_strong_password(length)
            print(f"\n✅ Generated Strong Password: {strong_password}")
            print("(We recommend saving this in a secure password manager)")
        elif choice == '3':
            print("\nThank you for using Password Strength Meter! Stay secure. 🔒")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()