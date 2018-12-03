import PackageDatabase as pd


active_charge = 0


def place_order(type, weight, source_addr, destination_addr): # TODO: Address needs to be standardized somehow.
    valid = True # Was this command valid/successful?
    cost_for_delivery = 20  # (weight*51)/100
    # active_charge = cost_for_delivery
    # pd.execute_command("")
    return valid, cost_for_delivery


def accept_charge(payment_type):
    pd.execute_command("")
    return "Charge of " + str(active_charge) + " accepted"


def list_orders():
    pd.execute_command("")


def track_package(tracking_number):
    location = ""
    expected_delivery = ""
    pd.execute_command("")
    return location, expected_delivery


def bill_status():
    total = 0
    pd.execute_command("")
    return "Bill total: " + str(total)
