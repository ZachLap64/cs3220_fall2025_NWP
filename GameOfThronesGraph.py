import Dynasty

class GameOfThronesGraph:
    def __init__(self, corpus):
        #initialisation of dictionary that will store all houses.
        self.houses = {}
        #Load the house corpus
        for data_item in corpus[0:len(corpus)]: #slice the corpus
            d = Dynasty.Dynasty(data_item['name'])
            self.houses.update({data_item['name'] : d})
            for character in data_item['characters']:
                d.append(character)
            #The keys are Houses' (Dynasty) names, the values are Dynasty objects.


    def __iter__(self): # for the case like the following: for house in GameOfThronesHouses:
        self.index = 0
        self.keyList = []
        for keys in self.houses:
            self.keyList.append(keys)
        return self
    
    def __next__(self):
        if self.index >= len(self.houses):
            raise StopIteration
        iKey = self.keyList[self.index]
        self.index += 1
        return self.houses[iKey]
            
    def __contains__(self, h): #Check if h (house's name) is a key in dict houses - the house is in the graph
        if h in self.houses: 
            return True
        else: 
            return False
