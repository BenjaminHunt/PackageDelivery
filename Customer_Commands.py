import PackageDatabase as pd


active_charge = 0


def place_order(type, weight, source_addr, destination_addr):
    cost_for_delivery = (weight*51)/100
    active_charge = cost_for_delivery
    pd.execute_command("")
    return cost_for_delivery


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
