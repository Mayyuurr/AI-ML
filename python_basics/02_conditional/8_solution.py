password=input("password:-")

pass_len=len(password)

print(pass_len)

if pass_len<6:
    strength="Weak"
elif pass_len<=10:
    strength="Medium"
else:
    strength="Strong"

print(strength)