#user/vies.py

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from care import db
from care.models import User, Report, Doctor
from care.doctors.forms import RegistrationForm, LoginForm, UpdateUserForm
from care.doctors.picture_handler import add_profile_pic


doctors = Blueprint('doctors', __name__)

#register

@doctors.route('/doctor_register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        doctor = Doctor(
            email = form.email.data,
            username = form.username.data,
            password = form.password.data)
        db.session.add(doctor)
        db.session.commit()
        flash('Thanks for Registration')
        return redirect(url_for('doctors.login'))
    return render_template('doctor_register.html', form=form)


#login

@doctors.route('/doctor_login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        doctor = Doctor.query.filter_by(email=form.email.data).first()
        if doctor is not None and doctor.check_password(form.password.data):
            login_user(doctor)
            flash('Login Success')
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('core.doctor_index')
            return redirect(next)
    return render_template('doctor_login.html', form=form)






#logout

@doctors.route('/doctor_logout')
def logout():
    logout_user()
    return redirect(url_for("core.index"))


#account

@doctors.route('/doctor_account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic
        current_user.username =  form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your Account is updated')
        return redirect(url_for('doctors.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_image = url_for('static', filename='doctor_profile_pic/'+current_user.profile_image)

    return render_template('doctor_account.html', profile_image = profile_image, form=form)
