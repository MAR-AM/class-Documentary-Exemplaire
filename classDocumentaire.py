class Documentaire ():
    _count = 0
    def __init__(self,titre, date_de_sortie ):
        self._titre = titre
        self._date_de_sortie = date_de_sortie
        Documentaire._count += 1
    
    #getters

    #def getcode(self):
     #   return self._code
    def gettitre(self):
        return self._titre
    def getdate_de_sortie(self):
        return self._date_de_sortie
    
    #Setters

    #def setcode(self, code):
     #   self._code = code
    def settitre(self, titre):
        self._titre = titre
    def setdate_de_sortie(self, date_de_sortie):
        self._date_de_sortie = date_de_sortie
    
    #Methods

    def Tostring (self):
        print("-the title of the documentary = ",self.gettitre() ,"\nrelease date = ",self.getdate_de_sortie() ,
               "\nthe code : ",Documentaire._count)
    
    #def Equals (self,D1):
#
 #       if (self.getcode()==D1.getcode()):
  #          return True
   #     else:
    #        return False
    

class Exemplaire (Documentaire):
    def __init__(self , titre, date_de_sortie, numero, date_de_achat ):
        super().__init__( titre, date_de_sortie)
        self.__numero = numero
        self.__date_de_achat = date_de_achat

    #getters & setters 
    
    def getnumero(self):
        return self.__numero
    def setnumero(self,numero):
        self.__numero = numero
    def getdate_de_achat(self):
        return self.__date_de_achat
    def setdate_de_achat(self,date_de_achat):
        self.__date_de_achat = date_de_achat

    #methods

    def Tostring (self):
        print("-the title of the documentary = ",self.gettitre() ,"\nrelease date= ",self.getdate_de_sortie() , "\nthe code : ",
            Documentaire._count,"\nthe numero = ",self.getnumero(),"\nthe date of purchase = ",self.getdate_de_achat())
    def Equals (self,V3):

        if self.getnumero()==V3.getnumero():
           return True
        else:
            return False

