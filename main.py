"""
Ce module contient une fonction pour vérifier si un nombre est premier.
La fonction `isprime` détermine si un nombre donné est un nombre premier.
Elle utilise des optimisations pour réduire le nombre de vérifications nécessaires.
"""

def isprime(p):
    """
    Fonction qui permet de vérifier si p est un nombre premier.

    :param p: Nombre entier à tester.
    :return: True si p est premier, False sinon.
    """
    if p < 2:
        return False
    for i in range(2, int(p**0.5) + 1):  # Vérifier jusqu'à la racine carrée de p
        if p % i == 0:
            return False
    return True

def main():
    """
    Fonction principale qui vérifie si la fonction précédente est efficace.
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()  # Pour ajouter une nouvelle ligne après la liste des nombres premiers

if __name__ == "__main__":
    main()
