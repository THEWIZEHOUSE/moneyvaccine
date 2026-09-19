import re
with open('index.html', 'r') as f: html = f.read()
html = html.replace('-ml-4 sm:-ml-8 md:-ml-12', '')
with open('index.html', 'w') as f: f.write(html)
