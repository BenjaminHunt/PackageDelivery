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
    #with open("data/Person.csv") as line:
        #writer = csv.reader(line)
        #for row in writer:
            #i = row[3].strip()
            #FirstName = row[0].strip()
            #MiddleName = row[1].strip()
            #LastName = row[2].strip()
            #payment = row[4].strip()
            #balance = row[5].strip()
            #if balance == '':
                #balance = None
            #cursor.execute("INSERT INTO person VALUES(%s, %s, %s, %s, %s, %s)",
                           #(i,FirstName, MiddleName, LastName, payment, balance))

    #with open("data/address.csv") as line:
        #writer = csv.reader(line)
        #for row in writer:
            #i = row[6].strip()
            #state = row[0].strip()
            #city = row[1].strip()
            #zip = row[2].strip()
            #street = row[3].strip()
            #street_num = row[4].strip()
            #Apt_num = row[5]
            #cursor.execute("INSERT INTO address VALUES(%s, %s, %s, %s, %s, %s, %s)",
                        #(i, state, city, zip, street, street_num, Apt_num))

    #with open("data/Location.csv") as line:
        #writer = csv.reader(line)
        #for row in writer:
            #location_id = row[0].strip()
            #type = row[1].strip()
            #cursor.execute("INSERT INTO location VALUES(%s, %s)",(location_id,type))

    #with open("data/MOCK_DATA.csv") as line:
        #writer = csv.reader(line)
        #for row in writer:
            #packageid = row[0].strip()
            #sender = row[1].strip()
            #receiver = row[2].strip()
            #if receiver == '':
                #receiver = None
            #cost = row[3].strip()
            #type = row[4].strip()
            #priority = row[5].strip()
            #ishazard = row[6].strip()
            #if ishazard == '':
                #ishazard = 'false'
            #isinternational = row[7].strip()
            #if isinternational == '':
                #isinternational = 'false'
            #weight = row[9].strip()
            #if weight == '':
                #weight = 0.00
            #value = row[10].strip()
            #if value == '':
                #value = 0
            #cursor.execute("INSERT INTO package VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           #(packageid, sender, receiver, cost, type, priority, ishazard, isinternational, weight, value))
    #connection.commit()

    #with open("data/order.csv") as line:
        #writer = csv.reader(line)
        #for row in writer:
            #trackingnumber = row[0].strip()
            #packageid = row[1].strip()
            #ordertime = row[2].strip()
            #fullfilledtime = row[3].strip()
            #shippertime = row[4].strip()
            #deliveredtime = row[5].strip()
            #cursor.execute("INSERT INTO entry VALUES(%s, %s, %s, %s, %s, %s)",
                           #(trackingnumber,packageid, ordertime, fullfilledtime, shippertime, deliveredtime))
    #connection.commit()

    #with open("data/log.csv") as line:
        #writer = csv.reader(line)
        #for row in writer:
            #log_id = row[0].strip()
            #timestamp = row[1].strip()
            #event = row[2].strip()
            #status = row[3].strip()
            #location_id = row[4].strip()
            #cursor.execute("INSERT INTO log VALUES(%s, %s, %s, %s, %s, %s)",
                        #(log_id, location_id, log_id, timestamp, event, status))

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
    elif int(id) >= 9000:
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
    value = []
    try:
        cursor.execute(command)
        if command[0] != "I":
            value = cursor.fetchall()
        else:
            connection.commit()
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
        return "Type anything but help, logout or role and it will be executed as raw SQL"
    return format(admin.execute_admin_command(text))


def cust_PAE(id, array):
    response = "\"{}\" is not a supported command.".format(array[0])
    if array[0] == "placeorder":  # placeorder <type> <weight> <source_add> <destination_add>
        valid, cost = customer.place_order(id, array[1], array[2], array[3:])  # TODO: INVALID SYNTAX/PARAMETERS RESPONSE
        if valid:
            response = "Order placed. The cost is ${}.".format(cost)
        else:
            response = "Invalid syntax."
    elif array[0] == "acceptcharge":
        valid, charge = customer.accept_charge(id)
        if valid:
            response = "{}".format(charge)
        else:
            response = "Invalid syntax."
    elif array[0] == "listorders":
        valid, packagesOut, packagesIn = customer.list_orders(id)
        if valid:
            response = "Packages Out:\n{}".format(packagesOut)
            response += "\nPackages In:\n{}".format(packagesIn)
        else:
            response = "Invalid syntax."
    elif array[0] == "trackpackage":
        valid, location = customer.track_package(array[1])
        if valid:
            response = "Location of package is {}".format(location)
        else:
            response = "Invalid syntax."
    elif array[0] == "billstatus":
        valid, total = customer.bill_status(array[1])
        if valid:
            response = "{}".format(total)
        else:
            response = "Invalid syntax."
    elif array[0] == "help":
        response = "Available commands:\n\t" \
                   "placeorder <type> <weight> <destination_add>: place an order\n\t" \
                    "acceptcharge: accept the charge associated with package, using your payment method\n\t" \
                    "listorders: list active packages, in and out going\n\t" \
                    "trackpackage <tracking_number>: track location of package by tracking number\n\t" \
                    "billstatus <packageID>: get the status of your bill\n\t" \
                    "logout: log out\n\t" \
                    "role: display your role\n\t" \
                    "help: this menu"
    return response


def employee_PAE(id, array):
    response = "\"{}\" is not a supported command.".format(array[0])
    if array[0] == "listpackages":
        valid, packages = employee.list_packages()
        if valid:
            response = "Packages:\n{}".format(packages)
        else:
            response = "Invalid syntax."
    elif array[0] == "updateholdloc":
        valid = employee.update_hold_loc(array[1],array[2])
        if valid:
            response = "Hold location of "+array[1]+" updated to "+array[2]
        else:
            response = "Invalid syntax."
    elif array[0] == "markintransit":
        valid = employee.mark_in_transit(array[1], array[2])
        if valid:
            response = "Package" + array[1] + " marked in transit on vehicle " + array[2]
        else:
            response = "Invalid syntax."
    elif array[0] == "markasdelivered":
        valid = employee.mark_as_delivered(array[1], array[2:])
        if valid:
            response = "Package" + array[1] + " marked as delivered"
        else:
            response = "Invalid syntax."
    elif array[0] == "help":
        response = "Available commands:\n\t" \
                   "listpackages: list active packages\n\t" \
                   "updateholdloc <package> <location>: update holding location\n\t" \
                   "markintransit <package> <vehicle>: mark a package in transit\n\t" \
                   "markasdelivered <tracking number> <time>: mark a package as delivered\n\t" \
                   "logout: log out\n\t" \
                   "role: display your role\n\t" \
                   "help: this menu"
    return response


if __name__ == "__main__":
    main()
