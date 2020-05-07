from flask import Flask, request, make_response
from flask_cors import CORS
from function import DBManager
import requests

app = Flask(__name__)
CORS(app)


@app.route('/task', methods=['GET'])
def task():
    resp = make_response(DBManager.get_all_tasks(), 200)
    resp.mimetype = "application/json"
    return resp


@app.route('/task/hrid/<hr_id>', methods=['GET'])
def taskhr(hr_id):
    resp = make_response(DBManager.get_all_tasks_by_hrid(hr_id), 200)
    resp.mimetype = "application/json"
    return resp


@app.route('/task/hrid/<hr_id>/uid/<user_id>', methods=['POST', 'GET'])
def task_hrid_uid(hr_id, user_id):
    if request.method == 'GET':
        resp = make_response(
            DBManager.get_all_tasks_by_hrid_userid(hr_id, user_id), 200)
    elif request.method == 'POST':
        resp = make_response(DBManager.add_task(
            request.get_json(), hr_id, user_id), 200)
    resp.mimetype = "application/json"
    return resp


@app.route('/task/<task_id>/hrid/<hr_id>/uid/<user_id>', methods=['PUT'])
def task_tid_hrid_uid(task_id, hr_id, user_id):
    resp = make_response(DBManager.update_task(
        request.get_json(), task_id, hr_id, user_id), 200)
    resp.mimetype = "application/json"
    return resp


@app.route('/task/<task_id>/uid/<user_id>', methods=['DELETE'])
def task_uid_task(task_id, user_id):
    resp = make_response(DBManager.delete_task(task_id, user_id), 200)
    resp.mimetype = "application/json"
    return resp


@app.route('/account', methods=['GET', 'POST'])
def account():
    if request.method == 'GET':
        resp = make_response(DBManager.get_account(), 200)
    elif request.method == 'POST':
        info = requests.get('http://3.227.193.57:8001/users/all') #LinkedIn API
        resp = make_response(DBManager.add_account(info.json()), 200)
    resp.mimetype = "application/json"
    return resp


@app.route('/account/education/<education>', methods=['GET'])
def account_edu(education):
    resp = make_response(
        DBManager.get_account_education(education), 200)
    resp.mimetype = "application/json"
    return resp


@app.route('/account/region/<region>', methods=['GET'])
def account_reg(region):
    resp = make_response(
        DBManager.get_account_region(region), 200)
    resp.mimetype = "application/json"
    return resp


if __name__ == '__main__':
    print('Running at port 5000')
    app.run(threaded=True, host='0.0.0.0', port=5000)
