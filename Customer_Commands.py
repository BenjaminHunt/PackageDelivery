import PackageDatabase as pd


active_charge = 0


def place_order(id, type, weight, source_addr, destination_addr): # TODO: Address needs to be standardized somehow.
    valid = True # Was this command valid/successful?
    cost_for_delivery = weight * 51/100
    last_id = pd.execute_command("SELECT MAX(id) FROM package")
    pd.execute_command(("INSERT INTO package VALUES (%s, %s, %s, %s, %s, %s, %s, %, %s, %s)",
                       (last_id[0][0]+1, id, None, cost_for_delivery, type, "medium", "false", "false", weight, 2)))
    return valid, cost_for_delivery


def accept_charge(payment_type):
    valid = True # Was this command valid/successful?
    return valid, "Charge of " + str(active_charge) + " accepted"


def list_orders(id):
    valid = True # Was this command valid/successful?
    packagesOut = pd.execute_command("SELECT packageID, cost FROM package WHERE sender={}".format(id))
    packagesIn = pd.execute_command("SELECT packageID, cost FROM package WHERE receiver={}".format(id))
    return valid, packagesOut, packagesIn


def track_package(tracking_number):
    valid = True # Was this command valid/successful?
    locationID = pd.execute_command("SELECT locationID FROM log WHERE trackingnumber={}".format(tracking_number))
    location = pd.execute_command("SELECT * FROM location WHERE locationID={}".format(locationID))
    return valid, location


def bill_status(packageID):
    valid = True # Was this command valid/successful?
    total = pd.execute_command("SELECT cost FROM package WHERE packageID={}".format(packageID))
    return valid, "Bill total: " + str(total)
