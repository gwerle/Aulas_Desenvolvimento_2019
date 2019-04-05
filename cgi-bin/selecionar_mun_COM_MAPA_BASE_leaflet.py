#!/usr/bin/python
# -*- coding: utf-8 -*-
# ATENÇÃO - para este código funcionar, os layers WMS publicado no Geoserver devem estar originalmente em lat/long e

import psycopg2

conn = psycopg2.connect("dbname = 'sig' port = '5432'  user= 'user' password = 'user' host='localhost'")
cursor = conn.cursor()

def list_municipios():
	results = []
	cursor.execute("""SELECT gid,nome FROM bairros ORDER BY nome""")
	for id,nome in cursor:
		results.append((id, nome))
	return results

print 'Content-Type: text/html; charset=UTF-8\n\n'
print '<html>'
print '<head><title> Aplicativo web </title><head>'
print """<link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.4/dist/leaflet.css"
   integrity="sha512-puBpdR0798OZvTTbP4A8Ix/l+A4dHDD0DGqYW6RQ+9jxkRFclaxxQb/SJAWZfWAkuyeQUytO7+7N4QKrDh+drA=="
   crossorigin=""/>"""
print """<script src="https://unpkg.com/leaflet@1.3.4/dist/leaflet.js"
   integrity="sha512-nMMmRyTVoLYqjP9hrbed9S+FzjZHW5gY1TWCHA5ckwXZBadntCNs8kEqAWdrb9O7rxbCaA4lKTIWjDXZxflOcA=="
   crossorigin=""></script>"""
print '<body>'
print 'Selecione um municipio:'
print '<form method="POST" action="visualizar_mun_COM_MAPA_BASE_leaflet.py">'
print '<select name="MunID" size=10">'

for id,nome in list_municipios():
	print '<option value = "' + str(id)+'">'+nome+'</option>'

print '</select>'
print '<p>'
print '<input type="submit" value="Enviar">'
print '</form>'

print '<div id="map" style="width: 800px; height: 500px"></div>'
print """
<script>

	var mymap = L.map('map').setView([-25.45, -49.27], 10);



	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);

	var wmsLayer = L.tileLayer.wms('http://localhost:8082/geoserver/sig/wms', {
	    layers: 'sig:bairros', transparent: 'true', format: 'image/png'
	}).addTo(mymap);



</script> """
print '</body>'
print '</html>'

conn.commit()
cursor.close()
conn.close()
