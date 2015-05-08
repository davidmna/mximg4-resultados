# -*- encoding: utf-8 -*-
import mysql.connector
import re
import sys
import urllib

try:
	cnx = mysql.connector.connect(
			user='root', 
			password='', 
			host='localhost',
			database='mximg4')

	cursor = cnx.cursor()

	for id in range(1, 12000):
		url = "http://www.lohechoenmexico.mx/mximg4/mximg_voto.php?&ID=%s" % id
		f = urllib.urlopen(url)
		html_content = f.read()

		author = re.search("esta\s?es.+<strong>(.*)</strong>", html_content, re.I).group(1)
		votes = re.search("esta.+foto.+tiene.*<strong>(.*)</strong>", html_content, re.I).group(1)
		image = re.search("<img src=\"fotos/(.*)\" alt", html_content, re.I).group(1)
		text = re.search("^\s+</span>(.*)<span class=\"txt1\">", html_content, re.I | re.M | re.S).group(1)

		if author != "" and image != "m_":
			print "Id: %s, Votos: %s" % (id, votes)
			add_photo = ("INSERT INTO photos (id, author, votes, image, text) VALUES (%s, %s, %s, %s, %s)")
			data_photo = (id, author, votes, image, text)
			cursor.execute(add_photo, data_photo)

	#cnx.commit()

except:
	print "Error:", sys.exc_info()[1]

finally:
	if cursor:
		cursor.close();
	if cnx:
		cnx.close();
