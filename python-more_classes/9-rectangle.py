#!/usr/bin/python3

"""
AJUSTER Module 8-rectangle.py

Ce module définit une classe Rectangle avec :
- deux attributs privés : __width et __height
- des getters et setters avec vérification de type/valeurs
- un constructeur avec arguments optionnels
- une méthode area() qui retourne l’aire
- une méthode perimeter() qui retourne le périmètre
  (0 si width ou height est nul)
- la méthode __str__ qui retourne une représentation textuelle du rectangle
  avec des '#'
- la méthode __repr__ qui retourne une chaîne permettant de recréer
  un objet identique avec eval()
- la méthode __del__ qui affiche "Bye rectangle..."
lors de la suppression de l’instance
- un attribut de classe number_of_instances qui compte les objets
Rectangle vivants
- un attribut print_symbol utilisé pour représenter graphiquement le rectangle
- une méthode statique bigger_or_equal() pour comparer deux rectangles
selon leur aire
- une méthode de classe square() qui retourne un rectangle de largeur et
  hauteur égales (carré)
- une méthode de classe square() qui retourne un rectangle avec width == height
"""


class Rectangle:
    """
    Classe Rectangle qui définit un rectangle avec :
    - des attributs privés pour la largeur et la hauteur
    - des accesseurs avec vérification de type et de valeur
    - un compteur d'instances (number_of_instances) qui suit le nombre
    d'objets créés
    - un attribut de classe print_symbol utilisé pour personnaliser
    l'affichage du rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise un nouveau rectangle.
        Args:
        ° width (int): largeur du rectangle (par défaut 0)
        ° height (int): hauteur du rectangle (par défaut 0)
        Raises:
        ° TypeError: si width ou height ne sont pas des entiers
        ° ValueError: si width ou height sont négatifs
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter de la largeur du rectangle.
        Retourne la valeur de l'attribut privé __width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter de la largeur avec vérifications :
        - doit être un entier
        - doit être >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter de la hauteur du rectangle
        Retourne la valeur de l'attribut privée __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter de la hauteur avec 2 vérifications :
        ° être un entier
        ° être sup ou égale à 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Permet de calculer l'aire du rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Permet de calculer le périmètre du rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """
        Retourne une représentation textuelle du rectangle avec des '#'
        Chaque ligne correspond à la hauteur du rectangle,
        et chaque ligne contient 'width' caractères '#'.
        Si width ou height est nul, retourne une chaîne vide.
        """
        if (self.__width) == 0 or (self.__height) == 0:
            return ("")
        else:
            return ("\n".join([str(self.print_symbol) * self.__width]
                              * self.__height))

    def __repr__(self):
        """
        Retourne une chaîne de texte représentant le rectangle
        sous la forme : Rectangle(width, height)
        Cette chaîne doit permettre de recréer un objet identique
        via la fonction eval().
        """
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """
        Permet d'afficher un message quand l'instance est supprimé
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare deux rectangles et retourne celui qui a la plus grande aire.
        Si les deux ont la même aire, retourne rect_1.
        Args: rect_1 (Rectangle): premier rectangle à comparer
        rect_2 (Rectangle): second rectangle à comparer
        Raises:TypeError: si rect_1 ou rect_2 ne sont pas des
        instances de Rectangle
        Returns:
        Rectangle: le rectangle ayant la plus grande aire ou rect_1
        en cas d’égalité
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        Crée un nouveau rectangle ayant la même largeur et hauteur.
        Cette méthode permet de créer un carré à partir d'une seule valeur.
        Args: size (int): la taille du côté du carré (valeur par défaut : 0)
        Returns: Rectangle: une nouvelle instance de Rectangle avec largeur
        et hauteur égales à size
        """
        return (cls(size, size))
