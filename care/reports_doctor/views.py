from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from care import db
from care.models import User, Report, Doctor
from care.reports.forms import ReportForm
from care.reports.report_handler import add_report

reports = Blueprint('reports', __name__)

#create
@reports.route('/add_report', methods=['GET', 'POST'])
@login_required
def add_report():
    form = ReportForm()
    if form.validate_on_submit():
        if form.picture.data:
            add_report(form.picture.data)
        report = Report(
            title = form.title.data,
            text = form.text.data,
            user_id = current_user.id,
        )
        db.session.add(report)
        db.session.commit()
        flash('Report Added!')
        return redirect(url_for('core.index'))
    return render_template('add_report.html', form = form)



#view
@reports.route('/<int:report_id>')
def report(report_id):
    report = Report.query.get_or_404(report_id)
    return render_template('report.html', title = report.title,
    date = report.date, report = report)


#delete

@reports.route('/<int:report_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_report(report_id):
    report = Report.query.get_or_404(report_id)
    if report.author != current_user:
        abort(403)
    db.session.delete(report)
    db.session.commit()
    flash('Report Deleted Successfully')
    return redirect(url_for('core.index'))
