from datetime import datetime

class Attendancesystem:
    
    def __init__(self): 
        
        self.attendace_list = {}
        
    def mark_attendace(self,name):
            
        date = datetime.now().strftime("%Y-%m-%d")
        
        if name in self.attendace_list:
            
            if date in self.attendace_list[name]: 
                print(f"{name} is already marked present for today.")
            
            else: 
                
                self.attendace_list[name].append(date)    
                
                print(f"{name} has been marked present for {date}.")
        
        else: 
            
                self.attendace_list[name] = [date]
                
                print(f"{name} has been present for {date}")      
                
    def view_attendace(self):
           
        if not self.attendace_list: 
            
            print("No attendce records found.")
        
        else: 
            print("Attence List")
            
            for name , dates in self.attendace_list.items():
                print (f"{name} : {','.join(dates)}") 
                
                
    def view_specific_attendance(self,name ):
        if name in self.attendace_list:
            dates = self.attendace_list
            
            print(f"{name} has been present on: {','.join(dates)}")
        
        else:
            
                            
            print(f"No attendace records found for { name}.")
            
            
            
    def run(self):
        
        while True: 
            
            print("\nAttendance Management System")
            
            print("1. Mark Attendace")                              
            print("2. View Attendace")
            print("3. View Specific Attendace")
            print("4. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice =="1":
                name = input("Enter the name of the member: ")
                self.mark_attendace(name)
                
            elif choice =="2":
                self.view_attendace()
                
            elif choice =="3":
                name = input("Enter the name of the member: ")
                self.view_specific_attendance(name)
            
            elif choice == "4:":
            
                print("Exiting the system.")
                break
            
            else:    
                print("invalid choice. Please try again.")  
                
                
if __name__ == "__main__":
    
    system = Attendancesystem()
    
    system.run()                  