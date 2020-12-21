import string, random

def password(n):
	s=list(string.printable[:92])
	check=False
	while check==False:
		pas= []
		pas.extend(random.sample(s, plen))
		check = any(item in list(string.ascii_lowercase) for item in pas) & any(item in list(string.ascii_uppercase) for item in pas) & any(item in list(string.digits) for item in pas) & any(item in list(string.punctuation) for item in pas)
	print("".join(pas))

plen=int(input("Enter the length of the password"))
password(plen)