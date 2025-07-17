from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    return render_template('items.html', items=[])
