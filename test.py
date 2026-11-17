import math

racine_carre = math.sqrt(16)
print("La racine carre de ce nombre est :", racine_carre)

# note_cc = 12
# note_exam = 27.5
# progression = note_exam - note_cc
# print ("Progression du cours :",progression, "point")

note = 12
seuil_validation = 10


if note < seuil_validation :    
    print("Module non valide")
    print("Note actuelle : ", note)
else :
    print("Module valide")
    print("Note actuelle : ", note)
    
