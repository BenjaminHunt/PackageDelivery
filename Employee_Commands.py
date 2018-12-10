"""
Title: Employee_Commands
Author: notorious40s
Description: Backend commands an employee role can execute across the database
"""

import PackageDatabase as pd
import time
import datetime

"""
Function for grabbing a specified number of packages in the database.
"""
def list_packages(limit):
    valid = True
    result = pd.execute_command("SELECT * FROM package LIMIT {}".format(limit))
    if result == "Invalid SQL":
        valid = False
    return valid, result

"""
Function for an employee to update a hold location in the delivery process.
"""
def update_hold_loc(packageid, locationid):
    valid = True
    result = pd.execute_command("UPDATE log SET locationid={} WHERE trackingnumber={}".format(locationid,packageid))
    if result == "Invalid SQL":
        valid = False
    return valid

"""
Function for marking a package that as just been shipped, "in transit".
"""
def mark_in_transit(packageid, locationid):
    valid = True
    result = pd.execute_command("UPDATE log SET locationid={} WHERE trackingnumber={}".format(locationid, packageid))
    if result == "Invalid SQL":
        valid = False
    return valid

"""
Function for marking a package as delivered at the current time.
"""
def mark_as_delivered(trackingnumber):
    timestamp = time.time()
    date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    valid = True
    result = pd.execute_command("UPDATE entry SET deliveredtime='{}' WHERE trackingnumber={}".format(date, trackingnumber))
    if result == "Invalid SQL":
        valid = False
    return valid

