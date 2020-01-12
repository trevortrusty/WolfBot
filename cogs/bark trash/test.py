import csv

with open('D:/dev/discordbots/WolfBot/cogs/whitelist.csv', 'r') as f:
            reader = csv.reader(f)
            whitelist = list(reader)[0]

print(whitelist)
whitelist = ["Cos", "Tan"]
print(whitelist)
input()