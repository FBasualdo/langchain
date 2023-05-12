import sqlite3

conn = sqlite3.connect('db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS products
          ([product_id] INTEGER PRIMARY KEY, 
          [product_name] TEXT,
          [price] MONEY)
          ''')

c.execute('''
          INSERT INTO products (product_id, product_name, price)

                VALUES
                (1,'Marroc', 100),
                (2,'Alfajor', 350),
                (3,'Caramelo', 15),
                (4,'Helado de crema', 300),
                (5,'Helado de agua', 225)
          ''')


conn.commit()
