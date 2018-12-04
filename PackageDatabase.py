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
import Admin_Commands as admin
import Employee_Commands as employee

connection = post.connect(host="reddwarf.cs.rit.edu", dbname='nwv4110', user='nwv4110', password='weix8shahcah6aiVee2A')
cursor = connection.cursor()


def main():
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
    if value and value != "Invalid SQL":
        return True
    else:
        return False


# TODO: Determine role of user
def get_role(id):
    if int(id) == 0:
        return "admin"
    elif int(id) > 9000:
        return "employee"
    return "customer"


# TODO: Generate new user with role, and other required information
def new(role):
    if role == "customer":
        last_id = execute_command("SELECT MAX(Id) FROM person WHERE id<9000")
        return last_id[0][0] + 1            # RETURN NEW CUSTOMER
    elif role == "employee":
        last_id = execute_command("Select MAX(id) FROM person WHERE id > 8999")
        if last_id:
            last_id = 9000
            return last_id
        return last_id[0][0] + 1             # RETURN NEW EMPLOYEE
    else:
        return 0   # RETURN NEW ADMIN


def execute_command(command):
    print("db file: " + command)
    try:
        cursor.execute(command)
        value = cursor.fetchall()
        return value
    except:
        connection.rollback()
        return "Invalid SQL"


def parse_and_execute(text, id, role):
    response = "RESPONSE"
    array = text.split()
    print(array)

    if role == "admin":
        response = admin_PAE(text)
    elif role == "customer":
        response = cust_PAE(id, array)
    elif role == "employee":
        response = employee_PAE(id, array)

    return response


def admin_PAE(text):
    if text == "help":
        return "Type anything but help and it will be executed as raw SQL"
    return format(admin.execute_admin_command(text))


def cust_PAE(id, array):
    response = "\"{}\" is not a supported command.".format(array[0])
    if array[0] == "placeorder":  # placeorder <type> <weight> <source_add> <destination_add>
        valid, cost = customer.place_order(id, array[1], array[2], array[3], array[4])  # TODO: INVALID SYNTAX/PARAMETERS RESPONSE
        if valid:
            response = "Order placed. The cost is ${}.".format(cost)
        else:
            response = "Invalid syntax. No order placed."
    elif array[0] == "acceptcharge":
        valid, charge = customer.accept_charge(id)
        if valid:
            response = "{}".format(charge)
        else:
            response = "Invalid syntax. No order placed."
    elif array[0] == "listorders":
        valid, packagesOut, packagesIn = customer.list_orders(id)
        if valid:
            response = "Packages Out:\n{}".format(packagesOut)
            response += "\nPackages In:\n{}".format(packagesIn)
        else:
            response = "Invalid syntax. No order placed."
    elif array[0] == "trackpackage":
        valid, location = customer.track_package(array[1])
        if valid:
            response = "Location of package is {}".format(location)
        else:
            response = "Invalid syntax. No order placed."
    elif array[0] == "billstatus":
        valid, total = customer.bill_status(array[1])
        if valid:
            response = "{}".format(total)
        else:
            response = "Invalid syntax. No order placed."
    elif array[0] == "help":
        response = "Available commands:\n\t" \
                   "placeorder <type> <weight> <source_add> <destination_add>: place an order\n\t" \
                    "acceptcharge: accept the charge associated with package, using your payment method\n\t" \
                    "listorders: list active packages, in and out going\n\t" \
                    "trackpackage <tracking_number>: track location of package by tracking number\n\t" \
                    "billstatus <packageID>: get the status of your bill\n\t" \
                    "help: this menu"
    return response


def employee_PAE(id, array):
    response = "\"{}\" is not a supported command.".format(array[0])
    return response


if __name__ == "__main__":
    main()
