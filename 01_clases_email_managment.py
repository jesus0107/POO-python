import json
from operator import methodcaller

class Email:
  def __init__(self, email_from = [], subject = None, body = None):
    self.email_from = email_from
    self.subject = subject
    self.body = body
  
  def changeSubject(self, subject: str):
    self.subject = subject

  def changeBody(self, body: str):
    self.body = body


class Gmail:
  name = "Gmail"

class Hotmail:
  name = "Hotmail"

class EmailManagement:
  def __init__(self, email_provider = None):
    self.email_provider = email_provider
  
  def send(self, to: list, text: str ):# -> int
    emails = ",".join(to)
    print(f"Email para {emails}, con texto {text}, con el provedor {self.email_provider.name}")
    return 0

  def checkInbox(self): # -> dict
    emails = []
    # emailTmp =  Email()
    
    # emailTmp.email_from = ["ejemplo@emailcom", "correo@ejemplo.com"]
    # emailTmp.changeSubject("Subject 1")
    # emailTmp.changeBody("Hola a todos")
    
    # emails.append(emailTmp)
    
    # emailTmp.email_from = ["ejemplo@emailcom", "correo@ejemplo.com"]
    # emailTmp.changeSubject("Subject 2")
    # emailTmp.changeBody("Hola a todos")
    
    # emails.append(emailTmp)
    
    # emailTmp.email_from = ["ejemplo@emailcom", "correo@ejemplo.com"]
    # emailTmp.changeSubject("Subject 3")
    # emailTmp.changeBody("Hola a todos")
    
    # emails.append(emailTmp)
    data = [
      {
          "body": "Hola a todos",
          "emails": [
              "ejemplo@emailcom",
              "correo@ejemplo.com"
          ],
          "subject": "Subject 1"
      },
      {
          "body": "Hola a todos",
          "emails": [
              "ejemplo@emailcom",
              "correo@ejemplo.com"
          ],
          "subject": "Subject 2"
      },
      {
          "body": "Hola a todos",
          "emails": [
              "ejemplo@emailcom",
              "correo@ejemplo.com"
          ],
          "subject": "Subject 3"
      }
    ]
    
    for element in data:
      email = Email()
      email.email_from = element["emails"]
      email.changeSubject(element["subject"])
      email.changeBody(element["body"])
      
      emails.append(email)
      
    return emails
  
email_management = EmailManagement()
email_management.email_provider = Gmail()

emails = email_management.checkInbox()
print(json.dumps(emails, default = lambda obj: obj.__dict__,sort_keys=True, indent=4))

resultado = email_management.send(["email1@gmail.com", "email2@gamil.com"], "saludos")
print(f"\n resultado: {resultado}")