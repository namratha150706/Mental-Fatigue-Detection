
import time

print("=" * 45)
print("       MENTAL FATIGUE DETECTION SYSTEM")
print("=" * 45)

name = input("Enter your name: ")

while True:
    sleep = float(input("Hours of sleep (0-24): "))
    if 0 <= sleep <= 24:
        break
    print("Invalid input! Enter between 0 and 24.")

while True:
    study = float(input("Hours spent studying (0-24): "))
    if 0 <= study <= 24:
        break
    print("Invalid input! Enter between 0 and 24.")

while True:
    stress = int(input("Stress level (1-10): "))
    if 1 <= stress <= 10:
        break
    print("Enter a value between 1 and 10.")

while True:
    focus = int(input("Concentration level (1-10): "))
    if 1 <= focus <= 10:
        break
    print("Enter a value between 1 and 10.")

score = 0

if sleep < 6:
    score += 2

if study > 6:
    score += 2

if stress >= 7:
    score += 2

if focus <= 4:
    score += 2

print("\nAnalyzing...")
time.sleep(2)

print("\n========== REPORT ==========")
print("Name:", name)
print("Fatigue Score:", score, "/ 8")

if score <= 2:
    print("Status: LOW FATIGUE")
    print("Recommendation: Maintain your routine.")
elif score <= 5:
    print("Status: MODERATE FATIGUE")
    print("Recommendation: Take regular breaks.")
else:
    print("Status: HIGH FATIGUE")
    print("Recommendation: Take sufficient rest.")

print("============================")
print("Educational prototype only.")
