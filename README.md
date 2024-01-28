# Overview

The purpose of this project was two- or possibly three-fold.

First, I wanted to learn how to work with SQL relational databases. A long time ago, I had some experience with editing databases directly using SQL and Microsoft Access, but I'd forgotten most of what I knew.

Second, I wanted to create a simple tool that would let me edit an item database for a text-based game. In the future, I would like to create a text-based adventure in which the player would acquire items, and rather than pulling from and storing into lists, I thought it would be good to use a database.

Third, I wanted to create a simple proof-of-concept in which I use a database in a mini text adventure.

The program works more or less as described above. At the start, the program will create a database called "items.db," and within it, four tables called "inventory," "weapons," "armor," and" consumables. The top menu will be displayed with two options: "Developer mode" and "Game mode."

In developer mode, the user can follow the menus to choose any of the four tables in the database and add, delete, edit, or display entries in that table. Each table has from two to five columns. Each of these can be edited after creation except for item_id, which is meant to be immutable because it is the ID that connects the databases shared across databases.

In game mode, the user can play a very brief text "adventure," which amounts more or less to choosing an item that gets added to the inventory table. If the user chooses the potion, they drink the potion, at which point the quantity is reduced. This little exercise is meant purely to illustrate (and, more technically, to teach myself) how a database can be used in a text adventure.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Project Demo Video](https://youtu.be/UMbxJB5KgGw)

# Relational Database

As described up above, the database I am using is called "items.db" and is meant to store a game's item information.

It is divided into four tables: inventory, weapons, armor, consumables. The inventory table only has a column for item_id and the item's quantity. This is because the rest of the information can come from the other databases themselves using JOIN.

The weapons, armor, and consumables tables all have very similar layouts, with columns divided into item_id, item_name, item_desc, sell_value, and then a unique value for each item type. For weapons it is "damage," for armor it is "defense," and for consumables it is "effect."

# Development Environment

The tools I used for this project were VS Code with the Prettier extension and the Python extension, which includes Pylance.
As you may have guessed, the programming language used in this project is Python together with the sqlite3 library.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Python Documentation about SQLite3](https://docs.python.org/3/library/sqlite3.html)
- This site is great for comprehensive referencing

- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- This site is great for easy-to-understand tutorials

- [Stack Overflow](https://stackoverflow.com/)
- This site is great for looking up questions you may have

- [Youtube](https://www.youtube.com/)
- Youtube has tons of tutorials about most things. I watched a number of them, and the one I probably enjoyed the most was: 

- [Youtube](https://www.youtube.com/watch?v=zU7NW0tTyr0)
- This tutorial has very clear explanations and is pretty well organized.

# Future Work

- Code optimizations: A lot of the code is similar, e.g. the menus, and I'm sure there's a way to refactor it to make it more optimized and shorter. For the purposes of this assignment, I was focused more on getting something working, but the code is not optimized.

- Quantity/delete sections: Originally, I wanted the player to drink both potions and then to delete the potion entry from the player's inventory, but I wasn't able to get the logic right on that one, so it's something I'd like to continue working on.

- More game: The game portion of the program is obviously just a small snippet, while the end-goal is to have a much longer version. In fact, I would probably want to separate the DB manager program from the actual game.

- A graphical interface could be helpful. At the very least, functions. (This might be part of the code optimization.)
