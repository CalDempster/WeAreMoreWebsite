from flask import Flask, render_template , request , jsonify
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy class from flask_sqlalchemy module

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MORE.db'
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(80), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    product = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Order('{self.item}', '{self.surname}', '{self.firstname}', '{self.email}' , '{self.product}')"
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)
def makeDatabase():
    db.create_all()
    db.session.commit()
    db.session.close()


@app.route('/')
def home():
    makeDatabase()
    return render_template('order.html')

# region Configs 
# Configure Flask-Mail with the power of SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'wearem.o.r.e10@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'coyp bikd zgel ydau'  # Replace with an app password for security
app.config['MAIL_DEFAULT_SENDER'] = 'wearem.o.r.e10@gmail.com'  
#endregion

@app.route('/send_email', methods=['POST'])
def save_order():
    try:
        product = request.form['Product']
        firstname = request.form['FirstName']
        surname = request.form['Surname']
        email = request.form['Email']
        new_order = Order(firstname=firstname,surname=surname,email=email,product=product)
        db.session.add(new_order)
        db.session.commit()
        db.session.close()
        return jsonify({"message": Order.query.all()})
    except Exception as e:
        return jsonify({"error": "FUCK"})


def send_email():
    try:
        subject = f"Preorder from {request.form['FirstName']} {request.form['Surname']}"
        name = request.form['FirstName']
        email = request.form['Email']
        product = request.form['Product']
        enquiry = request.form['Enquiry']

        msg = Message(subject, recipients=['wearem.o.r.e10@gmail.com'])
        msg.body = f"Product: {product}\nEnquiry: {enquiry}\nEmail: {email}"
        
        cusMsg = Message("Thank you for your enquiry ", recipients=[email])
        cusMsg.html = f"<h1>Thank you for your enquiry {name}</h1><p>We will get back to you as soon as possible</p>"
        
        mail.send(msg)
        mail.send(cusMsg)
        
        return jsonify({"message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
mail = Mail(app)
if __name__ == '__main__':
    app.run(debug=True)