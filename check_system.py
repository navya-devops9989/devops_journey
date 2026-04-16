import os

# 1. Define what we are looking for
file_name = "goals.txt"

# 2. The Check (The Diagnostic)
if os.path.exists(file_name):
    print("✅ Success! The file is in the lab.")

# 3. The Action (The Healing)
else:
    print("⚠️ Alert! File missing. Re-creating it now...")
    with open(file_name, "w") as f:
        f.write("Target Salary: 10 LPA")
    print("🛠️ System Healed: The file has been restored.")
