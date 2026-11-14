import os
import subprocess
import sqlite3

PASSWORD = "admin123"
def get_user(name):
    conn = sqlite3.connect("app.db")
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return conn.execute(query).fetchall()


def calculate(expression):
    return eval(expression)


def run_command(cmd):
    return subprocess.run(cmd, shell=True)


def add_item(item, items=[]):
    items.append(item)
    return items


def broken():
    return undefined_variable
