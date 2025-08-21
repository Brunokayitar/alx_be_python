# daily_reminder.py

# --- Inputs ---
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Simple input validation loops
while priority not in ["high", "medium", "low"]:
    priority = input("Priority (high/medium/low): ").strip().lower()

while time_bound not in ["yes", "no"]:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# --- Match/Case reaction based on priority ---
match priority:
    case "high":
        base = f"'{task}' is a high priority task"
    case "medium":
        base = f"'{task}' is a medium priority task"
    case "low":
        base = f"'{task}' is a low priority task"
    case _:
        base = f"'{task}' has an unknown priority"

# --- Time sensitivity modifies the reminder ---
if time_bound == "yes":
    print(f"Reminder: {base} that requires immediate attention today!")
else:
    print(f"Note: {base}. Consider completing it when you have free time.")
