import smtplib

def gmailsend(body):
	server = 'smtp.gmail.com'
	port = 587
	sender = 'abcdefghi@gmail.com'
#mail id from the sender 
	password = '123456'
#password of you mail id
	receivers = 'abccceee007@gmail.co'
#receivers email id
	fromPerson = 'TechOffice Automation'
#From name""
	subject = 'Application Health Check - Automated'
#subject
	message = "From:"+fromPerson+"\nTo:"+receivers+"\nMIME-Version: 1.0\nContent-Type: text/html\nSubject: "+subject+"\n\n\n\nHi<br><br> Please find the below checks <br><br>"+body
	
	smtpObj = smtplib.SMTP(server,int(port))
	smtpObj.starttls()
	smtpObj.login(sender,password) 
	smtpObj.sendmail(sender,receivers.split(';'),message)
	print("Mail Sent Successfully")
	
gmailsend("hello")
