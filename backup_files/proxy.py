from flask import Flask, request
import requests

app = Flask(__name__)
BADGR_URL = 'http://nginx/'
CLIENT_ID = 'moodle'

@app.route('/o/token', methods=['POST'])
def tokenized():
	print('Token got!')
	print(type(request.form))
	n_form = dict(request.form)
	n_form['client_id'] = CLIENT_ID
	n_form['grant_type'] = 'password'
	n_form['scope'] = 'rw:profile rw:issuer rw:backpack'
	print(n_form)
	resp = requests.post(BADGR_URL+'o/token', data=n_form)
	return dict(resp.json())

@app.route('/<path:generic>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def fallback(generic):
	print('Generic path!')
	print(generic)
	print(request.data)
	if request.method == 'GET':
		resp = requests.get(BADGR_URL+generic, data=request.data, headers=dict(request.headers))
	elif request.method == 'POST':
		resp = requests.post(BADGR_URL+generic, data=request.data, headers=dict(request.headers))
	elif request.method == 'PUT':
		resp = requests.put(BADGR_URL+generic, data=request.data, headers=dict(request.headers))
	else:
		resp = requests.delete(BADGR_URL+generic, data=request.data, headers=dict(request.headers))
	return resp.json()
	
