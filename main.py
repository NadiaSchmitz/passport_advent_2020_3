#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID)

batch = []
passports = []
symbol_check = 0
valid_passports = 0
data = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
check = 0

with open("batch.txt", "r") as file1:
    for line in file1:
        batch.append(line)
    print(batch)

for item in batch:
    if item.find('§') > 0:
        symbol_check = 1
if symbol_check == 1:
    print("Symbol wurde gefunden. Man braucht einen neuen Delimiter.")
else:
    print("Symbol wurde nicht gefunden.")

string = "".join(batch)
string = string.replace("\n\n", "§ ")
string = string.replace("\n", " ")
passports = string.split('§')

for i in range(0, len(passports)):
    for j in range(0, 7):
        print(passports[i], data[j])
        if data[j] in passports[i]:
            check = check + 1
            print(check)
    if check == 7:
        print("Passport ist valid", passports[i], i)
        valid_passports = valid_passports + 1
        check = 0
    else:
        print("Passport ist invalid", passports[i], i)
        check = 0

print(valid_passports)
