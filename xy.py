class point :
    def __init__(x,abscise =0,ordonne = 0):
          x.abscise = abscise
          x.ordonne = ordonne
    def getAbscise(x):
        return x.abscise
    def setAbscise(x,abscise):
         x.abscise = abscise

    def getardonne(x):
        return x.ordonne

    def setordonne(x,ordonne):
        x.ordonne = ordonne
    def distance(x,point):
        return (((point.ordonne-x.ordonne))**2+(point.abscise-x.abscise)**2)**(1/2)
    def Norme(x):
         return  (((x.ordonne )) ** 2 + (x.abscise) ** 2) ** (1 / 2)







