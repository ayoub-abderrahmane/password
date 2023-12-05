from hashlib import sha256   # import getpass (pour masquer le mot de passe sur l'écran)
import secrets
import json
while True:
  password = str(input("Veuillez entrez votre mot de passe : "))

  # Définition des conditions pour créer :  

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
       print ("Votre mot de passe a bien été pris en compte")
       break
    elif password[s] != "&" and password[s] != "!" and password[s] != "@" and password[s] != "#" and password[s] != "$" and password[s] != "%" and password[s] != "*" and password[s] != "^" and s == (len(password)-1):
        print ("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)")

  #Création d'un sel pour mieux sécuriser le mot de passe
  salt = secrets.token_hex(24).encode()
  salt = b'13mhasnkfmahxh9a47tpn032gpt'

  # Hashage du mot de passe saisi par l'utilisateur   
  password = password.encode()
  password_hash = sha256(salt + password).hexdigest()


  # Ecriture du mot de passe hashé et salé dans un fichier

  fichier = open('fichier.txt','a')

  fichier.write(password_hash)
  
  to_continue= input ("Souhaitez-vous ajouter de nouveaux mots de passe ? (oui/non) : ")
 
  if to_continue == "non" or to_continue == "Non" or to_continue == "NON":
     break