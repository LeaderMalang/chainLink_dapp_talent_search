from flask import Flask, request, jsonify

from adapter import  Adapter
from flask_mail import Mail, Message


app = Flask(__name__)
mail= Mail(app)
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '00328f085e7900'
app.config['MAIL_PASSWORD'] = '202ec276f72bae'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())


@app.route('/', methods=['POST'])
def call_adapter():
    data = request.get_json()
    if data == '':
        data = {}
    adapter = Adapter(data)
    return jsonify(adapter.result)
@app.route('/send_email',methods=['POST'])
def send_email():
    data = request.get_json()
    if data == '':
        data = {}
    adapter = Adapter(data)
    return jsonify(adapter.result)

@app.route("/mail_api")
def mail_api():
   msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['someone1@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return jsonify({"error":"","success":"email sent please verify by click the link"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8090', threaded=True)
