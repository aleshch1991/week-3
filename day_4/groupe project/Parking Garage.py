class Parking():
    def __init__(self):
        self.ticketavailable = list(range(1,11))
        self.currentticket = {}
        self.parkingspot = list(range(1,11))
        self.total = 0
    
    def take_ticket(self):
        if self.parkingspot:
            self.space =self.parkingspot.pop()
            self.ticket = self.ticketavailable.pop()
            self.currentticket[self.ticket]= False
            print("Printing your ticket. ")
            print(f"Ticket # {self.ticket}")
            
        else:
            print("No Spaces Available!")
        
    
    def pay_for_parking(self):
        Q2 = int(input("Please Insert Excatly $25 "))
        self.total += Q2
    
        if Q2 >=25:
            print("Procede to exit")
        
        elif Q2 <25:
            print("Add to your balance")
            
    def leave_garage(self):
            print("Thank you for using Cheen To Phate Parking Garage.")

    def showInstructions(self):
        print("""
Welcome to Cheen Tu Phate Parking Garage. 
Please select one of the following options!
[1] Park
[2] Pay
[3] Leave
[4] Quit
""")
    
    def run(self):
        self.showInstructions()
        
        while True:
            choice = input("What would you like to do? ")
            
            if choice == "1":
                self.take_ticket()
                
            elif choice == "2":
                self.pay_for_parking()
            
            elif choice == "3":
                self.leave_garage()
                
            elif choice == "4":
                break
                
            else:
                print("Please see the Cheen Tu Phate Attendant!")
            
car=Parking()
car.run()