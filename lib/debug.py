#!/usr/bin/env python3
from __init__ import CONN, CURSOR
from department import Department
import ipdb

def reset_database():
    Department.drop_table()
    Department.create_table()
    Department.create("Payroll", "Building A")
    Department.create("HR", "Building B")

reset_database()
ipdb.set_trace()