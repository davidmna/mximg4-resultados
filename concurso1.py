# -*- encoding: utf-8 -*-
import re
import urllib
import sys
#from sys import argv
#from sys import exc_info

try:
	id = sys.argv[1]
	url = "http://www.lohechoenmexico.mx/mximg4/mximg_voto.php?&ID=%s" % id
	f = urllib.urlopen(url)
	html_content = f.read()

	author = re.search("esta\s?es.+<strong>(.*)</strong>", html_content, re.I).group(1)
	votes = re.search("esta.+foto.+tiene.*<strong>(.*)</strong>", html_content, re.I).group(1)
	image = re.search("<img src=\"fotos/(.*)\" alt", html_content, re.I).group(1)
	text = re.search("^\s+</span>(.*)<span class=\"txt1\">", html_content, re.I | re.M | re.S).group(1)

	print "Id: %s" % id
	print "Autor: %s" % author.strip()
	print "Votos: %s" % votes.strip()
	print "Imagen: %s" % image.strip()
	print "Texto: %s" % text.strip()

except:
	 print "Error:", sys.exc_info()[1]