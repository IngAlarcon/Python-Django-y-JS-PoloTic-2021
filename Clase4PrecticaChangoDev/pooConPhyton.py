"""
Programación Orientada a Objetos
La programación orientada a objetos es un
paradigma de programación , o
una forma de pensar sobre la programación, que se centra en objetos que
pueden almacenar información y realizar acciones.

Objetos
•Una entidad o “cosa” en tu programa, usualmente un sustantivo.
•Un ejemplo de un objeto sería una persona en particular.

Clases
•Las clases se usan para crear objetos
•Podemos crear muchos objetos desde una sola clase
•Las Clases definen el tipo de datos ( type
•El proceso de crear un objeto desde una clase se denomina instanciación .

"""
class Perro:
    # Atributo de clase
    especie = "Canis lupus familiaris"

    def __init__(self, nombre, edad): #__init__ va as er el constructor de mi clase
        self.nombre = nombre #Mi atributo es publico
        self.edad = edad     #Mi atributo es publico
        self._altura = 70    #Con _ estoy haciendo mi atributo privado
        """
        >>> from pooConPhyton import Perro #ejecuto mi archivo donde esta mi clase que cree
        >>> pepe = Perro("Peponacio", 9)   # Creando un objeto con  mi clase perro
        >>> sony = Perro("Sonacio", 2)      
        >>> tomy = Perro("Tomicito", 12)
        >>> pepe.nombre                    #Mostrando datos de mi objeto creado
        'Peponacio'
        >>> sony.edad
        2
        """
    # Metodo de instancia
    def descripcion(self): #
        return (f"{self.nombre} tiene {self.edad} años")

    """
    >>> pepe.descripcion()
    'Peponacio tiene 9 años'   
    """

    # Otro metodo de instancia
    def ladrar(self, sonido):
        return (f"{self.nombre} hace este sonido {sonido}")

    """
    >>> pepe.ladrar("Guauu jejejeje")
    'Peponacio hace este sonido Guauu jejejeje'    
    """
    # metodo de py que me permite describir como esta construida mi clase segun los datos que le pase
    #def __str__(self): lo hace mas descriptivo a mi clase


    def __str__(self):
        return (f"{self.nombre} tiene {self.edad} años, y mide {self._altura}")

    """
    >>> print(tomy) #Automaticamente busca la funcion str donde esta implementada y la ejecuta
    Tomicito tiene 12 años
    >>>  
    """
    #Decoreitor
    ""
    #@property espesifico que no sea publico y defino las configuraciones
    @property #para aceder a una atributo  puede servir para setear o recuperar
    def altura(self):
        return self._altura


######  Herencia (Clases Padre e Hijos) #####

"""
En ocasiones vamos a necesitar generalizar Clases para poder reutilizarlas 
en clases hijas y de esta manera simplificar y ahorrar código.
En el ejemplo anterior de los perros usábamos una clase Perro,
sin embargo pueden haber muchas razas de Perro.
Para que una clase hija herede los atributos y métodos del padre 
simplemente la pasamos como parámetro en la definición de la clase.

"""

class DogoArgentino(Perro): #Hereda la clase Perro que seria del padre
    # Atributo de clase
    raza = "Dogo Argentino"

class BullDogFrances(Perro):
    # Atributo de clase
    raza = "Bulldog Frances"

    """
    >>> from pooConPhyton import DogoArgentino
    >>> tomy = DogoArgentino("Tomicito", 12)
    >>> tomy.raza
    'Dogo Argentino'
    >>> tomy.nombre
    'Tomicito'
    >>> type(tomy)
    <class 'pooConPhyton.DogoArgentino'>        
    """

# pass me sirve para declarar una clase vacia para usarlo en el futuro
# pongo pass para evitar que me de un error
class PerritoPuequines(Perro):
    pass


#Ejecutando Con run

#Precticando con la variable altura decoreitor
perro2 = Perro("loki",21)
print(perro2.altura)
print(perro2)

perro1 = DogoArgentino("Pepe",6)
print(perro1.raza)
print(type(perro1))