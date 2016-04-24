# coding:utf-8

import smtplib, os,sys
from email.mime.text import MIMEText
from src import config

class EmailManager():
    def send_email(self, jokes):
        body = ''
        body_template = '''
        <section class="row tn-article-body">
        <div style="text-align: left; line-height: 1.8;font-size: 17px">
            <p>@content</p>
        </div>
        <section style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
            <img style="max-width: 100%;" src="@picurl">
        </section>
        </section>
        <hr>
        '''

        for item in jokes:
            body += body_template.replace('@content', item.get('content', '')) \
                .replace('@picurl', item.get('picurl', ''))
        email_html = ''

        try:
            path = os.path.join(os.path.dirname(sys.argv[0]),'smstemplate.html')
            file = open(path, 'r', encoding='utf8')
            email_html = file.read()

        except Exception as e:
            print(e)
        finally:
            file.close()

        email_html = email_html.replace('@body', body)

        msg = MIMEText(email_html, _subtype='html', _charset='utf-8')
        msg['From'] = config.mail_user
        msg['To'] = ';'.join(config.receivers)
        msg['Subject'] = '笑话来了'

        smtp = smtplib.SMTP()
        smtp.connect(config.mail_host)
        smtp.login(config.mail_user, config.mail_password)
        smtp.sendmail(config.mail_user, config.receivers, msg.as_string())

        smtp.close()