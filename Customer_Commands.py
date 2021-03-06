"""
Title: Customer_Commands
Author: notorious40s
Description: Backend commands a customer can execute across the database.
"""

import PackageDatabase as pd


active_c = 0


"""
Function for placing an order.
"""
def place_order(id, type, weight, destination_addr): # TODO: Address needs to be standardized somehow.
    valid = True # Was this command valid/successful?
    cost_for_delivery = int(weight) * 51/100
    last_id = pd.execute_command("SELECT MAX(id) FROM package")
    receiver_id = pd.execute_command("SELECT id FROM address WHERE state='{}' AND zip={} AND city='{}'"
                                     .format(destination_addr[4], destination_addr[5], destination_addr[3]))
    result = pd.execute_command(("INSERT INTO package VALUES ({}, {}, {}, {}, '{}', '{}', '{}', '{}', {}, {})"
                                 .format(last_id[0][0]+1, id, receiver_id[0][0], cost_for_delivery, type, "medium", "false", "false", weight, 2)))
    if result == "Invalid SQL":
        valid = False
    return valid, cost_for_delivery

"""
Function for grabbing the payment_method of a customer.
"""
def accept_charge(id):
    valid = True # Was this command valid/successful?
    #  TODO: need query here to get users payment type
    payment_type = pd.execute_command("SELECT payment_type FROM person WHERE id={}".format(id))
    if payment_type == "Invalid SQL":
        valid = False
    if active_c != 0:
        return valid, "Charge of " + str(active_c) + " accepted using payment type" + payment_type
    else:
        return valid, "No, active charge."

"""
Function to list the orders a customer has placed.
"""
def list_orders(id):
    valid = True # Was this command valid/successful?
    packagesOut = pd.execute_command("SELECT packageID, cost FROM package WHERE sender={}".format(id))
    packagesIn = pd.execute_command("SELECT packageID, cost FROM package WHERE receiver={}".format(id))
    if packagesIn or packagesOut == "Invalid SQL":
        valid = False
    return valid, packagesOut, packagesIn

"""
Function for tracking the package of a customer.
"""
def track_package(tracking_number):
    valid = True # Was this command valid/successful?
    locationID = pd.execute_command("SELECT locationID FROM log WHERE trackingnumber={}".format(tracking_number))
    location = pd.execute_command("SELECT * FROM location WHERE locationID={}".format(locationID[0][0]))
    if locationID == "Invalid SQL" or location == "Invalid SQL":
        valid = False
    return valid, location[0][1]

"""
Function for grabbing the current cost of a particular package a customer is paying for.
"""
def bill_status(packageID):
    valid = True # Was this command valid/successful?
    total = pd.execute_command("SELECT cost FROM package WHERE packageID={}".format(packageID))
    if total == "Invalid SQL":
        valid = False
    return valid, "Bill total: " + str(total)
