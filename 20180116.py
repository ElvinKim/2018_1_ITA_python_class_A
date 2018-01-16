import re

pattern_obj = re.compile("[a-z]+")

# match example
m = pattern_obj.match("abc")
print(m)

m = pattern_obj.match("65abc")
print(m)  # None

print("-" * 30)
# search example
m = pattern_obj.search("abc")
print(m)

m = pattern_obj.search("65abc")
print(m)

print("-" * 30)
# findall example
results = pattern_obj.findall("python is good")
print(results)

print("-" * 30)
# finditer example
match_iter = pattern_obj.finditer("python is good")

for m in match_iter:
    print(m)

print("-" * 30)
# Match Object example
m = pattern_obj.search("abc")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

print("-" * 30)



print("-" * 30)
m = pattern_obj.search("65abc")
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())
print("65abc"[m.start(): m.end()])

print("-" * 30)
pattern_obj = re.compile("abc.abc")
m = pattern_obj.match("abc\nabc")
print(m)  # None

pattern_obj = re.compile("abc.abc", re.DOTALL)
m = pattern_obj.match("abc\nabc")
print(m)

# Greedy vs Non-Greedy
html = """
<div>
<span>aaa</span>
<div>TEST</div>
</div>
"""
pattern = re.compile("<.*>", re.DOTALL)
print(pattern.findall(html))
pattern = re.compile("<(.*?)>", re.DOTALL)
print(pattern.findall(html))
print("\n")


email_pattern_obj = re.compile("[^@]+@[^@]+\.[^@]+")

m = email_pattern_obj.search("sangmook.kim@kaist.ac.kr")
print(m)







