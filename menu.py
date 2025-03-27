from os import *
from ioStuff import *
from client import * 
from property import *
NULL = None
class Menu:
  def __init__(self):
    self.breadcrumb = ""
    self.pageName = ""
    self.minMenuVal = 0
    self.maxMenuVal = 0
    self.menuOptions = []

  def displayPage(self):
    clearScreen()
    print(self.pageName)
    print("---------------------------")
    for option in self.menuOptions:
      print(option)
    print("")

  #======================================

  def displayDashboard(self):
    self.pageName = "Dashboard"
    self.breadcrumb = ">"
    self.minMenuVal = 1
    self.maxMenuVal = 5
    self.menuOptions.clear()
    self.menuOptions.append("1. properties")
    self.menuOptions.append("2. clients")
    self.menuOptions.append("3. Agents")
    self.menuOptions.append("4. viewings")
    self.menuOptions.append("5. log out")
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      self.properties()
    elif choice == 2:
      self.clients()
      
  #======================================
  #property stuufas

  def properties(self):
    self.pageName = "Display properties"
    self.breadcrumb = "Dashboard>"
    self.minMenuVal = 1
    self.maxMenuVal = 4
    self.menuOptions.clear()    
    self.menuOptions.append("1. New property")
    self.menuOptions.append("2. Edit property ")
    self.menuOptions.append("3. delete property")
    self.menuOptions.append("4. Display properties")
    self.menuOptions.append("5. Back")  
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      tmpnewproperty = Property(NULL, NULL, NULL, NULL, NULL)
      self.newproperty(tmpnewproperty)
    elif choice == 2:
      self.editproperty()
    elif choice == 3:
      self.deleteproperty()
    elif choice == 4:
      self.displayproperties()
    elif choice == 5:
      self.displayDashboard()

  def newproperty(self, tmpnewproperty):
            
    self.managedby = tmpnewproperty.getmanagedby()
    self.area = tmpnewproperty.getarea()
    self.bedroomno = tmpnewproperty.getbedroomno()
    self.price = tmpnewproperty.getprice()
    self.status = tmpnewproperty.getstatus()
    
    self.pageName = "New property"
    self.breadcrumb = "Dashboard / New property>"
    self.minMenuVal = 1
    self.maxMenuVal = 7

    self.menuOptions.clear()
    self.menuOptions.append("1. Managed By: ")
    self.menuOptions.append("2. Area: ")
    self.menuOptions.append("3. Number of Bedrooms: ")
    self.menuOptions.append("4. price: ")
    self.menuOptions.append("5. status: ")
    self.menuOptions.append("6. Submit new client to database")
    self.menuOptions.append("7. Back")
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      choice = getString("Managed By: ", minLen=1, maxLen=30)
      self.managedby = choice
      tmpnewproperty.managedby = choice
      self.newproperty(tmpnewproperty)
      
    elif choice == 2:
      choice = getString("Area: ", minLen=1, maxLen=12)
      self.area = choice
      tmpnewproperty.area = choice
      self.newproperty(tmpnewproperty) 

    elif choice == 3:
      choice = getNumber("Number of Bedrooms: ", minVal=0, maxVal=8)
      self.bedroomno = choice
      tmpnewproperty.bedroomno = choice
      self.newproperty(tmpnewproperty) 

    elif choice == 4:
      choice = getMoney("price: ", 1000.00, 999000.00)
      self.price = choice
      tmpnewproperty.price = choice
      self.newproperty(tmpnewproperty)       

    elif choice == 5:
      choice = getString("status:", 1, 10)
      self.status = choice
      tmpnewproperty.status = choice
      self.newproperty(tmpnewproperty) 

    elif choice == 6:
      if getYesNo("Are you sure you want to submit this client?") == "y":
        db.addpToDB(tmpnewproperty)
        self.displayDashboard()
      else:
        self.newproperty(tmpnewproperty) 
      
    elif choice == 7:
      self.displayDashboard()
    
  #======================================
  #Client stoof

  
  def clients(self):
    self.pageName = "clients"
    self.breadcrumb = "Dashboard>"
    self.minMenuVal = 1
    self.maxMenuVal = 4
    self.menuOptions.clear()    
    self.menuOptions.append("1. New client")
    self.menuOptions.append("2. Remove client")
    self.menuOptions.append("3. Display clients")
    self.menuOptions.append("4. Back")  
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      tmpNewclient = client()
      self.newclient(tmpNewclient)
    elif choice == 2:
      self.removeclient
    elif choice == 3:
      self.displayclients() 
    elif choice == 4:
      self.displayDashboard()

  
  def newclient(self, tmpNewclient):
            
    self.managedby = tmpNewclient.getmanagedby()
    self.area = tmpNewclient.getarea()
    self.bedroomno = tmpNewclient.getbedroomno()
    self.price = tmpNewclient.getprice()
    self.status = tmpNewclient.getstatus()
    self.email = tmpNewclient.getEmail()
    self.gender = tmpNewclient.getGender()
    
    self.pageName = "New client"
    self.breadcrumb = "Dashboard / New client>"
    self.minMenuVal = 1
    self.maxMenuVal = 9

    self.menuOptions.clear()
    self.menuOptions.append("1. Managed By: " + self.managedby)
    self.menuOptions.append("2. Area: " + self.area)
    self.menuOptions.append("3. Number of Bedrooms: " + self.bedroomno)
    self.menuOptions.append("5. price: " + self.price)
    self.menuOptions.append("6. status: " + self.status)
    self.menuOptions.append("8. Submit new client to database")
    self.menuOptions.append("9. Back")
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      choice = getString("Managed By: ", minLen=1, maxLen=20)
      self.managedby = choice
      tmpNewclient.managedby = choice
      self.newclient(tmpNewclient)
      
    elif choice == 2:
      choice = getString("Area: ", minLen=1, maxLen=12)
      self.area = choice
      tmpNewclient.area = choice
      self.newclient(tmpNewclient)
  
    elif choice == 3:
      choice = getDate("Number of Bedrooms: ", minLen=1, maxLen=10)
      self.bedroomno = choice
      tmpNewclient.bedroomno= choice
      self.newclient(tmpNewclient)

    elif choice == 5:
      choice = getString("price", 1, 50)
      self.price = choice
      tmpNewclient.price = choice
      self.newclient(tmpNewclient)

    elif choice == 6:
      choice = getstatusNumber("status:")
      self.status = choice
      tmpNewclient.status = choice
      self.newclient(tmpNewclient)

    elif choice == 7:
      choice = getEmail("eMail:")
      self.email = choice
      tmpNewclient.email= choice
      self.newclient(tmpNewclient)

    elif choice == 8:
      if getYesNo("Are you sure you want to submit this client?") == "y":
        db.addclientToDB(tmpNewclient)
        self.displayDashboard()
      else:
        self.newclient(tmpNewclient)
      
    elif choice == 9:
      self.displayDashboard()
#-------------------

def displayproperties(self):
  self.pageName = "Displayproperties"
  self.breadcrumb = "Dashboard>"
  self.minMenuVal = 1
  self.maxMenuVal = 4
  self.menuOptions.clear()
  self.menuOptions.append("1. Display properties (day view)")
  self.menuOptions.append("2. Display properties (week view)")
  self.menuOptions.append("3. Back")
  self.displayPage()
  
  choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
  if choice == 1:
    self.displayDayViewproperties()
  elif choice == 2:
    self.displayWeekViewproperties()
  elif choice == 3:
    self.displayDashboard()

def displayDayViewproperties(self):
  self.pageName = "Display properties (day view)"
  self.breadcrumb = "Dashboard / Display properties (day view)>"
  self.minMenuVal = 1
  self.maxMenuVal = 2

  self.menuOptions.clear()
  self.menuOptions.append("1. Display properties for today")
  self.menuOptions.append("2. Back")
  self.displayPage()

  choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
  if choice == 1:
    self.displayDayViewproperties()
  elif choice == 2:
    self.displayDashboard()

def displayWeekViewproperties(self):
  self.pageName = "Display properties (week view)"
  self.breadcrumb = "Dashboard / Display properties (week view)>"
  self.minMenuVal = 1
  self.maxMenuVal = 2

  self.menuOptions.clear()
  self.menuOptions.append("1. Display properties for this week")
  self.menuOptions.append("2. Back")
  self.displayPage()

  choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
  if choice == 1:
    self.displayWeekViewproperties()
  elif choice == 2:
    self.displayDashboard()



