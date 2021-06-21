f = open("D:\\myfiles\welcome.txt", "r")
#f = open("demofile.txt", "r")
print(f.read())

# Return the 5 first characters of the file:
print(f.read(5))

# Read one line of the file

print(f.readline())

for x in f:
  print(x)

f.close()

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

import os
os.rmdir("myfolder")


# reading from csv files
with open("test.csv", mode="r") as f:
  reader = csv.reader(f, delimiter=",")
  for row in reader:
    print(row)