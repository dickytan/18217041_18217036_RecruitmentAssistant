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

    def update_task(request, hr_id, user_id):
        conn = DBManager.connect()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = """ UPDATE todo SET task = %(t)s, isDone = %(i)s, due = %(d)s WHERE hr_id = %(hi)s AND user_id = %(ui)s """
            values = {'hi': hr_id, 'ui': user_id,
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
    def delete_task(task, user_id):
        conn = DBManager.connect()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = """ DELETE FROM todo WHERE task = %(t)s AND user_id = %(ui)s """
            values = {'ui': user_id, 't': task}
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
