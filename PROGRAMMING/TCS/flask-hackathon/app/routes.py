from app import app,  bcrypt
from flask import render_template, url_for, flash, redirect, request
from app.forms import RegistrationForm , DetailsForm, searchform
#from flask_login import login_manager, login_user, current_user, logout_user, login_required


data = []


@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    form = RegistrationForm()

    return render_template("index.html",title="blood donation",form=form)
    
try:
    @app.route('/search',methods=['GET','POST'])
    def search():
        print(data)
        bgpost = []
        form = searchform()
        
        if form.validate_on_submit():
            bbid = form.bbid.data
            bg = form.bloodgroup.data
            if bbid:
                info = data[bbid]
            elif bg:
                for post in data:
                    if bg in post:
                        bgpost.append(post)

        return render_template('search.html',form=form,bgpost=bgpost,post=info)


bbid = 1
@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    print("woksjbdkvsbkjsjajvajhdvhasvdhvavsdhvsavjdvjvasjvdv")

    if form.validate_on_submit():
        print("woksjbdkvsbk")
        user = {}
        user[bbid] = [form.username.data,form.email.data,form.number.data,form.address.data,form.bloodgroup.data,form.dob.data,form.age.data,form.ioe_name.data,form.ioe_contact.data,form.ioe_number.data,form.ioe_relation.data,form.password.data]
        bbid += 1
        print(user)
        data.append(user)
    return render_template("register.html",title="blood donation",form=form)


