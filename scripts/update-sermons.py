from bs4 import BeautifulSoup

# TODO: update from share drive/upload to vimeo/sermon.net

with open('../public_html/commons/sermons.html','r') as f:
  sermons_src = BeautifulSoup(f,'html.parser')

long = sermons_src.find_all('div')[1].prettify('utf-8') + sermons_src.find_all('div')[3].prettify('utf-8')

short = sermons_src.find_all('div')[1].prettify('utf-8')
short += '\n<div class="row">\n'
short += sermons_src.find_all('div')[4].prettify('utf-8') + sermons_src.find_all('div')[8].prettify('utf-8') + sermons_src.find_all('div')[12].prettify('utf-8')
short += '\n</div>'
  
with open('../public_html/index.html', 'r+') as f:
  index = BeautifulSoup(f,'html.parser')
  s = index.find(id='fh5co-sermon')
  s.string = short
  f.seek(0)
  str = index.prettify('utf-8').replace('&lt;','<')
  str = str.replace('&gt;','>')
  f.write(str)
  f.truncate()

with open('../public_html/sermons.html', 'r+') as f:
  sermons = BeautifulSoup(f,'html.parser')
  s = sermons.find(id='fh5co-sermon')
  s.string = long
  f.seek(0)
  str = sermons.prettify('utf-8').replace('&lt;','<')
  str = str.replace('&gt;','>')
  f.write(str)
  f.truncate()
