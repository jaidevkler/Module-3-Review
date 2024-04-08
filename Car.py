class Car:
    
    def __init__(self, make, model): 
        self.make = make
        self.model = model
        
    def get_make(self): # getter method to get the attribute
        return self.make
    
    def get_model(self): # getter method to get the attribute
        return self.model
    
    def set_make(self, new_make): # setter method
        self.make = new_make 

    def set_model(self, new_model): # setter method
        self.make = new_model