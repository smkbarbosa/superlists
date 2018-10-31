#importa o selenium
from selenium import webdriver


#seleciona o Firefox como driver
browser = webdriver.Firefox()
#chama o endereço localhost:8000
browser.get('http://localhost:8000')


#testa se o titulo do  browser é django
assert 'Django' in browser.title
