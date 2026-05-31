# 🔐 Password Security Analyzer

A Python-based **Password Security Analyzer and Generator** that evaluates password strength, calculates entropy, provides improvement suggestions, and generates cryptographically secure passwords.  
Designed as a beginner–to–intermediate **cybersecurity / Python project** following ethical security practices.

---

## 📌 Features

- ✅ Password strength analysis (Weak / Medium / Strong)
- 🔢 Entropy calculation (in bits)
- 📝 Actionable feedback for weak passwords
- 🔐 Secure password generator using `secrets`
- 📄 Automatic security report generation
- 📂 Organized project structure

## 🛠️ Technologies Used

- Python 3
- Regular Expressions (`re`)
- Cryptographic module (`secrets`)
- File handling
- CLI-based interaction

## 📁 Project Structure


Password-Security-Analyzer/
│
├── final_project/
│ ├── analyzer.py # Password analysis logic
│ ├── generator.py # Secure password generator
│ ├── main.py # Main CLI application
│ ├── common_passwords.txt # List of common weak passwords
│ └── reports/ # Generated password reports
│
├── .env
├── .gitignore
└── README.md


---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/Password-Security-Analyzer.git
cd Password-Security-Analyzer/final_project
2️⃣ Run the program
python main.py
📋 Usage Options
🔍 Check Password Strength
Analyzes:
Length
Uppercase & lowercase letters
Numbers
Special characters
Displays:
Strength level
Entropy score
Improvement suggestions
Saves a report automatically
🔐 Generate Secure Password
Generates a random, strong password
Uses cryptographically secure randomness
📄 Sample Output
PASSWORD SECURITY ANALYZER
--------------------------
1. Check password
2. Generate secure password
Choose option: 1
Enter password: My1^stproject

Strength: Strong
Entropy: 85.21 bits
Excellent password!
🎯 Learning Outcomes
Understanding password security principles
Entropy-based strength measurement
Secure random generation
Modular Python project design
File handling & reporting
⚠️ Disclaimer

This project is for educational and ethical cybersecurity learning only.
Do not use it for unauthorized access or malicious activities.

📌 Future Improvements
Hash comparison with common password databases
GUI version (Tkinter / Web)
Password breach API integration
Export reports as CSV or PDF

👨‍💻 Author

Ayush I
Cybersecurity & Python Enthusiast
