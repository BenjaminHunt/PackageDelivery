import PackageDatabase as pd


def execute_admin_command(command):  # execute sql directly
    return pd.execute_command(command)
