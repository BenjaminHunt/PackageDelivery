import PackageDatabase as pd


def list_packages():
    valid = True
    result = pd.execute_command("SELECT * FROM package")
    if result == "Invalid SQL":
        valid = False
    return valid, result


def update_hold_loc(package, location):
    valid = True
    result = pd.execute_command("UPDATE package SET location={} WHERE id={}".format(location, package))
    if result == "Invalid SQL":
        valid = False
    return valid


def mark_in_transit(package, vehicle):
    valid = True
    result = pd.execute_command("")
    if result == "Invalid SQL":
        valid = False
    return valid


def mark_as_delivered(package):
    valid = True
    result = pd.execute_command("")
    if result == "Invalid SQL":
        valid = False
    return valid


def change_expected_delivery(package, date):
    valid = True
    result = pd.execute_command("")
    if result == "Invalid SQL":
        valid = False
    return valid

