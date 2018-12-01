import PackageDatabase as pd


active_charge = 0


def place_order(type, weight, source_addr, destination_addr):
    cost_for_delivery = (weight*51)/100
    active_charge = cost_for_delivery

    return cost_for_delivery


def accept_charge(payment_type):
    command = ""
    return command


def list_orders():
    command = ""
    return command


def track_package():
    command = ""
    return command


def bill_status():
    command = ""
    return command
