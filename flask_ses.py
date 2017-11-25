import boto3


class SESMailer:
    """AWS Simple Email Service Extension."""

    def __init__(self, app=None):
        """Initialize SES interface.

        :param app: Flask application
        """
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize SESMailer."""
        self.ses_sender = app.config.get('AWS_SES_SENDER')
        self.aws_region = app.config['AWS_SES_REGION_NAME']
        self.aws_access_key_id = app.config['AWS_ACCESS_KEY_ID']
        self.aws_secret_access_key = app.config['AWS_SECRET_ACCESS_KEY']

    @property
    def connection(self):
        if not hasattr(self, '_ses_mailer'):
            self._ses_mailer = boto3.client(
                'ses', region_name=self.aws_region,
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
            )
        return self._ses_mailer

    def send_email(self, recipients, sender=None, subject='', text='', html=''):
        """Send e-mail.

        :param recipients: Recipients e-mails list.
        :param sender: Sender e-mail.
        :param subject: E-mail subject.
        :param text: E-mail body as a text.
        :param html: E-mail body html.
        """
        if sender is None:
            sender = self.ses_sender

        email = self.connection.send_email(
            Source=sender,
            Destination={'ToAddresses': recipients},
            Message={
                'Subject': {'Data': subject},
                'Body': {
                    'Text': {'Data': text},
                    'Html': {'Data': html},
                }
            }
        )
        return email

