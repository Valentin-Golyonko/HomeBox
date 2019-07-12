from flask import (
    Blueprint, render_template
)

from db import get_db, close_db
from color_log.Log_Color import *

bp = Blueprint('sensors', __name__)
db_data = []


@bp.route('/sensors')
def index():
    log_verbose("sensors: index()")
    global db_data
    cur = get_db().cursor()
    db_data = cur.execute(
        'SELECT *'
        ' FROM bme280'
        ' ORDER BY created DESC LIMIT 20'
    ).fetchall()
    close_db()
    return render_template('sensors/sensors.html', db_data=[db_data])


@bp.route('/sensors/temp_bme280')
def show_tem_bme280():
    log_verbose("sensors: show_tem_bme280()")
    _id = [i['id'] for i in db_data]
    t = [i['temperature'] for i in db_data]
    h = [i['humidity'] for i in db_data]
    p = [i['pressure'] for i in db_data]
    c = [i['created'].strftime('%Y-%m-%d %H:%M:%S') for i in db_data]
    log_info("\tcreated: %s %s" % (c, type(c[0])))
    return render_template('sensors/temp_bme280.html', db_data=[db_data, _id, t, h, p, c])


@bp.route('/sensors/hum_bme280')
def show_hum_bme280():
    log_verbose("sensors: show_hum_bme280()")
    _id = [i['id'] for i in db_data]
    t = [i['temperature'] for i in db_data]
    h = [i['humidity'] for i in db_data]
    p = [i['pressure'] for i in db_data]
    c = [i['created'].strftime('%Y-%m-%d %H:%M:%S') for i in db_data]
    log_info("\tcreated: %s %s" % (c, type(c[0])))
    return render_template('sensors/hum_bme280.html', db_data=reversed([db_data, _id, t, h, p, c]))
