#! python3
# city_simulator.py

#The aim of this program is to simulate the movement of the inhabitants of a theoratical city based on a few assumptions of their behaviour.

import random

class House():
    '''Represents a house in the city.
    Each house is uniquely defined by its row and column position indicators.
    Initiaslly each house's resident is set to None. This can be changed with move resident method.'''
    def __init__(self, row, column, city):
        self.row = row
        self.column = column
        self.city = city
        self.empty = True
        self.resident = None

    def __str__(self):
        if not self.empty:
            return self.resident.side
        else:
            return 'EMPTY'

    def move_resident(self, resident):
    #Moves the resident from their current house to the house on which this method is called.
        if self.empty:
            self.resident = resident
            self.resident.house = self
            self.empty = False
            self.city.empty_houses.remove(self)

    def neighbours(self):
    #Returns a tuple of neighbours with resident objects.
        if self.row > 0 and self.column > 0 and self.row < 9 and self.column < 9:
            houses = self.city.houses
            nei = list()
            for i in (1,-1, 0):
                for j in (1, -1, 0):
                    nei_house = houses[(self.row +i , self.column +j)] 
                    if not nei_house.empty:
                        nei.append(nei_house.resident)
            nei.remove(self.resident)
            return tuple(nei)



class Resident():
    '''Represents a resident in the city.
    Each resident can belong to either Red or Blue group.
    Each resident has the following attributes:
    house -> The house in which they currently reside in.
    side -> Can be Red or Blue.
    '''
    def __init__(self, house, side):
        self.house = house
        self.side = side
        self.house.resident = self
        self.house.empty = False
        self.house.city.empty_houses.remove(house)

    def move_to_house(self, house):
    #Moves the resident to the given house.
        self.house.city.empty_houses.remove(house)
        self.house.city.empty_houses.append(self.house)
        self.house.empty = True
        self.house.resident = None
        self.house =  house
        self.house.resident = self
        

    def happiness(self):
        neighbours = self.house.neighbours()
        hap = 0
        if not neighbours== None:
            for nei in neighbours:
                if nei.side == self.side:
                    hap += 1
                else:
                    hap -= 1
            
        return hap
    

class City():
    '''Represent a city with 100 houses and 80 resident with 40 Red side and 40 Blue side.'''
    def __init__(self):
        self.empty_houses = list()
        self.houses = dict()
        for row in range(10):
            for column in range(10):
                self.houses[(row, column)] = House(row, column, self)
                self.empty_houses.append(self.houses[(row, column)])

        self.residents = list()
        for i in range(10):
            for j in range(8):
                if j % 2 == 0:
                    side = 'RED'
                else:
                    side = 'BLUE'
                house = self.houses[(i, j)]
                res = Resident(house, side)
                self.residents.append(res)
                

    def print_city(self):
                               houses = self.houses
                               for i in range(10):
                                   for j in range(10):
                                       print(str(houses[(i, j)]).ljust(10), end = ' ')
                                   print()
                                
    def migrate(self):
        for house in self.houses.values():
            if not house.empty:
                if house.resident.happiness() < 0:
                    new_house = random.choice(self.empty_houses)
                    print(new_house.row, new_house.column)
                    house.resident.move_to_house(new_house)
                    
                
                                       
                                    
 

        
