# core/views.py

from flask import render_template,request,Blueprint
from care.models import Report

core = Blueprint('core',__name__)

@core.route('/')
def index():
    # MORE TO COME!
    page = request.args.get('page', 1, type=int)
    reports = Report.query.order_by(Report.date.desc()).paginate(page=page, per_page=3)
    return render_template('index.html', reports=reports)

@core.route('/info')
def info():
    return render_template('info.html')

@core.route('/doctor_index')
def doctor_index():
    return render_template('doctor_index.html')
