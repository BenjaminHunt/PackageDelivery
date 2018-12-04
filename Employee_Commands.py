import PackageDatabase as pd


def list_packages():
    return pd.execute_command("SELECT * FROM package")


def update_hold_loc(package, location):
    pd.execute_command("")


def mark_in_transit(package, vehicle):
    pd.execute_command("")


def mark_as_delivered(package):
    pd.execute_command("")


def change_expected_delivery(package, date):
    pd.execute_command("")

