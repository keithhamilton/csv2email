#!/usr/bin/python
# coding: utf-8

from smtplib import SMTP, SMTPDataError

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from sys import argv
from time import sleep

from datetime import date

import app.Logger
import app.mail.Mailer
import app.csv.Csv2Dict

#----------------------------------------

if __name__ == '__main__':
    
    # constants
    CSV_FILE_PATH=argv[1]
    SMTP_TIME_OUT=60
    MAX_EMAIL_PER_BATCH=50

    # members
    email_batch_list=[]
    success_data = {
        'valid_emails': [],
        'invalid_emails': [],
        'send_count': 0,
        'send_errors': []
    }

    # read in email body files
    f = open('./app/resource/html_body.txt','r')
    html_text = f.read()
    f.close()

    f = open('./app/resource/plain_text_body.txt','r')
    plain_text = f.read()
    f.close()

    # generate dictionary of email recipients
    name_email_dictionary = Csv2Dict.parse(CSV_FILE_PATH)
    
    # get batch count
    email_count = len(name_email_dictionary)
    print(str(email_count)+' total emails to send')
    total_batch_count = email_count/MAX_EMAIL_PER_BATCH
    current_batch = 1

    if email_count % MAX_EMAIL_PER_BATCH > 0:
        total_batch_count += 1

    # Main Loop
    # while the name_email_dictionary has members
    while name_email_dictionary:
        for i in range(MAX_EMAIL_PER_BATCH):
            # if the dictionary still has members
            if name_email_dictionary:
                # pop an item and append it to the batch list
                email_batch_list.append(name_email_dictionary.popitem())
        # when the batch_list has reached 50 members, run the generate email method
        
        batch_success_data = Mailer.generateEmail(email_batch_list, current_batch, total_batch_count, html_text, plain_text, SMTP_TIME_OUT)
        current_batch += 1

        # update statistics
        for item in batch_success_data['valid_emails']:
            success_data['valid_emails'].append(item)
        for item in batch_success_data['invalid_emails']:
            success_data['invalid_emails'].append(item)
        for item in batch_success_data['send_errors']:
            success_data['send_errors'].append(item)
        success_data['send_count'] += batch_success_data['send_count']

        #reset batch list
        email_batch_list = []
        
    Logger.create_log_file(success_data)
