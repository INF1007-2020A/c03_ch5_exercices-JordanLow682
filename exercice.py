#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    nom_nombre = float(input("Veuillez entrer un nombre: "))
    if mon_nombre < 0:
        mon_nombre *= -1
    return mon_nombre


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    index = 0
    resultat = []
    nom = ""
    
    for index in prefixes:
        nom = print(prefixes[index] + suffixes)
        resultat.append[nom]
    return resultat


def prime_integer_summation() -> int:
    sum = 0
    number = 0
    while(number < 100):
        sum += number
        number += 1
    return sum


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
