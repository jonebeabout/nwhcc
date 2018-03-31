from bs4 import BeautifulSoup

with open('../public_html/commons/head.html','r') as f:
  head_src = BeautifulSoup(f,'html.parser')

head = head_src.find('meta').prettify('utf-8')

with open('../public_html/commons/footer.html','r') as f:
  footer_src = BeautifulSoup(f,'html.parser')

footer = footer_src.find_all('div')[0].prettify('utf-8') + footer_src.find_all('div')[1].prettify('utf-8') + footer_src.find_all('div')[2].prettify('utf-8') + footer_src.find_all('div')[3].prettify('utf-8')

with open('../public_html/commons/service_times.html','r') as f:
  times_src = BeautifulSoup(f,'html.parser')  

times = times_src.find_all('div')[1].prettify('utf-8') + times_src.find_all('div')[3].prettify('utf-8')
  
with open('../public_html/commons/verses.html','r') as f:
  verses_src = BeautifulSoup(f,'html.parser')

verses = verses_src.find_all('div')[1].prettify('utf-8') + verses_src.find_all('div')[2].prettify('utf-8')

with open('../public_html/index.html', 'r+') as f:
  index = BeautifulSoup(f,'html.parser')
  index.head.string = head
  index.footer.string = footer
  t = index.find(id='fh5co-counter')
  t.string = times
  v = index.find(id='fh5co-bible-verse')
  v.string = verses
  f.seek(0)
  str = index.prettify('utf-8').replace('&lt;','<')
  str = str.replace('&gt;','>')
  f.write(str)
  f.truncate()

with open('../public_html/sermons.html', 'r+') as f:
  sermons = BeautifulSoup(f,'html.parser')
  sermons.head.string = head
  sermons.footer.string = footer
  t = sermons.find(id='fh5co-counter')
  t.string = times
  f.seek(0)
  str = sermons.prettify('utf-8').replace('&lt;','<')
  str = str.replace('&gt;','>')
  f.write(str)
  f.truncate()
  
with open('../public_html/ministries.html', 'r+') as f:
  ministries = BeautifulSoup(f,'html.parser')
  ministries.head.string = head
  ministries.footer.string = footer
  t = ministries.find(id='fh5co-counter')
  t.string = times
  f.seek(0)
  str = ministries.prettify('utf-8').replace('&lt;','<')
  str = str.replace('&gt;','>')
  f.write(str)
  f.truncate()

with open('../public_html/events.html', 'r+') as f:
  events = BeautifulSoup(f,'html.parser')
  events.head.string = head
  events.footer.string = footer
  t = events.find(id='fh5co-counter')
  t.string = times
  f.seek(0)
  str = events.prettify('utf-8').replace('&lt;','<')
  str = str.replace('&gt;','>')
  f.write(str)
  f.truncate()

with open('../public_html/beliefs.html', 'r+') as f:
  beliefs = BeautifulSoup(f,'html.parser')
  beliefs.head.string = head
  beliefs.footer.string = footer
  t = beliefs.find(id='fh5co-counter')
  t.string = times
  f.seek(0)
  str = beliefs.prettify('utf-8').replace('&lt;','<')
  str = str.replace('&gt;','>')
  f.write(str)
  f.truncate()
  
with open('../public_html/contact.html', 'r+') as f:
  contact = BeautifulSoup(f,'html.parser')
  contact.head.string = head
  contact.footer.string = footer
  t = contact.find(id='fh5co-counter')
  t.string = times
  f.seek(0)
  str = contact.prettify('utf-8').replace('&lt;','<')
  str = str.replace('&gt;','>')
  f.write(str)
  f.truncate()