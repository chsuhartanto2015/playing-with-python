#!/usr/bin/env python
from lxml import html
import requests, locale, smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

#Set the limit here.  If the current exchange rate is higher than 'limit'
#you will be notified.
limit = 13380
sender = 'chsuhartanto.2015@gmail.com'
receivers = 'chsuhartanto@gmail.com'

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

#This will fetch the currency quote from Bloomberg's website
page = requests.get('http://www.bloomberg.com/quote/USDIDR:CUR')
tree = html.fromstring(page.text)

#This will create the quote
quote1 = tree.xpath('//div[@class="price"]/text()')
quote2 = ''.join(quote1)

#Take out the comma separator 
quote = locale.atoi(quote2)
limit2 = locale.format("%d", limit, grouping=True)

if (quote > limit):
    message_ori = 'IDR to USD Quote:', quote2 + ". It's time to sell"
    message = ' '.join(message_ori)
    msg = MIMEText(message)
    print 'IDR to USD Quote:', quote2 + ". It's time to sell"
else:
    message_ori = "No Worries.  It's still below", limit2 + ". It's now at", quote2 + "."
    message = ' '.join(message_ori)
    msg = MIMEText(message)
    print "No Worries.  It's still below", limit2 + ". It's now at", quote2 + "."

subject = "USD/IDR Quote from Bloomberg"
msg['From'] = sender
msg['To'] = receivers
msg['Subject'] = subject
s = smtplib.SMTP('localhost')
s.sendmail(sender, [receivers], msg.as_string())
s.quit()

