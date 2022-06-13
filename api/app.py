import os
import json
import logging

logging.basicConfig(
    format='%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s', level='INFO')

from engine import MongoEngine
from flask import Flask, request, jsonify, redirect

from version import read_version


uri = os.environ.get("MONGODB_URL")
database = 'meli_interations'
collection_name = 'interations'

client = MongoEngine(uri)

app = Flask(__name__)

def friends(friends):
    return friends[0].union(friends[1])


def normalize(form):
    for key in ['source', 'target']:
        form[key] = form[key].title() 


@app.route("/", methods=["GET"])
def home():
    return jsonify(read_version())


@app.route("/healthcheck", methods=["GET"])
def healthchek():
    return 'working'


@app.route("/interaction", methods=["POST"])
def interaction():
    form = dict(request.form.items())
    message = f"expects [source, target, book, weight] keys in the body, but receives [{form}]"

    try:
        assert 'source' in form.keys(), message
        assert 'target' in form.keys(), message
        assert 'book' in form.keys(), message
        assert 'weight' in form.keys(), message

        assert int(form['book']) == 4, f"expects only interactions of [book=4], but receives [{form}]" 

        normalize(form)

        r = client.insert_data(database, collection_name, data=form)
        return jsonify({'inserted_id': r}), 201
    
    except Exception as ex:
        return jsonify(f'bad request because: {ex}'), 400


@app.route("/common-friends", methods=["GET"])
def common_friends():
    form = request.args.to_dict()
    message = f"expects [source, target] query paramns, but receives [{form}]"

    try:
        assert 'source' in form.keys(), message
        assert 'target' in form.keys(), message

        normalize(form)
        
        s = [
            set(map(lambda x: x['target'], client.get_data(database, collection_name, {'source': form.get('source')}))),
            set(map(lambda x: x['source'], client.get_data(database, collection_name, {'target': form.get('source')}))),
        ]
        
        t = [
            set(map(lambda x: x['target'], client.get_data(database, collection_name, {'source': form.get('target')}))),
            set(map(lambda x: x['source'], client.get_data(database, collection_name, {'target': form.get('target')}))),
        ]
        s1 = friends(s)
        t1 = friends(t)

        r = {'common-friends': list(s1.intersection(t1)) }
        return jsonify(r), 200

    except Exception as ex:
        return jsonify(f'bad request because: {ex}'), 400


if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port='5000')
