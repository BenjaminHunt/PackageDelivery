import PackageDatabase as pd


active_c = 0


def place_order(id, type, weight, source_addr, destination_addr): # TODO: Address needs to be standardized somehow.
    valid = True # Was this command valid/successful?
    cost_for_delivery = weight * 51/100
    last_id = pd.execute_command("SELECT MAX(id) FROM package")
    result = pd.execute_command(("INSERT INTO package VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (last_id[0][0]+1, id, None, cost_for_delivery, type, "medium", "false", "false", weight, 2)))
    if result == "Invalid SQL":
        valid = False
    return valid, cost_for_delivery


def accept_charge(id):
    valid = True # Was this command valid/successful?
    #  TODO: need query here to get users payment type
    payment_type = pd.execute_command("SELECT payment_type FROM customers WHERE id={}".format(id))
    if payment_type == "Invalid SQL":
        valid = False
    if active_c != 0:
        return valid, "Charge of " + str(active_c) + " accepted using payment type" + payment_type
    else:
        return valid, "No, active charge."


def list_orders(id):
    valid = True # Was this command valid/successful?
    packagesOut = pd.execute_command("SELECT packageID, cost FROM package WHERE sender={}".format(id))
    packagesIn = pd.execute_command("SELECT packageID, cost FROM package WHERE receiver={}".format(id))
    if packagesIn or packagesOut == "Invalid SQL":
        valid = False
    return valid, packagesOut, packagesIn


def track_package(tracking_number):
    valid = True # Was this command valid/successful?
    locationID = pd.execute_command("SELECT locationID FROM log WHERE trackingnumber={}".format(tracking_number))
    location = pd.execute_command("SELECT * FROM location WHERE locationID={}".format(locationID))
    if locationID or location == "Invalid SQL":
        valid = False
    return valid, location


def bill_status(packageID):
    valid = True # Was this command valid/successful?
    total = pd.execute_command("SELECT cost FROM package WHERE packageID={}".format(packageID))
    if total == "Invalid SQL":
        valid = False
    return valid, "Bill total: " + str(total)
