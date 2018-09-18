age = int(input("What is your age:"))
if age > 62:
    print("You can get social security benefits")
else:
    print("wow jij bent jong!")
report = input("Report:")
if "large bonuses" in report:
    print("vacation time")
Hits = int(input("Hits:"))
Shield = (10 - Hits)
if Shield <= 0:
    print("You're dead...")
else:
    Shield = str(Shield)
    print("You have " + Shield + " Shield Points left")





