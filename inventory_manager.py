# Import sqlite to use SQL commands
import sqlite3
# Import time to use for a small bit in "Game mode"
import time


# --- Overview --- #
# 1. Set up database, setup tables.
# 2. Use "Dev mode" menus to add, delete, edit, list table entries.
# 3. Use "Game mode" option to demonstrate how items could be added, deleted, or listed in-game.

connection = sqlite3.connect("items.db")
cursor = connection.cursor()

# ------ Tables ------ #
# Line breaks are used for easier visibility of each table.
# More than one "style" of line break is used to experiment / determine which is preferable.
# (Also, I'm not sure about best practices in this regard)

# I created four tables in what seemed a logical manner at the time, but now I'm unsure if this is the best way to do it.
# Since three of the tables share all but one value, it may be worth making a fifth table that stores the item_id, item_name, item_desc, and sell_value.
# Then, the other tables would only have two values: item_id, and their own unique values (quantity, damage, defense, effect).
# That might be a better way to do it.

# Or maybe the tables should all be combined, and the "unique" values for each table could simply be null-able,
# so that they're only filled in for the items that have them.
# In that case, I would likely also add an extra column for item type.

# Inventory table
cursor.execute('''CREATE TABLE IF NOT EXISTS 
               inventory (
               item_id TEXT NOT NULL,
               quantity INTEGER NOT NULL)''')

# Weapons table
cursor.execute('''CREATE TABLE IF NOT EXISTS 
               weapons (
               item_id TEXT NOT NULL,
               item_name TEXT NOT NULL,
               item_desc TEXT NOT NULL,
               damage INTEGER NOT NULL,
               sell_value INTEGER NOT NULL)''')

# Armor table
cursor.execute("CREATE TABLE IF NOT EXISTS armor (\
               item_id TEXT NOT NULL,\
               item_name TEXT NOT NULL,\
               item_desc TEXT NOT NULL,\
               defense INTEGER NOT NULL,\
               sell_value INTEGER NOT NULL)")

# Consumables table
cursor.execute("CREATE TABLE IF NOT EXISTS consumables (\
               item_id TEXT NOT NULL,\
               item_name TEXT NOT NULL,\
               item_desc TEXT NOT NULL,\
               effect TEXT NOT NULL,\
               sell_value INTEGER NOT NULL)")

# Commit everything to the database. It's so easy to forget...
connection.commit()

# ------ Top Menu ------ #
top_menu_choice = None
while top_menu_choice != 3:
    print("Welcome to the Database: The Game!")
    print("Please select an option below.")
    print("1. Developer mode")
    print("2. Game mode")
    print("3. Quit")
    top_menu_choice = int(input(">> "))

    # ------ Dev Mode ------ #
    if top_menu_choice == 1:
        dev_choice = None
        while dev_choice != 5:
            print("")
            print("Which database would you like to edit?")
            print("1. Inventory")
            print("2. Weapons")
            print("3. Armor")
            print("4. Consumables")
            print("5. Back to top menu")
            dev_choice = int(input(">> "))

            # ------ Dev Mode: Inventory Table ------ #
            if dev_choice == 1:
                inven_choice = None
                while inven_choice !=5:
                    print("")                    
                    print("What do you want to do with the inventory?")
                    print("1. Add item")
                    print("2. Delete item")
                    print("3. Edit item")
                    print("4. Display all items")
                    print("5. Back to previous menu")
                    inven_choice = int(input(">> "))

                    # Add items to inventory
                    if inven_choice == 1:                        
                        item_id = input("Enter an item ID: ")
                        quantity = input("Enter the quantity: ")
                        values = (item_id, quantity)
                        cursor.execute("INSERT INTO inventory VALUES (?, ?)", values)
                        connection.commit()

                    # Delete items from inventory
                    elif inven_choice == 2:
                        item_id = (input("Enter an item ID to delete: "),)
                        cursor.execute("DELETE FROM inventory WHERE item_id=?", item_id)

                    # Edit items in inventory (quantity only - item IDs are unchangeable for now)
                    elif inven_choice == 3:
                        item_id = input("Enter an item ID to edit: ")
                        update = int(input("Select a quantity greater than 0 for this item: "))
                        values = (update, item_id)
                        if update == 0:
                            print("Please select a quantity greater than 0.")
                        else:
                            cursor.execute("UPDATE inventory SET quantity=? WHERE item_id=?", values)
                            connection.commit()

                    # Display everything in inventory
                    elif inven_choice == 4:
                        cursor.execute("SELECT * FROM inventory")
                        table_content = cursor.fetchall()
                        if len(table_content) > 0:
                            for entry in table_content:
                                print(entry)
                        else:
                            print("There are no entries in this table.")

                    elif inven_choice == 5:
                        break

                    else:
                        print("Please enter a valid choice.")

            #------ Dev Mode: Weapons Table ------ #
            elif dev_choice == 2:
                w_table_choice = None
                while w_table_choice !=5:
                    print("")
                    print("What do you want to do with the weapons table?")
                    print("1. Add entry")
                    print("2. Delete entry")
                    print("3. Edit entry")
                    print("4. Display all entries")
                    print("5. Back to previous menu")
                    w_table_choice = int(input(">> "))

                    # Add items to weapons table
                    if w_table_choice == 1:
                        item_id = input("Enter an item ID: ")
                        item_name = input("Enter an item name: ")
                        item_desc = input("Enter a description: ")
                        damage = input("Enter the amount of damage it deals: ")
                        sell_value = input("Enter the item's sell value: ")
                        values = (item_id, item_name, item_desc, damage, sell_value)
                        cursor.execute("INSERT INTO weapons VALUES (?, ?, ?, ?, ?)", values)
                        connection.commit()

                    # Delete items from weapons table
                    elif w_table_choice == 2:
                        item_id = (input("Enter an item ID to delete: "),)
                        cursor.execute("DELETE FROM weapons WHERE item_id=?", item_id)

                    # Edit items in weapons table
                    elif w_table_choice == 3:
                        item_id = input("Enter an item ID to edit: ")
                        attribute = input("Enter the attribute you would like to edit\n(item_name, item_desc, damage, sell_value): ")

                        if attribute == "item_name":
                            update = input("Enter a new name for this item: ")
                            values = (update, item_id)
                            cursor.execute("UPDATE weapons SET item_name=? WHERE item_id=?", values)
                            connection.commit()

                        elif attribute == "item_desc":
                            update = input("Enter a new description for this item: ")
                            values = (update, item_id)
                            cursor.execute("UPDATE weapons SET item_desc=? WHERE item_id=?", values)
                            connection.commit()

                        elif attribute == "damage":
                            update = int(input("Enter a new damage value for this item: "))
                            values = (update, item_id)
                            cursor.execute("UPDATE weapons SET damage=? WHERE item_id=?", values)
                            connection.commit()

                        elif attribute == "sell_value":
                            update = int(input("Enter a new sell value for this item: "))
                            values = (update, item_id)
                            cursor.execute("UPDATE weapons SET sell_value=? WHERE item_id=?", values)
                            connection.commit()

                        else:
                            print("Please select a quantity greater than 0.")

                    # Display all items in weapons table
                    elif w_table_choice == 4:
                        cursor.execute("SELECT * FROM weapons")
                        table_content = cursor.fetchall()
                        if len(table_content) > 0:
                            for entry in table_content:
                                print(entry)
                        else:
                            print("There are no entries in this table.")

                    elif w_table_choice == 5:
                        break

                    else:
                        print("Please enter a valid choice.")

            #------ Dev Mode: Armor Table ------ #
            elif dev_choice == 3:
                a_table_choice = None
                while a_table_choice !=5:
                    print("")
                    print("What do you want to do with the armor table?")
                    print("1. Add entry")
                    print("2. Delete entry")
                    print("3. Edit entry")
                    print("4. Display all entries")
                    print("5. Back to previous menu")
                    a_table_choice = int(input(">> "))

                    # Add items to armor table
                    if a_table_choice == 1:
                        item_id = input("Enter an item ID: ")
                        item_name = input("Enter an item name: ")
                        item_desc = input("Enter a description: ")
                        defense = input("Enter the amount of defense it has: ")
                        sell_value = input("Enter the item's sell value: ")
                        values = (item_id, item_name, item_desc, defense, sell_value)
                        cursor.execute("INSERT INTO armor VALUES (?, ?, ?, ?, ?)", values)
                        connection.commit()

                    # Delete items from armor table
                    elif a_table_choice == 2:
                        item_id = (input("Enter an item ID to delete: "),)
                        cursor.execute("DELETE FROM armor WHERE item_id=?", item_id)

                    # Edit items in armor table
                    elif a_table_choice == 3:
                        item_id = input("Enter an item ID to edit: ")
                        attribute = input("Enter the attribute you would like to edit\n(item_name, item_desc, defense, sell_value): ")

                        if attribute == "item_name":
                            update = input("Enter a new name for this item: ")
                            values = (update, item_id)
                            cursor.execute("UPDATE armor SET item_name=? WHERE item_id=?", values)
                            connection.commit()

                        elif attribute == "item_desc":
                            update = input("Enter a new description for this item: ")
                            values = (update, item_id)
                            cursor.execute("UPDATE armor SET item_desc=? WHERE item_id=?", values)
                            connection.commit()

                        elif attribute == "defense":
                            update = int(input("Enter a new defense value for this item: "))
                            values = (update, item_id)
                            cursor.execute("UPDATE armor SET defense=? WHERE item_id=?", values)
                            connection.commit()

                        elif attribute == "sell_value":
                            update = int(input("Enter a new sell value for this item: "))
                            values = (update, item_id)
                            cursor.execute("UPDATE armor SET sell_value=? WHERE item_id=?", values)
                            connection.commit()

                        else:
                            print("Please enter a valid attribute to edit.")

                    # Display all items in armor table
                    elif a_table_choice == 4:
                        cursor.execute("SELECT * FROM armor")
                        table_content = cursor.fetchall()
                        if len(table_content) > 0:
                            for entry in table_content:
                                print(entry)
                        else:
                            print("There are no entries in this table.")

                    elif a_table_choice == 5:
                        break

                    else:
                        print("Please enter a valid choice.")

            #------ Dev Mode: Consumables Table ------ #
            elif dev_choice == 4:
                c_table_choice = None
                while c_table_choice != 5:
                    print("")
                    print("What do you want to do with the consumables table?")
                    print("1. Add entry")
                    print("2. Delete entry")
                    print("3. Edit entry")
                    print("4. Display all entries")
                    print("5. Back to previous menu")
                    c_table_choice = int(input(">> "))

                    # Add items to consumables table
                    if c_table_choice == 1:
                        item_id = input("Enter an item ID: ")
                        item_name = input("Enter an item name: ")
                        item_desc = input("Enter a description: ")
                        effect = input("Enter the effect of the item: ")
                        sell_value = input("Enter the item's sell value: ")
                        values = (item_id, item_name, item_desc, effect, sell_value)
                        cursor.execute("INSERT INTO consumables VALUES (?, ?, ?, ?, ?)", values)
                        connection.commit()

                    # Delete items from consumables table
                    elif c_table_choice == 2:
                        item_id = (input("Enter an item ID to delete: "),)
                        cursor.execute("DELETE FROM consumables WHERE item_id=?", item_id)

                    # Edit items in consumables table
                    elif c_table_choice == 3:
                        item_id = input("Enter an item ID to edit: ")
                        attribute = input("Enter the attribute you would like to edit\n(item_name, item_desc, effect, sell_value): ")

                        if attribute == "item_name":
                            update = input("Enter a new name for this item: ")
                            values = (update, item_id)
                            cursor.execute("UPDATE consumables SET item_name=? WHERE item_id=?", values)
                            connection.commit()

                        elif attribute == "item_desc":
                            update = input("Enter a new description for this item: ")
                            values = (update, item_id)
                            cursor.execute("UPDATE consumables SET item_desc=? WHERE item_id=?", values)
                            connection.commit()

                        elif attribute == "effect":
                            update = input("Enter a new effect for this item: ")
                            values = (update, item_id)
                            cursor.execute("UPDATE consumables SET effect=? WHERE item_id=?", values)
                            connection.commit()

                        elif attribute == "sell_value":
                            update = int(input("Enter a new sell value for this item: "))
                            values = (update, item_id)
                            cursor.execute("UPDATE consumables SET sell_value=? WHERE item_id=?", values)
                            connection.commit()

                    # Display all items in consumables table
                    elif c_table_choice == 4:
                        cursor.execute("SELECT * FROM consumables")
                        table_content = cursor.fetchall()
                        if len(table_content) > 0:
                            for entry in table_content:
                                print(entry)
                        else:
                            print("There are no entries in this table.")

                    elif c_table_choice == 5:
                        break

                    else:
                        print("Please enter a valid choice.")

            else:
                print("Please enter a valid choice.")

    # ------ Game Mode ------ #
    elif top_menu_choice == 2:
        # Disclaimer that "Game mode" isn't actuall an entire game, but rather meant to be a kind of proof of concept.
        print("")
        print("This is meant to be a small example of how a relational")
        print("database could be used in a text-based adventure.")
        print("")
        print("It is meant to showcase how a program can modify a database")
        print("without a user explicitly telling it what to do.")
        print("")
        print("Without further ado...")

        # Adding input here and every so often below to break up the long text blocks
        input("")

        print("You wake up in a dark room. You don't know how you got there,\nbut you have a headache and feel a throbbing pain on your right side.\nYou reach down and touch your side, only to find your clothes caked in blood.\nYou look around but cannot see anything save for the wall opposite you,\nwhich is faintly lit by a torch whose flame is beginning to smoulder.")
        print("")
        print("Just in front of the wall you see three pedestals, each with a different item.")
        print("You get up and approach the pedestals when suddenly glowing glyphs\nappear on the wall. They're like no language you've ever seen, and\nyet somehow you're able to understand them.")

        input("")

        print("\"Three choices lie before thee,")
        print("to whom this message shows,")
        print("Select an item carefully,")
        print("for when one door opens, two shall close.\"")

        input("")

        print("Which item will you choose?")
        print("")
        print("1. The \x1B[33mlong sword\x1B[0m. The blade looks chipped and slightly rusty,\nbut it still seems to have some fight in it yet.")
        print("")
        print("2. The \x1B[33mpotions\x1B[0m. Even in the dim light, the two flasks emit a bright red glow.\nThe liquid looks sweet, and you're thirsty.")
        print("")
        print("3. The \x1B[33msteel shield\x1B[0m. While it is true that in some situations\nthe best defense is a good offense, generally\nthe best defense is... defense.")
        print("")
        item_choice = int(input(">> "))
    
        # In later scenarios, we would want to check to see if the player already has the selected item in their inventory, in which case we would only increment the quantity. For now, we assume the player has nothing in their inventory.

        if item_choice == 1:
            # This first choice is meant to prove that items from the weapons table can be added and their details displayed properly with the JOIN feature.
            print("As soon as you pick up the long sword, the two other pedestals vanish as though they had never been there.")

            item_id = "long_sword"
            quantity = 1
            values = (item_id, quantity)
            cursor.execute("INSERT INTO inventory VALUES (?, ?)", values)
            connection.commit()

            cursor.execute("SELECT * FROM inventory INNER JOIN weapons ON inventory.item_id = weapons.item_id")
            current_inventory = cursor.fetchall()
            print("")

            # Distinguishing between singular and plural here, not because it fits this particular situation but because it would be useful later. 
            if len(current_inventory) == 1:
                print("You now have the following item in your inventory:")
            else:
                print("You now have the following items in your inventory:")
            for item in current_inventory:
                print(f"Name: \x1B[33m{item[3]}\x1B[0m\nDesc: \"{item[4]}\"\nDamage: {item[5]}\nQuantity Held: {item[1]}\nSell Value: {item[6]}")
                print("")

        elif item_choice == 2:
            # This second choice is meant for a couple things.
            # First, to prove that consumable items can be added to the inventory and displayed with JOIN without issue.
            # Second, to test out the "quantity" column, i.e. to write the code / logic that decreases the quantity when a consumable item is used.

            print("As soon as you pick up the potions, the two other pedestals vanish as though they had never been there.")

            item_id = "health_potion"
            quantity = 2
            values = (item_id, quantity)
            cursor.execute("INSERT INTO inventory VALUES (?, ?)", values)
            connection.commit()            

            cursor.execute("SELECT * FROM inventory INNER JOIN consumables ON inventory.item_id = consumables.item_id")
            current_inventory = cursor.fetchall()
            print("")

            # I wanted to switch to a different form of logic for the singular/plural checking here so as to practice coding.
            # Rather than only checking the length of the current inventory, I wanted to also check and see if the quantity is greater than 1 when there is only one item in the inventory, in which case it would be treated as plural.
            # Admittedly, I'm on the fence about whether having two of a single item should be treated as plural - logically, it makes sense, but from the user's perspective, only a single item is listed, even if the quantity is more than one.
            # Unfortunately, I wasn't able to get the code to work on time, so I'm using the same logic as above.
             
            if len(current_inventory) == 1:
                print("You now have the following item in your inventory:")

            else:
                print("You now have the following items in your inventory:")

            for item in current_inventory:
                print(f"Name: \x1B[33m{item[3]}\x1B[0m\nDesc: \"{item[4]}\"\nEffect: {item[5]}\nQuantity Held: {item[1]}\nSell Value: {item[6]}")
                print("")

            print("Looking down at the flasks in your hands, your thirst only seems to grow stronger.")
            print("Without hesitation, you decide to down one of the potions...")
            for i in range(3):
                time.sleep(0.5)
            print("")
            print("Suddenly, you experience a sensation you've never felt before, as though the sweetness of the potion was imprinted onto your very soul.")
            print("Your wound seems to have healed a bit, and you're feeling much more refreshed than just a moment ago.")

            # I couldn't figure out a better way to do this in time.
            updated_quantity = (1, "health_potion")
            cursor.execute("UPDATE inventory SET quantity=? WHERE item_id=?", updated_quantity)
            connection.commit()

            cursor.execute("SELECT * FROM inventory INNER JOIN consumables ON inventory.item_id = consumables.item_id")
            current_inventory = cursor.fetchall()
            print("You now have the following item in your inventory:")            
            for item in current_inventory:
                print(f"Name: \x1B[33m{item[3]}\x1B[0m\nDesc: \"{item[4]}\"\nEffect: {item[5]}\nQuantity Held: {item[1]}\nSell Value: {item[6]}")
                print("")

            # --------- To-do ---------- #
            # To-do in a future update: write code / logic that removes an item from the inventory when its quantity reaches 0 

        elif item_choice == 3:
            # This third choice is similar to the first, but in a way is meant to verify that it's possible to use the same column reference, i.e. {item[5]}, even if the column / attribute name is different. This is sort of verified in choice #2 as well, but choice #2 has many other things going on, so I thought it worthwhile to check it here.
            #Plus, we have to make sure the armor table is working properly.
            print("As soon as you pick up the , the two other pedestals vanish as though they had never been there.")

            item_id = "steel_shield"
            quantity = 1
            values = (item_id, quantity)
            cursor.execute("INSERT INTO inventory VALUES (?, ?)", values)
            connection.commit()            

            cursor.execute("SELECT * FROM inventory INNER JOIN armor ON inventory.item_id = armor.item_id")
            current_inventory = cursor.fetchall()
            print("")

            if len(current_inventory) == 1:
                print("You now have the following item in your inventory:")
            else:
                print("You now have the following items in your inventory:")
            for item in current_inventory:
                print(f"Name: \x1B[33m{item[3]}\x1B[0m\nDesc: \"{item[4]}\"\nDamage: {item[5]}\nQuantity Held: {item[1]}\nSell Value: {item[6]}")
                print("")

        else:
            print("Please enter a valid choice.")
            input("")         

    elif top_menu_choice == 3:
        print("")
        break
    
    else:
        print("Please enter a valid choice.")
        input("")