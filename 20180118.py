f = open("sample.txt", "w", encoding="utf-8")
f.write("가자가자!!!!")

f.close()

f = open("sample2.txt", "w", encoding="utf-8")

for i in range(10):
    f.write(str(i + 1) + "\n")
f.close()

f = open("sample2.txt", "r", encoding="utf-8")
# print(f.read())
print(f.readline())
print(f.readline())
print("-" * 30)

for line in f.readlines():
    print(line)

print("-" * 30)

f.close()

f = open("sample2.txt", "r", encoding="utf-8")

for line in f.readlines():
    print(line)
f.close()

# mode 'a'
f = open("sample2.txt", "a", encoding="utf-8")
f.write("test")
f.close()

# with
with open("sample3.txt", "w", encoding="utf-8") as f:
    f.write("가자가자!!!!")


# 실습

f = open("multiplication_table.txt", "w", encoding="utf-8")

for i in range(2, 10):
    for j in range(1, 10):
        f.write("{} * {} = {}".format(i, j, i*j) + "\n")

f.close()

with open("multiplication_table.txt", "a", encoding="utf-8") as f:
    for i in range(10, 20):
        for j in range(1, 10):
            f.write("{} * {} = {}".format(i, j, i*j) + "\n")

f_read = open("multiplication_table.txt", "r", encoding="utf-8")
f_write = open("copy_mul.txt", 'w', encoding="utf-8")

for line in f_read.readlines():
    f_write.write(line)

f_read.close()
f_write.close()
