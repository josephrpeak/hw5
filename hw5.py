# Joe Peak
# Program 5
# 11/20/2022
# CS 101

class House():
    def __init__(self, year = 0, principal = 0, location = "none", current_value = 0, age = 0):
        self.year = year
        self.principal = principal
        self.location = location
        self.current_value = current_value
        self.age = age
        
    def currentValue(self):
        self.current_value = self.principal * (1 + 0.08) ** self.age

        return self.current_value

    def moneyEarned(self):
        return self.current_value - self.principal
        
    def __str__(self):
        self.current_value = self.currentValue()
        return f"--------------------\nHouse Information:\n Year Built: {self.year}\n Purchase Price: {self.principal}\n Current Value of House: {round(self.current_value, 2)}\n Location: {self.location}\n--------------------"
        
            
def main():
    states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

    retry = True
    
    while(retry == True):
        print("Welcome to our house calculation app.")

        while(True):
            try:
                model_year = int(input("Enter house model year: "))
                if(model_year < 0 or model_year > 2022):
                    raise ValueError
                else:
                    break
                
            except ValueError:
                print("Please enter a valid year.")

        
        while(True):
            try:
                house_price = int(input("Price of the house: "))
                if(house_price < 1):
                    raise ValueError
                else:
                    break
                
            except ValueError:
                print("Please enter a valid price.")

        while(True):
            try:
                current_year = int(input("Current year: "))
                if(current_year < model_year or current_year > 2022):
                    raise ValueError
                else:
                    break
                
            except ValueError:
                print("Please enter the correct current year")

        while(True):
            try:
                house_location = input("Enter your house location: ")
                if(house_location.upper() not in states):
                    raise ValueError
                else:
                    break
                
            except ValueError:
                print("Please enter a valid location.")
        
        house = House(model_year, house_price, house_location.upper(), 0, current_year - model_year)
        house.current_value = house.currentValue()
        
        print(house)
        print(f"--------------------\nTotal value you will earn : \n{round(house.moneyEarned(), 2)}\n--------------------")
        
        while(True):
            try:
                retry = input("Would you like to check the price of another house? (Y/N)")
                if(retry.upper() != 'Y' and retry.upper() != 'N'):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Please enter Y or N.")
        
        if(retry.upper() == 'N'):
            retry = False
        else:
            retry = True
            
if __name__ == "__main__":
    main()






    
