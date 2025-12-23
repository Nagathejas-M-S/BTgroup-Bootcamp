'''
Design Challenge 4: Restaurant Management 
There is a restaurant which has many of its branch at various location. The restaurant offers a wide 
range of menu and there is also a special menu where a discount of 30% is given. Every menu is 
composed of minimum 3 course category have its own items. 
Design the OO model for the above problem statement and implement the code to 
• List the total number of menu items 
• List all the menu items for a particular course category 
• List all the special discount menu 
'''


class MenuItem:
    def __init__(self,name,price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price
        
class CourseCategory:
    def __init__(self,name):
        self.__name = name
        self.__items = []

    @property
    def name(self):
        return self.__name

    @property
    def items(self):
        return self.__items
        
    def add_item(self,item):
        self.__items.append(item)
        
class Menu:
    def __init__(self,name):
        self.__name = name
        self.__categories = []

    @property
    def name(self):
        return self.__name

    @property
    def categories(self):
        return self.__categories
        
    def add_category(self,category):
        self.__categories.append(category)
        
    def total_items(self):
        return sum(len(category.items) for category in self.__categories)
    
    def get_price(self, item):
        return item.price
    
    
class SpecialMenu(Menu):
    def get_price(self, item):
        return item.price * 0.7 # applying 30% discount
    
    
    
class Branch:
    def __init__(self,location):
        self.__location = location
        self.__menus = []

    @property
    def menus(self):
        return self.__menus
        
    def add_menu(self,menu):
        self.__menus.append(menu)
        
    def get_special_menus(self):
        return [menu for menu in self.__menus if isinstance(menu, SpecialMenu)]
    
class Restaurant:
    def __init__(self,name):
        self.__name = name
        self.__branches = []
        
    def add_branch(self,branch):
        self.__branches.append(branch)
        
    # 1. Total number of menu items
    def total_menu_items(self):
        total = 0
        for branch in self.__branches:
            for menu in branch.menus:
                total += menu.total_items()
        return total
    
    # 2. List all menu items for a particular course category
    def list_items_by_category(self, category_name):
        result = []
        for branch in self.__branches:
            for menu in branch.menus:
                for category in menu.categories:
                    if category.name.lower() == category_name.lower():
                        result.extend(category.items)
        return result
    
    # 3. List all special discount menus
    def list_special_menus(self):
        special_menus = []
        for branch in self.__branches:
            special_menus.extend(branch.get_special_menus())
        return special_menus
    
if __name__ == "__main__":
    
    # Create restaurant
    restaurant = Restaurant("Food Palace")

    # Create branch
    branch = Branch("Bangalore")
    restaurant.add_branch(branch)

    # Create categories
    starter = CourseCategory("Starter")
    main_course = CourseCategory("Main Course")
    dessert = CourseCategory("Dessert")

    # Add menu items
    starter.add_item(MenuItem("Soup", 120))
    starter.add_item(MenuItem("Spring Rolls", 150))

    main_course.add_item(MenuItem("Paneer Butter Masala", 260))
    main_course.add_item(MenuItem("Veg Biryani", 230))

    dessert.add_item(MenuItem("Ice Cream", 100))
    dessert.add_item(MenuItem("Gulab Jamun", 90))

    # Create menus
    regular_menu = Menu("Regular Menu")
    special_menu = SpecialMenu("Festive Special Menu")

    # Add categories to menus (minimum 3)
    for menu in (regular_menu, special_menu):
        menu.add_category(starter)
        menu.add_category(main_course)
        menu.add_category(dessert)

    # Add menus to branch
    branch.add_menu(regular_menu)
    branch.add_menu(special_menu)

    # -------- Outputs --------
    print("Total menu items:", restaurant.total_menu_items())

    print("\nStarter Items:")
    for item in restaurant.list_items_by_category("Starter"):
        print(f"- {item.name}")

    print("\nSpecial Discount Menus:")
    for menu in restaurant.list_special_menus():
        print("-", menu.name)

    print("\nPrice Check (Special Menu):")
    print("Original price:", regular_menu.get_price(dessert.items[0]))
    print("Discounted price:", special_menu.get_price(dessert.items[0]))
