import logging
from typing import List

import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

from config import config, logger_config


# My endpoint comes here, localhost for now
def retrieve_offers(logger_object: logging.Logger):
    response = requests.get('http://localhost:5000/offers')
    logger_object.info('Sending GET request to own API')
    if response.status_code == 200:
        logger_object.info('Successfully retrieved parsed response from own API')
        return response.json()
    else:
        logger_object.error(f'Failed to retrieve offers from own API: {response.status_code}')
        return None


def send_email(offers: List[dict], logger_object: logging.Logger) -> None:
    # Configure SMTP settings
    smtp_host = config.email_credentials['smtp_host']
    smtp_port = config.email_credentials['smtp_port']
    sender_email = config.email_credentials['sender_email']
    sender_password = config.email_credentials['sender_password']

    # TODO: add more recipient addresses
    recipients = config.recipients

    # Format offers into email body
    email_body = format_offers(offers, logger_object)

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = 'recipient@example.com'  # What do I need to write here? Is this needed?
    msg['Subject'] = f'Offers for {datetime.now().strftime("%Y-%m-%d")}'

    # Attach body to the message
    msg.attach(MIMEText(email_body, 'plain'))

    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        try:
            server.sendmail(sender_email, recipients, msg.as_string())
            logger_object.info(f'Successfully sent mails to all ({len(recipients)}) recipients')
        except (smtplib.SMTPHeloError, smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused, smtplib.SMTPDataError,
                smtplib.SMTPNotSupportedError) as e:
            logger_object.error(f'Failed to send email to ({len(recipients)}) recipients: {type(e).__name__} - {e}')


def format_offers(offers: List[dict], logger_object: logging.Logger) -> str:
    formatted_offers = ""
    logger_object.info('Formatting mail body')
    for offer in offers:
        formatted_offers += f'Offer: {offer}\n'
    logger_object.info('Successfully formatted mail body')
    return formatted_offers


def start_mailer_service():
    logger = logger_config.setup_logger('mailer-logger')
    offers = retrieve_offers(logger)
    # if offers:
    #     send_email(offers, logger)
    # else:
    #     logger.error('No offers retrieved from own endpoint, skipping email sending')


if __name__ == "__main__":
    start_mailer_service()
