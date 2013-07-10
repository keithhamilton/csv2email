def generateEmail(email_batch_list,current_batch, total_batch_count,html_text,plain_text,smtp_time_out):
    print('sending batch of 50...({0} of {1})'.format(current_batch, total_batch_count))
    return_data = {
        'valid_emails': [],
        'invalid_emails': [],
        'send_count': 0,
        'send_errors': []
    }


    mail_server = SMTP('smtp-pdx.wk.com')
    
    # iterating through batch list
    for item in email_batch_list:
        to_address = item[0]
        from_address = 'megan.a@wk.com'
        
        message_text_html = html_text.format(item[1])
        message_plain_text = plain_text.format(item[1])

        # create email object
        email = MIMEMultipart('alternative')
        email['Subject'] = 'Can we cast you in a Dodge commercial?'
        email['From'] = from_address
        email['To'] = to_address

        # set MIME content based on read-in files
        plain_text_body = MIMEText(message_plain_text, 'plain')
        html_body = MIMEText(message_text_html, 'html')

        # attach to email
        email.attach(plain_text_body)
        email.attach(html_body)

        # validating email using SMTP server
        #address_valid = mail_server.verify(to_address)
        # if email is valid, return code will be less than 400
        #if address_valid[0] < 400:
        return_data['valid_emails'].append(to_address)
        try:
            mail_server.sendmail(from_address, to_address, email.as_string())
            return_data['send_count'] += 1
           
        except:
            return_data['send_errors'].append(to_address)
            pass

        # if email is not valid, append to invalid emails list
        #else:
        #    return_data['invalid_emails'].append(to_address)
        #    return_data['send_errors'].append(to_address)

    mail_server.quit()

    print('pausing for {0} seconds...'.format(smtp_time_out))
    sleep(smtp_time_out)

    return return_data