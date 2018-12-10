"""
Title: Admin_Commands
Author: notorious40s
Description: Backend command for executing raw SQL for an Admin role.
"""

import PackageDatabase as pd

"""
Single function that simply takes in SQL style commands and executes it directly.
"""
def execute_admin_command(command):  # execute sql directly
    return pd.execute_command(command)
