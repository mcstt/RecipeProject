import tkinter as tk
from tkinter import *
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recipe Book")
        self.geometry("500x500")

        self.filteredItems=[]
        self.frames = {}
        self.frames["HomePage"] = HomePage(self)
        self.frames["HomePage"].grid(row=0, column=0, sticky="nesw")
        self.frames["IngredientsPage"] = IngredientsPage(self)
        self.frames["IngredientsPage"].grid(row=0, column=0, sticky="nesw")
        self.frames["RCPage"] = RCPage(self)
        self.frames["RCPage"].grid(row=0, column=0, sticky="nesw")
        self.frames["Region"] = Region(self)
        self.frames["Region"].grid(row=0, column=0, sticky="nesw")
        self.frames["Country"] = Country(self)
        self.frames["Country"].grid(row=0, column=0, sticky="nesw")
        self.frames["EuropePage"] = EuropePage(self)
        self.frames["EuropePage"].grid(row=0, column=0, sticky="nesw")
        self.frames["AsiaPage"] = AsiaPage(self)
        self.frames["AsiaPage"].grid(row=0, column=0, sticky="nesw")
        self.frames["SouthAmericaPage"] = SouthAmericaPage(self)
        self.frames["SouthAmericaPage"].grid(row=0, column=0, sticky="nesw")
        self.frames["AfricaPage"] = AfricaPage(self)
        self.frames["AfricaPage"].grid(row=0, column=0, sticky="nesw")
        self.frames["CoursePage"] = CoursePage(self)
        self.frames["CoursePage"].grid(row=0, column=0, sticky="nesw")
        self.frames["Recent"] = Recent(self)
        self.frames["Recent"].grid(row=0, column=0, sticky="nesw")

        self.newPage("HomePage")

    def newPage(self, PageName):
        new = self.frames[PageName]
        new.tkraise()






class HomePage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.container = container
        self.RecipeLabel = tk.Label(self, text="Recipes")
        self.RecipeLabel.grid(row=0, column=0)
        self.IngredientsButton = tk.Button(self, text="Ingredients", command=lambda: container.newPage("IngredientsPage"))
        self.IngredientsButton.grid(row=1, column=0)
        self.RCButton = tk.Button(self, text="Region/Country", command=lambda: container.newPage("RCPage"))
        self.RCButton.grid(row=2, column=0)
        self.CoursesButton = tk.Button(self, text="Course Menu", command=lambda: container.newPage("CoursePage"))
        self.CoursesButton.grid(row=3, column=0)
        self.RecentButton = tk.Button(self, text="Recently Viewed", command=lambda: container.newPage("Recent"))
        self.RecentButton.grid(row=5, column=0)
        self.LogOut = tk.Button(self, text="Log Out", command=lambda: container.newPage("MainMenu"))
        self.LogOut.grid(row=0, column=1)
        self.Search = tk.Button(self, text="Search", command=lambda: self.search())
        self.Search.grid(row=1, column=1)


    def filters(self,value):
        self.container.filteredItems.append(value)
        print(self.container.filteredItems)

    def search(self):
        self.listbox = Listbox(height = 10, width = 15, bg = "grey")
        self.listbox.grid(row=2, column=2)

        self.listbox.insert(0, "Massimo")






class IngredientsPage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.homepage = HomePage(container)
        self.IngredientsLabel = tk.Label(self, text="Selecting Ingredients")
        self.IngredientsLabel.grid(row=0, column=0)
        self.EntryBar = tk.Entry(self)
        self.EntryBar.grid(row=1, column=0)
        self.Search = tk.Button(self, text="Search", command=lambda: self.getValue())
        self.Search.grid(row=1,column=1)
        self.BackButton = tk.Button(self,text="Back", command=lambda: container.newPage("HomePage"))
        self.BackButton.grid(row=0, column=1)

    def getValue(self):
        value = self.EntryBar.get()
        self.homepage.filters(value)






class RCPage(tk.Frame):
    def __init__(self,container):
        super().__init__(container)

        self.BackButton = tk.Button(self,text="Back", command=lambda: container.newPage("HomePage"))
        self.BackButton.grid(row=0, column=1)
        self.Region = tk.Button(self, text="Regional Food", command=lambda: container.newPage("Region"))
        self.Region.grid(row=0, column=0)
        self.Country = tk.Button(self, text="Country's Food", command=lambda: container.newPage("Country"))
        self.Country.grid(row=1, column=0)

class Region(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.homepage = HomePage(container)
        self.BackButton = tk.Button(self,text="Back", command=lambda: container.newPage("RCPage"))
        self.BackButton.grid(row=0, column=1)
        self.Europe = tk.Button(self, text="Europe", command=lambda: self.homepage.filters("Europe"))
        self.Europe.grid(row=0, column=0)
        self.Asia = tk.Button(self, text="Asia", command=lambda: self.homepage.filters("Asia"))
        self.Asia.grid(row=1, column=0)
        self.Africa = tk.Button(self, text="Africa", command=lambda: self.homepage.filters("Africa"))
        self.Africa.grid(row=2, column=0)
        self.SouthAmerica = tk.Button(self, text="South America", command=lambda: self.homepage.filters("SouthAmerica"))
        self.SouthAmerica.grid(row=3, column=0)




class Country(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.homepage = HomePage(container)
        self.BackButton = tk.Button(self,text="Back", command=lambda: container.newPage("RCPage"))
        self.BackButton.grid(row=0, column=1)
        self.Europe = tk.Button(self, text="Europe", command=lambda: container.newPage("EuropePage"))
        self.Europe.grid(row=0, column=0)
        self.Asia = tk.Button(self, text="Asia", command=lambda: container.newPage("AsiaPage"))
        self.Asia.grid(row=1, column=0)
        self.Africa = tk.Button(self, text="Africa", command=lambda: container.newPage("AfricaPage"))
        self.Africa.grid(row=2, column=0)
        self.SouthAmerica = tk.Button(self, text="South America", command=lambda: container.newPage("SouthAmericaPage"))
        self.SouthAmerica.grid(row=3, column=0)

class EuropePage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.BackButton = tk.Button(self,text="Back", command=lambda: container.newPage("Country"))
        self.BackButton.grid(row=0, column=1)
        self.Italy = tk.Button(self, text="Italy", command=lambda: container.newPage("HomePage"))
        self.Italy.grid(row=0, column=0)
        self.France = tk.Button(self, text="French", command=lambda: container.newPage("HomePage"))
        self.France.grid(row=1, column=0)
        self.Spain = tk.Button(self, text="Spanish", command=lambda: container.newPage("HomePage"))
        self.Spain.grid(row=2, column=0)
        self.Germany = tk.Button(self, text="German", command=lambda: container.newPage("HomePage"))
        self.Germany.grid(row=3, column=0)
        self.Greece = tk.Button(self, text="Greek", command=lambda: container.newPage("HomePage"))
        self.Greece.grid(row=4, column=0)

class AsiaPage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.BackButton = tk.Button(self,text="Back", command=lambda: container.newPage("Country"))
        self.BackButton.grid(row=0, column=1)
        self.China = tk.Button(self, text="Chinese", command=lambda: container.newPage("HomePage"))
        self.China.grid(row=0, column=0)
        self.Japan = tk.Button(self, text="Japanese", command=lambda: container.newPage("HomePage"))
        self.Japan.grid(row=1, column=0)
        self.India = tk.Button(self, text="Indian", command=lambda: container.newPage("HomePage"))
        self.India.grid(row=2, column=0)
        self.Thailand = tk.Button(self, text="Thai", command=lambda: container.newPage("HomePage"))
        self.Thailand.grid(row=3, column=0)
        self.Korea =  tk.Button(self, text="Korean", command=lambda: container.newPage("HomePage"))
        self.Korea.grid(row=4, column=0)
        self.Vietnam = tk.Button(self, text="Vietnamese", command=lambda: container.newPage("HomePage"))
        self.Vietnam.grid(row=5, column=0)

class AfricaPage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.BackButton = tk.Button(self,text="Back", command=lambda: container.newPage("Country"))
        self.BackButton.grid(row=0, column=1)
        self.Egypt = tk.Button(self, text="Egyptian", command=lambda: container.newPage("HomePage"))
        self.Egypt.grid(row=0, column=0)
        self.SouthAfrica = tk.Button(self, text="South African", command=lambda: container.newPage("HomePage"))
        self.SouthAfrica.grid(row=1, column=0)
        self.Nigeria = tk.Button(self, text="Nigerian", command=lambda: container.newPage("HomePage"))
        self.Nigeria.grid(row=2, column=0)
        self.Morocco = tk.Button(self, text="Moroccan", command=lambda: container.newPage("HomePage"))
        self.Morocco.grid(row=3, column=0)

class SouthAmericaPage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.BackButton = tk.Button(self, text="Back", command=lambda: container.newPage("Country"))
        self.BackButton.grid(row=0, column=1)
        self.Argentina = tk.Button(self, text="Argentinian", command=lambda: self.homepage.filters("Argentina"))
        self.Argentina.grid(row=0, column=0)
        self.Brazil = tk.Button(self, text="Brazilian", command=lambda: self.homepage.filters("Brazil"))
        self.Brazil.grid(row=1, column=0)
        self.Peru = tk.Button(self, text="Peruvian", command=lambda: self.homepage.filters("Peru"))
        self.Peru.grid(row=2, column=0)
        self.Columbia = tk.Button(self, text="Columbian", command=lambda: self.homepage.filters("Columbia"))
        self.Columbia.grid(row=3, column=0)
        self.Chile = tk.Button(self, text="Chilean", command=lambda: self.homepage.filters("Chile"))
        self.Chile.grid(row=4, column=0)


class CoursePage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.homepage = HomePage(container)
        self.BackButton = tk.Button(self,text="Back", command=lambda: container.newPage("HomePage"))
        self.BackButton.grid(row=0, column=1)
        self.Breakfast = tk.Button(self, text="Breakfast", command=lambda: self.homepage.filters("Breakfast"))
        self.Breakfast.grid(row=0, column=0)
        self.Lunch = tk.Button(self, text="Lunch", command=lambda: self.homepage.filters("Lunch"))
        self.Lunch.grid(row=1, column=0)
        self.Dinner = tk.Button(self, text="Dinner", command=lambda: self.homepage.filters("Dinner"))
        self.Dinner.grid(row=2, column=0)
        self.Desert = tk.Button(self, text="Desert", command=lambda: self.homepage.filters("Desert"))
        self.Desert.grid(row=3, column=0)






class Recent(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.BackButton = tk.Button(self,text="Back", command=lambda: container.newPage("HomePage"))
        self.BackButton.grid(row=0, column=1)






app = App()
app.mainloop()
