"""
Title: packageDatabase
Team: notorious40s
Description: This is the backend for the sql server that will be inserting the data
             into to the appropriate tables. As of now I only insert into one table
             but the logic for the rest of the tables will be very similar.
"""

import psycopg2 as post
import csv
import Customer_Commands as customer

connection = post.connect(host="reddwarf.cs.rit.edu", dbname='nwv4110', user='nwv4110', password='weix8shahcah6aiVee2A')
cursor = connection.cursor()


def main():

    print(new("customer"))
    #with open("Person.csv") as line:
        #writer = csv.reader(line)
        #for row in writer:
            #i = row[0].strip()
            #FirstName = row[1].strip()
            #MiddleName = row[2].strip()
            #LastName = row[3].strip()
            #payment = "paypal"
            #balance = 44.00
            #cursor.execute("SELECT * FROM person WHERE id=%s",i)
            #value = cursor.fetchall()
            #print(value)

    connection.commit()
    cursor.close()
    connection.close()


def login(id):
    value = execute_command(("SELECT * FROM person WHERE ID={}".format(id)))
    if value:
        return True
    else:
        return False

# TODO: Generate new user with role, and other required information
def new(role):
    if role == "customer":
        last_id = execute_command("SELECT MAX(Id) FROM person")
        return last_id[0][0] + 1            # RETURN NEW CUSTOMER
    elif role == "employee":
        return 10001            # RETURN NEW EMPLOYEE
    return 12345                # RETURN NEW ADMIN


def execute_command(command):
    cursor.execute(command)
    value = cursor.fetchall()
    return value


def parse_and_execute(text, id, role):
    response = "RESPONSE"
    array = text.split()
    print(array)

    if role == "admin":
        response = admin_PAE(id, array)
    elif role == "customer":
        response = cust_PAE(id, array)
    elif role == "employee":
        response = employee_PAE(id, array)

    return response


def admin_PAE(id, array):
    response = "\"{}\" is not a supported command.".format(array[0])
    return response


def cust_PAE(id, array):
    response = "\"{}\" is not a supported command.".format(array[0])
    if array[0] == "placeorder":  # placeorder <type> <weight> <source_add> <destination_add>
        valid, cost = customer.place_order(id, array[1], array[2], array[3], array[4])  # TODO: INVALID SYNTAX/PARAMETERS RESPONSE
        if valid:
            response = "Order placed. The cost is ${}.".format(cost)
        else:
            response = "Invalid syntax. No order placed."
    return response


def employee_PAE(id, array):
    response = "\"{}\" is not a supported command.".format(array[0])
    return response


if __name__ == "__main__":
    main()
