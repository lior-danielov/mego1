import random
password = []
letters = ['a','b','c']



password.append(random.choice(letters))
password.append(random.choice(letters))
password.append(random.choice(letters))
password.append(random.choice(letters))
password.append(random.choice(letters))
print(f"before\n(password)") # placholder or interpolatoion

random.shuffle(password)
print(f"\n\nAfter\n{password}")