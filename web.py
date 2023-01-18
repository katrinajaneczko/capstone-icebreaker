# pip3 install flask

import os

from flask import Flask, render_template

from functools import lru_cache
import time

import sys

sys.path.append('.') # so we can import api below
from api import get_user as _get_user, get_syllabi as _get_syllabi, get_syllabus as _get_syllabus

def cached(f, seconds=60):
    """
    decorator
    Cache function calls with a TTL
    """
    @lru_cache()
    def expensive(*args, ttl_hash=None, **kwargs):
        del ttl_hash
        return f(*args, **kwargs)

    def _f(*args, **kwargs):
        return expensive(*args, ttl_hash=round(time.time() / seconds), **kwargs)
    return _f

get_user = cached(_get_user)
get_syllabi = cached(_get_syllabi)
get_syllabus = cached(_get_syllabus)

app = Flask('syllabusapp', root_path=os.getcwd())
@app.route('/')
def index():
    _, user = get_user()
    _, syllabi = get_syllabi() 
    syllabi = syllabi['syllabi']
    return render_template('index.html', user=user, syllabi=syllabi)

@app.route('/syllabus/<syl_id>')
def syllabus_detail(syl_id):
    _, syllabus = get_syllabus(syl_id)
    _, user = get_user()
    return render_template('syllabus.html', user=user, syllabus=syllabus)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(debug=True)


