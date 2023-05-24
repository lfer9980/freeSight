import os
import uuid
from app import db
from app import models
from . import public_bp
from flask import request
from flask import jsonify
from datetime import datetime


@public_bp.before_app_request
def create_db():
    test = False
    db.create_all()

    if test:
        id = str(uuid.uuid4())
        msg = 'hola mundo'
        date = datetime.now()
        led = 'sala'
        status = '1'

        test_chat = models.Chat(id=id,
                                msg=msg,
                                datetime=date)

        test_domo = models.Domo(id=id,
                                led=led,
                                status=status,
                                datetime=date)

        db.session.add(test_chat)
        db.session.add(test_domo)
        db.session.commit()


@public_bp.route('/api/v1/public/send-domo', methods=['POST'])
def domo_data():
    try:
        id = str(uuid.uuid4())
        led = str(request.form['led'])
        status = float(request.form['status'])
        time = datetime.now()

    except Exception as e:
        print(e)
        return {'message': 'Datos incompletos'}, 400

    else:
        domo_data = {
            'id': id,
            'led': led,
            'status': status,
            'datetime': time
        }

        domo_data = models.Domo(**domo_data)

        try:
            db.session.add(domo_data)

        except:
            return {'message': 'Error base de datos'}, 500

        else:
            db.session.commit()
            return {'message': 'Guardado correctamente'}, 200


@public_bp.route('/api/v1/public/send-chat', methods=['POST'])
def chat_data():
    try:
        id = str(uuid.uuid4())
        msg = str(request.form['msg'])
        time = datetime.now()

    except Exception as e:
        print(e)
        return {'message': 'Datos incompletos'}, 400

    else:
        chat_data = {
            'id': id,
            'msg': msg,
            'datetime': time
        }

        chat_data = models.Chat(**chat_data)

        try:
            db.session.add(chat_data)

        except:
            return {'message': 'Error base de datos'}, 500

        else:
            db.session.commit()
            return {'message': 'Guardado correctamente'}, 200


@public_bp.route('/api/v1/public/domo', methods=['GET'])
def get_domo_data():
    try:
        domo_data = models.Domo.query.order_by(
            models.Domo.datetime.desc()).limit(1)

        domo_data = domo_data[0]

        resp_domo_data = {
            'led': domo_data.led,
            'status': domo_data.status,
        }

        return jsonify(resp_domo_data)

    except:
        return 'No hay datos, vuelva a intentarlo'


@public_bp.route('/api/v1/public/chat', methods=['GET'])
def get_chat_data():
    try:
        chat_data = models.Chat.query.order_by(
            models.Chat.datetime.desc()).limit(1)

        chat_data = chat_data[0]

        resp_chat_data = {
            'msg': chat_data.msg,
            'date': chat_data.datetime,
        }

        return jsonify(resp_chat_data)

    except:
        return 'No hay datos, vuelva a intentarlo'
