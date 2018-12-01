"""
Title: packageDatabase
Team: notorious40s
Description: This is the backend for the sql server that will be inserting the data
             into to the appropriate tables. As of now I only insert into one table
             but the logic for the rest of the tables will be very similar.
"""

import psycopg2 as post
import csv


def main():
    connection = post.connect(host="reddwarf.cs.rit.edu", dbname = 'nwv4110', user = 'nwv4110', password = 'weix8shahcah6aiVee2A')
    cursor = connection.cursor()

    with open("Person.csv") as line:
        writer = csv.reader(line)
        for row in writer:
            i = row[0].strip()
            FirstName = row[1].strip()
            MiddleName = row[2].strip()
            LastName = row[3].strip()
            payment = "paypal"
            balance = 44.00
            #cursor.execute("INSERT INTO person VALUES (%s, %s, %s, %s, %s, %s)", (i, FirstName, MiddleName, LastName, payment, balance))


    connection.commit()
    cursor.close()
    connection.close()


def parse_and_execute(role, text):
    response = "RESPONSE"
    array = text.split()
    print(array)

    if role == "admin":
        response = admin_PAE(array)
    elif role == "customer":
        response = cust_PAE(array)
    elif role == "employee":
        response = employee_PAE(array)

    return response


def admin_PAE(array):
    response = ""
    return response


def cust_PAE(array):
    response = ""
    return response


def employee_PAE(array):
    response = ""
    return response


main()
