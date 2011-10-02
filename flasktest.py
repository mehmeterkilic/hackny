#!/usr/bin/env python

import json
import csv

from flask import Flask, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/<name>')
def hello(name):
	return render_template('index.html', name=name)

@app.route('/howie/<name>')
def howie(name):
	return render_template('index.html', name=name)

@app.route('/banks/<state>')
def taxicomplaints(state):
	f = open('banklist.csv')
	rdr = csv.reader(f)
	banks = [row for row in rdr if row[2] == state]
	return render_template('banks.html', state=state,  banks=banks)

if __name__ == "__main__":
	app.run()
