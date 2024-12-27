from flask import Flask, jsonify, render_template_string
from math import e
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
app = Flask(__name__)

@app.route('/reset/<token>/<email>', methods=['GET'])
def enviaremail_redefinir(token, email):
    try:
        host = "smtp.hostinger.com"
        port = "465"
        login = ""
        senha = ""

        destinatarios = [email]

        server = smtplib.SMTP(host, port)
        server.ehlo()
        #server.starttls()
        server.login(login, senha)
        with open("C:\\Users\\dimas\\OneDrive\\Documents\\git\\morph\\send email\\reset.html", "r", encoding="utf8") as f:
            template = f.read()
            
        html_content = render_template_string(template, link=token)


        email_msg = MIMEMultipart()
        email_msg['From'] = login
        email_msg['Subject'] = "Redefinição de Senha - Morph!" 
        email_msg.attach(MIMEText(html_content, 'html'))

        server.sendmail(email_msg['From'], destinatarios, email_msg.as_string())
        server.quit()
        return jsonify({'status': 'success', 'message': 'E-mail enviado com sucesso!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Ocorreu um erro durante a execução: {}'.format(str(e))})

if __name__ == '__main__':
    app.run(debug=True)
