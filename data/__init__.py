from sqlite3 import Connection
from datetime import datetime, timedelta
conn = Connection("data.db")
c = conn.cursor()

class User:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

class Quiz:
    def __init__(self, vik_id, question, op1, op2, op3, op4, op5, op6, tr_op):
        self.vik_id = vik_id
        self.question = question
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.op5 = op5
        self.op6 = op6
        self.tr_op = tr_op

class Result:
    def __init__(self, id, test_id, ball, time):
        self.id = id
        self.test_id = test_id
        self.bal = ball
        self.time = time


class File:
    def __init__(self, id, file_id, file_name):
        self.id = id
        self.file_id = file_id
        self.file_name = file_name

def default_requests():
    c.execute("CREATE TABLE IF NOT EXISTS users (id, name, phone)")
    c.execute("CREATE TABLE IF NOT EXISTS results (id, test_id, ball, time)")
    c.execute("CREATE TABLE IF NOT EXISTS viks (id INTEGER PRIMARY KEY, vik_name)")
    c.execute("CREATE TABLE IF NOT EXISTS quizs (id INTEGER PRIMARY KEY, vik_id, question, op1, op2, op3, op4, op5, op6, tr_op)")
    c.execute("CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY, file_id, file_name)")

    conn.commit()

def add_user(id, name, phone):
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (id, name, phone))
    conn.commit()

def add_vik(vik_name):
    c.execute("INSERT INTO viks (vik_name) VALUES (?)", (vik_name, ))
    conn.commit()
    return get_viks()[-1]

def add_quiz(vik_id, question, tr_op, op1, op2, op3=None, op4=None, op5=None, op6=None):
    c.execute("INSERT INTO quizs (vik_id, question, op1, op2, op3, op4, op5, op6, tr_op) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (vik_id, question, op1, op2, op3, op4, op5, op6, tr_op))
    conn.commit()

def add_result(id, test_id, ball, time):
    c.execute("INSERT INTO results VALUES (?, ?, ?, ?)", (id, test_id, ball, time))
    conn.commit()

def add_file(file_id, file_name):
    c.execute("INSERT INTO files (file_id, file_name) VALUES (?, ?)", (file_id, file_name))
    conn.commit()

def get_vik(id):
    return c.execute("SELECT vik_name FROM viks WHERE id=?", (id, )).fetchone()

def get_quiz(id):
    data = c.execute("SELECT vik_id, question, op1, op2, op3, op4, op5, op6, tr_op FROM quizs WHERE id=?", (id, )).fetchone()
    if data:
        return Quiz(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])

def get_user(user_id):
    data = c.execute("SELECT id, name, phone FROM users WHERE id=?",(user_id, )).fetchone()
    if data: return User(data[0], data[1], data[2])

def get_result(id, test_id):
    data = c.execute("SELECT id, test_id, ball, time FROM results WHERE id=? AND test_id=?", (id, test_id)).fetchone()
    if data: return Result(data[0], data[1], data[2], data[3])

def get_file(id):
    data = c.execute("SELECT id, file_id, file_name FROM files WHERE id=?", (id, )).fetchone()
    if data: return File(data[0], data[1], data[2])

def get_users():
    return c.execute("SELECT id, name, phone FROM users").fetchall()

def get_viks():
    return c.execute("SELECT id, vik_name FROM viks").fetchall()

def get_quizs_vik(vik_id):
    return c.execute("SELECT id, question, op1, op2, op3, op4, op5, op6, tr_op FROM quizs WHERE vik_id=?", (vik_id, )).fetchall()

def get_results_test(test_id):
    queryset = c.execute("SELECT id, test_id, ball, time FROM results WHERE test_id=? ORDER BY ball DESC", (test_id, )).fetchall()
    return sorted(queryset, key=lambda i: i[3])

def get_results():
    return c.execute("SELECT id, test_id, ball, time FROM results").fetchall()

def get_file_names():
    return c.execute("SELECT id, file_name FROM files ").fetchall()

def get_viks_for_reyting(user_id):
    return list(set(c.execute("SELECT vik_id FROM quizs WHERE id=?", (user_id, )).fetchall()))

def get_files_range(start, stop):
    return c.execute("SELECT id, file_name FROM files WHERE start <= id AND id <= stop").fetchall()

def get_files():
    return c.execute("SELECT id, file_id, file_name FROM files").fetchall()

def del_quiz(quiz_id):
    c.execute("DELETE FROM quizs WHERE id=?", (quiz_id, ))
    conn.commit()

def del_quizs_vik(vik_id):
    c.execute("DELETE FROM quizs WHERE vik_id=?", (vik_id, ))
    conn.commit()

def del_vik(vik_id):
    c.execute("DELETE FROM viks WHERE id=?", (vik_id, ))
    conn.commit()

def del_user(id):
    c.execute("DELETE FROM users WHERE id=?", (id, ))
    conn.commit()

def del_results(id):
    c.execute("DELETE FROM results WHERE id=?", (id, ))
    conn.commit()

def del_result_test(id, test_id):
    c.execute("DELETE FROM results WHERE id=? AND test_id=?")
    conn.commit()

def del_file(id):
    c.execute("DELETE FROM files WHERE id=?", (id, ))
    conn.commit()

def clear_users():
    c.execute("DELETE FROM users")
    conn.commit()

def clear_results():
    c.execute("DELETE FROM results")
    conn.commit()

def clear_files():
    c.execute("DELETE FROM files")
    conn.commit()

def close_db():
    conn.close()
