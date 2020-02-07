import pymysql as mysql

class SFIA:
    def __init__(self):
        self.db=mysql.connect("localhost","root","","sfia_testbed")
        self.c=self.db.cursor()
        self.mainscreen()

    def mainscreen(self):
        print("-------------------------------------------")
        print("Please select one of the following options:")
        print("1: Add new database entry.")
        print("2: View current database entries.")
        print("3: delete a database entry")
        print("-------------------------------------------")
        Main_option = int(input("Option number: "))
        if Main_option == 1:
            self.dataentry()
        elif Main_option == 2:
            self.dataview()
        elif Main_option == 3:
            self.datadelete()
        else:
            print("Unrecognised entry detected. Reinitialising.")
            self.mainscreen()

    def dataentry(self):
        print("Data entry option")
        print("-------------------------------------------")
        print("Which database would you like to add to?")
        print("1: Users")
        print("2: Content")
        print("3: Main menu")
        print("-------------------------------------------")
        Edit_Option = int(input("Option number: "))
        if Edit_Option == 1:
            self.edituser()
        elif Edit_Option == 2:
            self.editcontent()
        elif Edit_Option == 3:
            opt3ret = str(input("Return to main menu? (Y/N) "))
            if opt3ret == "Y" or opt3ret == "y":
                opt3ret = "N"
                self.mainscreen()
            else:
                print("Not returning to mainscreen.")
                self.dataentry()
        else:
            print("Unrecognised entry detected. Refreshing.")
            self.dataentry()
    def edituser(self):
        print("Adding to user database")
        NextUser = c.execute("Select max(user_id) from users")+1
        print("Adding User_ID:", NextUser)                               # Function to look up next value in range
        Username=str(input("Username: "))
        Password=str(input("Password: "))
        Rank=str(input("Custom Rank: "))
        Bio=str(input("Bio: "))
        print("-------------------------------------------")
        save_user = str(input("Save this entry? (Y/N) "))
        if save_user == "Y" or save_user == "y":                #input to table commands
            c.execute("insert into users values("+NextUser+",'"+Username+"','"+Password+"','"+Rank+"','"+Bio+"','')")
            print("User",Username,"saved successfully.")
            AnotherUser=str(input("Input another user? (Y/N) "))
            if AnotherUser="Y" or AnotherUser="y":
                self.edituser()
        else:
            self.dataentry()
    def editcontent(self):
        print("Adding to content database")
        Page_ID = c.execute("Select max(Page_Ref) from content") + 1
        print("Adding role model number: ", Page_ID)  # Function to look up next value in range
        Idol = str(input("Name: "))
        History = str(input("Backstory: "))
        Links = str(input("Links to more info: "))
        print("-------------------------------------------")
        save_content = str(input("Save this entry? (Y/N) "))
        if save_content == "Y" or save_content == "y":  # input to table commands
            c.execute("insert into content values(" + Page_ID + ",'" + Idol + "','" + History + "','" + Links + ")")
            print("Role model", Idol, "saved successfully.")
            AnotherUser = str(input("Input another historical figure? (Y/N) "))
            if AnotherUser="Y" or AnotherUser="y":
                self.editcontent()
        else:
            self.dataentry()

    def dataview(self):
        print("Data view option")
        print("-------------------------------------------")
        print("Which database would you like to view from?")
        print("1: Users")
        print("2: Content")
        print("3: Main menu")
        print("-------------------------------------------")
        Edit_Option = int(input("Option number: "))
        if Edit_Option == 1:
            self.viewuser()
        elif Edit_Option == 2:
            self.viewcontent()
        elif Edit_Option == 3:
            opt3ret = str(input("Return to main menu? (Y/N) "))
            if opt3ret == "Y" or opt3ret == "y":
                opt3ret = "N"
                self.mainscreen()
            else:
                print("Not returning to mainscreen.")
                self.dataview()
        else:
            print("Unrecognised entry detected. Refreshing.")
            self.dataview()

    def dataviewscreen(self,query):
        self.c.execute(query)
        select=self.c.fetchall()
            for file in select:
                ViewID.lines()
                print("User ID:",file[0])
                print("User Name:", file[1])
                print("User Rank:", file[3])
                print("User Bio:", file[4])

    def viewuser(self):
        print("-------------------------------------------")
        print("Search by- options:")
        print("1: User ID number.")
        print("2: User Name.")
        print("3: User Rank.")
        print("4: Previous Menu.")
        print("-------------------------------------------")
        View_Option = int(input("Option number: "))
        if View_Option == 1:
            self.ViewID()
        elif View_Option == 2:
            self.ViewName()
        elif View_Option == 3:
            self.ViewRank()
        else:
            opt3ret = str(input("Return to previous menu? (Y/N) "))
            if opt3ret == "Y" or opt3ret == "y":
                opt3ret = "N"
                self.dataview()
            else:
                print("Not returning to previous menu.")
                self.viewuser()
        else:
            print("Unrecognised entry detected. Refreshing.")
            self.dataview()

    def ViewID(self):
        ID_Num=int(input("Which user ID would you like to search? "))
        self.dataviewscreen("Select * from users where user_id ="+ED_Num+" and deleted is null")

    def ViewName(self):
        U_name=int(input("What name would you like to search? "))
        self.dataviewscreen("Select * from users where username ="+U_Name+" and deleted is null")

    def ViewRank(self):
        U_rank=int(input("Which Rank would you like to search? "))
        self.dataviewscreen("Select * from users where user_id ="+U_rank+" and deleted is null")

    def viewcontent(self):

    def datadelete(self):
        print("Data delete option")

app=SFIA()