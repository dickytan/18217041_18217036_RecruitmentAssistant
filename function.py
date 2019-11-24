import requests
import json
import psycopg2
from psycopg2.extras import RealDictCursor


class DBManager:
    def connect():
        conn = None
        try:
            conn = psycopg2.connect(
                host="127.0.0.1", database="postgres", user="postgres", password="postgres")
            print("Connected")
            return conn
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close(conn):
        if conn is not None:
            conn.close()
            print("Disconnected")

    # GET
    def get_all_tasks():
        conn = DBManager.connect()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(""" SELECT * FROM todo """)
            json_result = json.dumps(cur.fetchall())
        except(Exception, psycopg2.Error) as error:
            dump = [{'Message': 'Failed to get record'}]
            json_result = json.dumps(dump)
        finally:
            DBManager.close(conn)
            return json_result

    def get_all_tasks_by_hrid(hr_id):
        conn = DBManager.connect()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = """ SELECT * FROM todo WHERE hr_id = %(hi)s """
            values = {'hi': hr_id}
            cur.execute(query, values)
            if (cur.rowcount == 0):
                dump = [{'Message': 'Invalid hr_id', 'hr_id': hr_id}]
                json_result = json.dumps(dump)
            else:
                json_result = json.dumps(cur.fetchall())
        except(Exception, psycopg2.Error) as error:
            dump = [{'Message': 'Failed to get record'}]
            json_result = json.dumps(dump)
        finally:
            DBManager.close(conn)
            return json_result

    def get_all_tasks_by_hrid_userid(hr_id, user_id):
        conn = DBManager.connect()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = """ SELECT * FROM todo WHERE hr_id = %(hi)s AND user_id = %(ui)s """
            values = {'hi': hr_id, 'ui': user_id}
            cur.execute(query, values)
            if (cur.rowcount == 0):
                dump = [{'Message': 'Invalid hr_id or user_id',
                         'hr_id': hr_id, 'user_id': user_id}]
                json_result = json.dumps(dump)
            else:
                json_result = json.dumps(cur.fetchall())
        except(Exception, psycopg2.Error) as error:
            dump = [{'Message': 'Failed to get record'}]
            json_result = json.dumps(dump)
        finally:
            DBManager.close(conn)
            return json_result
    # POST

    def add_task(request, hr_id, user_id):
        conn = DBManager.connect()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = """ INSERT INTO todo(hr_id,user_id, task, isDone, due) VALUES ( %(hi)s,  %(ui)s, %(t)s, %(i)s, %(d)s) """
            values = {'hi': hr_id, 'ui': user_id,
                      't': request['task'], 'i': request['isDone'], 'd': request['due']}
            dump = [{'Message': 'Success to insert record'}]
            cur.execute(query, values)
            conn.commit()
        except(Exception, psycopg2.Error) as error:
            dump = [{'Message': 'Failed to insert record'}]
            print(error)
        finally:
            json_result = json.dumps(dump)
            DBManager.close(conn)
            return json_result

    def update_task(request, task_id, hr_id, user_id):
        conn = DBManager.connect()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = """ UPDATE todo SET task = %(t)s, isDone = %(i)s, due = %(d)s WHERE task_id = %(ti)s AND hr_id = %(hi)s AND user_id = %(ui)s """
            values = {'ti': task_id, 'hi': hr_id, 'ui': user_id,
                      't': request['task'], 'i': request['isDone'], 'd': request['due']}
            dump = [{'Message': 'Success to update record'}]
            cur.execute(query, values)
            conn.commit()
        except(Exception, psycopg2.Error) as error:
            dump = {'Message': 'Failed to update record'}
            print(error)
        finally:
            json_result = json.dumps(dump)
            DBManager.close(conn)
            return json_result

# DELETE
    def delete_task(task_id, user_id):
        conn = DBManager.connect()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = """ DELETE FROM todo WHERE task_id = %(t)s AND user_id = %(ui)s """
            values = {'ui': user_id, 't': task_id}
            dump = [{'Message': 'Success to delete record'}]
            cur.execute(query, values)
            conn.commit()
        except(Exception, psycopg2.Error) as error:
            dump = {'Message': 'Failed to delete record'}
            print(error)
        finally:
            json_result = json.dumps(dump)
            DBManager.close(conn)
            return json_result

# SPECIAL
    def add_account(formatted_info):
        conn = DBManager.connect()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            for i in range(len(formatted_info)):
                query = """ INSERT INTO account(acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ( %(i)s,  %(n)s, %(t)s, %(r)s, %(e)s, %(w1)s, %(w2)s) """
                values = {'i': formatted_info[i]['account_id'], 'n': formatted_info[i]['account_name'], 't': formatted_info[i]['account_title'],
                          'r': formatted_info[i]['account_region'], 'e': formatted_info[i]['education_institution'], 'w1': formatted_info[i]['workplace1'], 'w2': formatted_info[i]['workplace2']}
                cur.execute(query, values)
                conn.commit()
            dump = [{'Message': 'Success to insert record'}]
        except(Exception, psycopg2.Error) as error:
            dump = [{'Message': 'Failed to insert record'}]
            print(error)
        finally:
            json_result = json.dumps(dump)
            DBManager.close(conn)
            return json_result

    def get_account():
        conn = DBManager.connect()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(""" SELECT * FROM account """)
            json_result = json.dumps(cur.fetchall())
        except(Exception, psycopg2.Error) as error:
            dump = [{'Message': 'Failed to get record'}]
            json_result = json.dumps(dump)
        finally:
            DBManager.close(conn)
            return json_result

    def get_account_education(education):
        conn = DBManager.connect()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = """ SELECT * FROM account WHERE acc_edu ~* %(ae)s """
            values = {'ae': education}
            cur.execute(query, values)
            if (cur.rowcount == 0):
                dump = [{'Message': 'Invalid account education',
                         'account education': education}]
                json_result = json.dumps(dump)
            else:
                json_result = json.dumps(cur.fetchall())
        except(Exception, psycopg2.Error) as error:
            dump = [{'Message': 'Failed to get record'}]
            json_result = json.dumps(dump)
        finally:
            DBManager.close(conn)
            return json_result

    def get_account_region(region):
        conn = DBManager.connect()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = """ SELECT * FROM account WHERE acc_region ~* %(ar)s """
            values = {'ar': region}
            cur.execute(query, values)
            if (cur.rowcount == 0):
                dump = [{'Message': 'Invalid account region',
                         'account region': region}]
                json_result = json.dumps(dump)
            else:
                json_result = json.dumps(cur.fetchall())
        except(Exception, psycopg2.Error) as error:
            dump = [{'Message': 'Failed to get record'}]
            json_result = json.dumps(dump)
        finally:
            DBManager.close(conn)
            return json_result
