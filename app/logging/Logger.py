def create_log_file(success_data):
    date_string = str(date.today().year)+'.'+str(date.today().month)+'.'+str(date.today().day)
    f = open(date_string+'.csv2Email.log','w')
    f.write("Log data for csv2Email.py\n")
    f.write("Date: {0}\n\n".format(date_string))

    f.write("SUCCESFUL EMAILS\n")
    f.write("-----------------------------------\n")
    f.write("Sent Count: {0}\n\n".format(success_data['send_count']))
    
    f.write("VALIDATED EMAILS\n")
    f.write("-----------------------------------\n")
    for item in success_data['valid_emails']:
        f.write("{0}\n".format(item))
    f.write('\n')

    f.write("INVALID EMAILS\n")
    f.write("-----------------------------------\n")
    for item in success_data['invalid_emails']:
        f.write("{0}\n".format(item))
    f.write('\n')
    
    f.write("SEND ERRORS\n")
    f.write("-----------------------------------\n")
    for item in success_data['send_errors']:
        f.write("{0}\n".format(item))
    f.write('\n')

    f.close()