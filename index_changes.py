from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    # connection dir property
    db_name = 'database.db'

    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Products Application')

        # Creating a Frame Container 
        frame = LabelFrame(self.wind, text = 'Register new Product')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 15)

        # Name Input
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # Price Input
        Label(frame, text = 'Price: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        #Description input
        Label(frame, text = 'Description: ').grid(row = 3, column = 0)
        self.description = Entry(frame)
        self.description.grid(row = 3, column = 1)


        # Button Add Product 
        ttk.Button(frame, text = 'Save Product', command = self.add_product).grid(row = 5, columnspan = 2, sticky = W + E)
        #sticky sirve para posicionar elementos con puntos cardinales

        # Output Messages 
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 4, column = 0, columnspan = 2, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(height = 10, columns = ('#1','#2')) # '#0' SE AGREGA POR DEFAULT, OK PERO ????
        self.tree.grid(row = 4, column = 0, columnspan = 3)
        #self.tree['show']='headings'
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Price', anchor = CENTER)
        self.tree.heading('#2', text = 'Description', anchor = CENTER)


        # Buttons
        ttk.Button(text = 'DELETE', command = self.delete_product).grid(row = 6, column = 1, sticky = W + E )
        ttk.Button(text = 'EDIT', command = self.edit_product).grid(row = 6, column = 2, sticky = W + E)

        # Filling the Rows
        self.get_products()

    # Function to Execute Database Querys
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Get Products from Database
    def get_products(self):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            #print (row)
            #print(row[1],row[2],row[3])
            self.tree.insert('', 0, text = row[1], values = (row[2],row[3]))

    # User Input Validation
    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0 and len(self.description.get())!=0

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?, ?)'
            parameters =  (self.name.get(), self.price.get(), self.description.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Product {} added Successfully'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
            self.description.delete(0,END)
        else:
            self.message['text'] = 'Name, price and description are Required'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'Record {} deleted Successfully'.format(name)
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Please, select Record'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        old_description=self.tree.item(self.tree.selection())['values'][1]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Product'
        # Old Name
        Label(self.edit_wind, text = 'Old name:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 0, column = 2)
        # New Name
        Label(self.edit_wind, text = 'New name:').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        # Old Price 
        Label(self.edit_wind, text = 'Old price:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 2, column = 2)
        # New Price
        Label(self.edit_wind, text = 'New price:').grid(row = 3, column = 1)
        new_price= Entry(self.edit_wind)
        new_price.grid(row = 3, column = 2)

        # Old description
        Label(self.edit_wind,text='Old description').grid(row = 4,column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_description), state = 'readonly').grid(row = 4, column = 2)
        #New description
        Label(self.edit_wind, text = 'New description:').grid(row = 5, column = 1)
        new_description= Entry(self.edit_wind)
        new_description.grid(row = 5, column = 2)


        Button(self.edit_wind, text = 'Update', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price,new_description.get(),old_description)).grid(row = 6, column = 2, sticky = W)
        self.edit_wind.mainloop()

    def edit_records(self, new_name, name, new_price, old_price, new_description,old_description):
        query = 'UPDATE product SET name = ?, price = ?, description = ? WHERE name = ? AND price = ?'
        parameters = (new_name, new_price,new_description,name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated successfylly'.format(name)
        self.get_products()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()