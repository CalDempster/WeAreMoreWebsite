from flask import Flask, render_template , request , jsonify
from flask_mail import Mail, Message
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('order.html')

# Configure Flask-Mail with the power of SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'wearem.o.r.e10@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'coyp bikd zgel ydau'  # Replace with an app password for security
app.config['MAIL_DEFAULT_SENDER'] = 'wearem.o.r.e10@gmail.com'  

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        subject = f"Preorder from {request.form['FirstName']} {request.form['Surname']}"
        recipient = request.form['Email']
        product = request.form['Product']
        enquiry = request.form['Enquiry']

        msg = Message(subject, recipients=[recipient])
        msg.body = f"Product: {product}\nEnquiry: {enquiry}"
        
        mail.send(msg)
        return jsonify({"message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

mail = Mail(app)
if __name__ == '__main__':
    app.run(debug=True)