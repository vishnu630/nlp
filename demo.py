import sqlite3 as sql

con=sql.connect('Restaurant_food_data.db')
cur=con.cursor()
foods = ["Idly", "Dosa", "Vada", "Roti", "Meals", "Veg Biryani",
         "Egg Biryani", "Chicken Biryani", "Mutton Biryani",
         "Ice Cream", "Noodles", "Manchooriya", "Orange juice",
         "Apple Juice", "Pineapple juice", "Banana juice"]
for i in range(len(foods)):
    cur.execute(
        "INSERT INTO item VALUES(:item_name,:no_of_customers,:no_of_positives,:no_of_negatives,:pos_perc,:neg_perc)",
        {
            'item_name': foods[i],
            'no_of_customers': "0",
            'no_of_positives': "0",
            'no_of_negatives': "0",
            'pos_perc': "0.0%",
            'neg_perc': "0.0%"
        }
        )
con.commit()
con.close()