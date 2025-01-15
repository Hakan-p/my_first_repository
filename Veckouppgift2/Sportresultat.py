print("Matchen är över, nu ska vi räkna ut resultatet! ")
goal_liverpool = int(input("Hur många mål gjorde Liverpool?:"))
goal_tottenham = int(input("Hur många mål gjorde Tottenham?:"))
if goal_tottenham > goal_liverpool:
    print("Tottenham vann!")
elif goal_tottenham < goal_liverpool:
    print("Liverpool vann!")
else:
    print("Matchen blev oavgjord")

# Testvärden :2 Liverpool 1 Tottenhamn
# Testvärden :1 Liverpool 2 Tottenhamn
# Testvärden :0 Liverpool 0 Tottenhamn  