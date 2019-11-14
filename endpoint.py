from flask import Flask, request, make_response
from function import DBManager

app = Flask(__name__)


@app.route('/task', methods=['GET'])
def task():
    if request.method == 'GET':
        resp = make_response(DBManager.get_all_tasks(), 200)
    resp.mimetype = "application/json"
    return resp


@app.route('/task/hrid/<hr_id>', methods=['GET'])
def taskhr(hr_id):
    resp = make_response(DBManager.get_all_tasks_by_hrid(hr_id), 200)
    resp.mimetype = "application/json"
    return resp


@app.route('/task/hrid/<hr_id>/uid/<user_id>', methods=['POST', 'PUT', 'GET', 'DELETE'])
def task_hrid_uid(hr_id, user_id):
    if request.method == 'GET':
        resp = make_response(
            DBManager.get_all_tasks_by_hrid_userid(hr_id, user_id), 200)
    elif request.method == 'DELETE':
        resp = make_response(DBManager.delete_task(hr_id, user_id), 200)
    elif request.method == 'POST':
        print(request.get_json())
        resp = make_response(DBManager.add_task(
            request.get_json(), hr_id, user_id), 200)
    elif request.method == 'PUT':
        resp = make_response(DBManager.update_task(
            request.get_json(), hr_id, user_id), 200)
    resp.mimetype = "application/json"
    return resp


if __name__ == '__main__':
    print('Running at port 5000')
    app.run(threaded=True, host='127.0.0.1', port=5000)
