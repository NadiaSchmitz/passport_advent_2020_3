batch = open('batch.txt', 'r')
passport = []

lines = batch.readlines()

# итерация по строкам
for line in lines:
    passport.append(line.strip())

# закрываем файл
batch.close


print(len(passport))
