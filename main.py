import hashlib

password = input("Veuillez entrez votre mot de passe : ")

if len(password) < 8:
    print ("Le mot de passe doit contenir au moins 8 caractères")

if password.isupper()==True:
    print("Le mot de passe doit contenir au moins une lettre minuscule")

if password.islower()==True:
    print ("Le mot de passe doit contenir au moins une lettre majuscule")

if any(chr.isdigit() for chr in password) == False:
    print("Le mot de passe doit contenir au moins un chiffre")
for s in range(len(password)):
    if password[s] == "&" or password[s] == "!" or password[s] == "@" or password[s] == "#" or password[s]  == "$" or password[s]  == "%" or password[s]  == "*" or password[s]  == "^":
        print ("Mot de passe enregistrée")
        break
    elif password[s] != "&" and password[s] != "!" and password[s] != "@" and password[s] != "#" and password[s] != "$" and password[s] != "%" and password[s] != "*" and password[s] != "^" and s == (len(password)-1):
        print ("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)")
    
hashage = hashlib.sha256()
hashage.update(b)
hashage.digest()
print (hashage)









