from app import flask_app
from flask import request
from app.models import Illness, Therapy, Diagnostic
from flask import jsonify


@flask_app.route('/getillnesinfo', methods=['GET'])
def get_illness_info():
    therapy_info = set()
    diagnosis_info = set()
    for elem in request.args.items():
        t = set(Therapy.query.get(str(elem[1])).get_therapy().split(','))
        d = set(Diagnostic.query.get(str(elem[1])).get_diagnosis().split(','))
        therapy_info.update(t)
        diagnosis_info.update(d)
    return jsonify({'therapy': list(therapy_info), 'diagnosis': list(diagnosis_info)})


@flask_app.route('/updatedb', methods=['GET'])
def update_db():
    new_info = dict()
    for i, elem in enumerate(Illness.query.all()):
        new_info[i] = elem.to_dict()
    return jsonify(new_info)


@flask_app.route('/test', methods=['GET'])
def test():
    return "done"
