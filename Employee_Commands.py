import PackageDatabase as pd


def list_packages(limit):
    valid = True
    result = pd.execute_command("SELECT * FROM package LIMIT {}".format(limit))
    if result == "Invalid SQL":
        valid = False
    return valid, result


def update_hold_loc(package, location):
    valid = True
    logid = pd.execute_command("SELECT MAX(logid) FROM log")
    result = pd.execute_command("INSERT INTO log VALUES({}, {}, {},  ")
    if result == "Invalid SQL":
        valid = False
    return valid


def mark_in_transit(package, vehicle):
    valid = True
    result = pd.execute_command("UPDATE package SET vehicle={} WHERE id={}".format(vehicle, package))
    if result == "Invalid SQL":
        valid = False
    return valid


def mark_as_delivered(trackingnumber, date):
    date = date[0] + " " +  date[1]
    valid = True
    result = pd.execute_command("UPDATE entry SET deliveredtime='{}' WHERE trackingnumber={}".format(date, trackingnumber))
    if result == "Invalid SQL":
        valid = False
    return valid

