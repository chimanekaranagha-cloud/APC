s = input("Enter String: ")
count = 0

for i in s:
    count = count + 1

print("Length =", count)


s = input("Enter String: ")

v = c = d = sp = sc = 0

for ch in s:
    if ch in "aeiouAEIOU":
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    elif ch == " ":
        sp += 1
    else:
        sc += 1

print("Vowels =", v)
print("Consonants =", c)
print("Digits =", d)
print("Spaces =", sp)
print("Special Characters =", sc)


s = input("Enter String: ")

rev = ""

for i in s:
    rev = i + rev

print(rev)

s = input("Enter String: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



s = input("Enter String: ")

u = l = 0

for ch in s:
    if ch.isupper():
        u += 1
    elif ch.islower():
        l += 1

print("Uppercase =", u)
print("Lowercase =", l)


s = input("Enter String: ")
a = input("Old Character: ")
b = input("New Character: ")

print(s.replace(a, b))


s = input("Enter String: ")

print(s.replace(" ", ""))


s = input("Enter String: ")
ch = input("Enter Character: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print(count)



s = input("Enter String: ")

print("First =", s[0])
print("Last =", s[-1])



s = input("Enter String: ")

for i in s:
    print(i, ord(i))


s = input("Enter Sentence: ")

words = s.split()

print("Words =", len(words))



s = input("Enter Sentence: ")

words = s.split()

long = words[0]

for i in words:
    if len(i) > len(long):
        long = i

print(long)


s = input("Enter Sentence: ")

words = s.split()

short = words[0]

for i in words:
    if len(i) < len(short):
        short = i

print(short)


s = input("Enter Sentence: ")

print(s.title())



s = input("Enter String: ")

for i in s:
    if s.count(i) > 1:
        print(i)



s = input("Enter String: ")

for i in set(s):
    print(i, "=", s.count(i))




s1 = input("First String: ")
s2 = input("Second String: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")


s = input("Enter String: ")

result = ""

for i in s:
    if i not in result:
        result += i

print(result)


s = input("Enter Main String: ")
sub = input("Enter Substring: ")

if sub in s:
    print("Found")
else:
    print("Not Found")


s = input("Enter Sentence: ")
word = input("Enter Word: ")

print(s.split().count(word))


p = input("Enter Password: ")

if len(p) >= 8:
    print("Valid")
else:
    print("Invalid")


s = input("Enter String: ")

count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        print(s[i], count, end="")
        count = 1

print(s[-1], count, sep="")



s = input("Enter String: ")

result = ""

count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)



s = input("Enter String: ")

ch = max(set(s), key=s.count)

print(ch)


s = input("Enter String: ")

freq = {}

for i in s:
    freq[i] = freq.get(i, 0) + 1

print(sorted(freq.items(), key=lambda x: x[1], reverse=True)[1][0])


text = input("Enter Text: ")

for i in text:
    print(chr(ord(i)+3), end="")


email = input("Enter Email: ")

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")




sentence = input("Enter a sentence: ")
words = sentence.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

print("Word Frequency:")

for word in freq:
    print(word, "=", freq[word])




s = input("Enter Sentence: ")

print(" ".join(s.split()[::-1]))


s1 = input("First String: ")
s2 = input("Second String: ")

if s2 in s1+s1:
    print("Yes")
else:
    print("No")

