import random as rd

fichier_reponse = "Haschcode 2019/qualification_round_2019.in/projet_reponse.txt"
fichier_1 = "Haschcode 2019/qualification_round_2019.in/a_example.txt"
fichier_2 = "Haschcode 2019/qualification_round_2019.in/b_lovely_landscapes.txt"
fichier_3 = "Haschcode 2019/qualification_round_2019.in/c_memorable_moments.txt"
fichier_4 = "Haschcode 2019/qualification_round_2019.in/d_pet_pictures.txt"
fichier_5 = "Haschcode 2019/qualification_round_2019.in/e_shiny_selfies.txt"

liste_fichier = [fichier_1, fichier_2, fichier_3, fichier_4, fichier_5]
p = int(100)

def lecture(fichier):
    """
    Lecture du fichier avec les images

    :param fichier: fichier à lire
    :type: str
    :return: liste des images
    :rtype: list(set)
    """
    global image, n
    image = list()
    n = int()
    f = open(fichier, encoding='utf8')
    n = int(f.readline())
    print("Nombre de ligne lu :", n)
    progression(0, prefix= "Lecture des données\t")
    for i in range (1,n+1):
        q = (i / n * 100)
        ligne = f.readline().strip()
        ligne = ligne.split()
        a = str((i-1)) + "N"
        ligne.append(a)
        image.append(set(ligne))
        progression(q, prefix= "Lecture des données\t")
    f.close()
    print()
    return

def comparaison(tag):
    """
    Recherche l'image avec le plus de points communs
    
    :param tag: tags à rechercher
    :type: list
    :return: l'image avec le plus de points communs
    :rtype: set

    ..note: Si on ne trouve pas de points commun, une image est choisie au hasard 
    """
    score_max = int()
    score_a = int()
    set_tag = set(tag)
    for set_image in image:
        score_a = score(image_ancienne, set_image)
        if score_a > score_max:
            score_max = score_a
            image_suivante = set_image
    if score_max == 0:
        image_suivante = rd.choice(image)
    image.remove(image_suivante)
    return image_suivante

def image_verticale(tag):
    """
    Recherche une autre image verticale avec le plus de points communs

    :param tag: tag à rechercher dans les images
    :type: list
    :return: appel la fonction info(image_suivante)

    ..note: image_suivante est choisi pour la suite car à le plus de points communs
            Si on ne trouve pas de points commun, une image est choisie au hasard

    """
    score_max = int()
    set_tag = set(tag)
    for set_image in image:
        if "V" in set_image:
            score_a = score(image_ancienne, set_image)
            if score_a > score_max:
                score_max = score_a
                image_suivante = set_image
    if score_max == 0:
        image_suivante = rd.choice(image)
        while "V" not in image_suivante:
            image_suivante = rd.choice(image)
    image.remove(image_suivante)
    image_suivante.remove("V")
    return suivante(image_suivante)

def info(image_lu):
    """
    Extrait toutes les informations utiles des images

    :param image_lu: l'image dont on veut les informations
    :type: set
    :return: le numéro de ligne, les tags, son oriention
    :rtype: list, list, str
    """
    liste_tags = list()
    orientation = str()
    num_ligne = list()
    liste_info = list(image_lu)
    for element in liste_info:
        if "N" in element:
            element = element.replace("N","")
            num_ligne.append(element)
        elif len(element) > 2:
            liste_tags.append(element)
        elif element == "H" or element == "V":
            orientation = element 
    return num_ligne, liste_tags, orientation

def suivante(image_lu):
    """
    Vérifie si l'image est verticale, et en recherche une autre avec points communs

    :param image_lu: l'image à traiter
    :type: set
    :return: son numéro de ligne, ses tags
    :rtype: list, list

    ..note: utilise la fonction info(image_lu) et image_verticale(liste_tags)
    """
    num_ligne, liste_tags, orientation = info(image_lu)
    if orientation == "V":
        num_ligne_v, liste_tags_v = image_verticale(liste_tags)
        num_ligne.append(num_ligne_v[0])
        for tag in liste_tags_v:
            if tag not in liste_tags:
                liste_tags.append(tag)
    return num_ligne, liste_tags

def score(image_ancienne, image_suivante):
    """
    Donne le nombre de points que rapporte les images

    :param image_ancienne/image_suivante: images à comptabilisées
    :type: set, set
    :return: le nombre de points
    :rtype: int
    """
    points = int()
    diff1 = image_ancienne.difference(image_suivante)
    diff2 = image_suivante.difference(image_ancienne)
    communs = image_ancienne.intersection(image_suivante)
    points += min(len(diff1), len(diff2), len(communs))
    return points

def reponse_ecriture(reponse):
    """
    Ecrit dans le fichier réponce

    :param: liste avec tout les numéros de lignes
    :type: list
    :return: nombre de slides
    :rtype: int

    :Example:
    748
    73 
    114 12
    """
    i = 1
    progression(0, prefix="Ecriture des données\t")
    fichier = open(fichier_reponse, 'w', encoding="UTF8")
    fichier.write(str(len(reponse))+ "\n")
    for element in reponse:
        reponse_str = str()
        q = (i / len(reponse) * 100)
        for ligne in element:
            reponse_str += ligne + " "
        fichier.write(str(reponse_str)+ "\n")
        progression(q, prefix="Ecriture des données\t")
        i += 1
    print()
    fichier.close()
    return len(reponse)

def progression (iteration, total=100, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Appel en boucle pour créer une barre de progression du terminal

    :param iteration: itération actuelle 
    :type: int
    :param total: total des itérations
    :param prefix: chaîne de préfixe
    :type: str
    :param prefix: chaîne de suffix
    :type: str
    :param decimals: nombre positif de décimales en pourcentage d'achèvement (Int)
    :type: int
    :param length: longueur de caractères de la barre
    :type: int
    :param fill: caractère de remplissage de la barre
    :type: str
    :param printEnd: caractère de fin
    :type: str
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration >= total: 
        print()

def image_init(fichier_lecure):
    """
    Premet de lancer l'emsemble des fonctions pour le HASCODE 2019

    :param fichier_lecure: le fichier à lire
    :type: str
    :return: le score effectué
    :rtype: int

    ..note: utilise les fonctions: info(), comparaison(), suivante(), score(), reponse_ecriture() 
    """
    global image_ancienne
    liste_reponse = list()
    points = int()
    itteration = int()
    image_suivante = set()
    image_ancienne = set()
    lecture(fichier_lecure)
    p = int()
    progression(0, prefix="Chargement des données\t")
    nombre = len(image)
    tag = str(rd.randint(0, nombre))
    tag = "N" + tag
    while len(image) > 0:
        reponse_str = str()
        image_suivante = comparaison(tag)
        reponse, tag = suivante(image_suivante)
        points += score(image_ancienne, set(tag))
        image_ancienne = set(tag)
        liste_reponse.append(reponse)
        q = ((n - len(image)))
        progression(iteration = q, total = n,prefix="Chargement des données\t")
    print()
    slides = reponse_ecriture(liste_reponse)
    print("Nombre de slides:", slides,"\nScore:", points)
    print(135 * "#", "\n")
    return points



if __name__ == "__main__":
    points_total = int()
    for fichier in liste_fichier:
        print(fichier)
        points_total += image_init(fichier)
    print(135 * "-","\n")
    print("Score total:", points_total,'\n')