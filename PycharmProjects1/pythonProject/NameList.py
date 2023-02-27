NamesList = ["Aaron Bentley", "Jordan Brookes", "James Chandler", "Leigh Evans", "Kelly Gresham", "Jordan Jemirifo",
             "Mark Kemsley", "Ryan Lombardi", "Sarah Steer", "Rob Totton"]
LongestName = ""

for data in NamesList:
    if len(data) > len(LongestName):
        LongestName = data

print("The Longest Name Is:", LongestName)
