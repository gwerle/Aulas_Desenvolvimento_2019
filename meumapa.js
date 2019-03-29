window.onload = function() {
var mapa = L.map('meumapa').setView([-25.45, -49.27], 12)
var osm = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(mapa);
var mapbox = L.tileLayer(
  'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}',
  {
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1Ijoic2NhbWJvaW0iLCJhIjoiY2pmMnJiYXduMWZlaTMzb2h0OHZnb2p5MyJ9.KS6DEMGACVV6xK7-XqxTeA',
  }
).addTo(mapa);
//ponto
var poligono = L.polygon([
[-25.45, -49.22],
[-25.48, -49.71],
[-25.59, -49.51],
[-25.66, -49.36]
])//.addTo(mapa);

var circulo = L.circle(
[-25.50, -49.46],
{
color: '#ff33cc',
fillColor: '#ff33cc',
fillOpacity: 0.2,
radius: 20000
}
)//.addTo(mapa);
//Pontos
var ponto1 = L.marker([-25.50, -49.21]);
    ponto2 = L.marker([-25.43, -49.50]);

//Linhas
var linha1 = L.polyline([[-25.45, -49.25], [-25.55, -49.15]]);
    linha2 = L.polyline([[-25.45, -49.15], [-25.55, -49.25]]);


var mun =  L.tileLayer.wms("http://localhost:8082/geoserver/sig/wms", {
layers: "sig:bairros",
transparent: "true",
format: "image/png"
})//.addTo(mapa);

var popup = L.popup()
.setLatLng([-25.44, -49.51])
.setContent('Eu sou uma popup!')
.openOn(mapa);


var pontos = L.layerGroup([ponto1, ponto2]);
var linhas = L.layerGroup([linha1, linha2]);
var desenhos = L.layerGroup([pontos, linhas, circulo, poligono]).addTo(mapa);

var baseCartografica = {
"OpenStreetMap": osm,
"Mapbox Streets": mapbox

}
//Mapas de sobreposiçao
var informacaoTematica = {
"Desenhos": desenhos,
"Geoserver": mun

}
//Adicionar objetos ao controle de camadas
L.control.layers(baseCartografica, informacaoTematica).addTo(mapa);
L.control.scale({position: 'bottomleft', imperial: 'false'}).addTo(mapa);
}
