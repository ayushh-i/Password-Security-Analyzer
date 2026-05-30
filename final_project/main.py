from analyzer import analyze_password
from generator import generate_password
from datetime import datetime
import os

print("PASSWORD SECURITY ANALYZER")
print("--------------------------")

choice = input("1. Check password\n2. Generate secure password\nChoose option: ")

if choice == "1":
    password = input("Enter password: ")

    strength, entropy, feedback = analyze_password(password)

    print("\nStrength:", strength)
    print("Entropy:", entropy, "bits")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)
    else:
        print("Excellent password!")

    # ---------- REPORT SAVING ----------
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"report_{timestamp}.txt"
    report_path = os.path.join("reports", report_name)

    with open(report_path, "w") as file:
        file.write("PASSWORD SECURITY REPORT\n")
        file.write("------------------------\n")
        file.write(f"Strength : {strength}\n")
        file.write(f"Entropy  : {entropy} bits\n")

        if feedback:
            file.write("Issues Found:\n")
            for item in feedback:
                file.write(f"- {item}\n")
        else:
            file.write("Issues Found: None\n")

    print(f"\nReport saved successfully in reports/{report_name}")

elif choice == "2":
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))

else:
    print("Invalid choice")