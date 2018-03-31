var myMap = L.map("locationMap", {
    center: [12, -15],
    zoom: 2
  });

L.tileLayer(
    "https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
    "access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ." +
    "T6YbdDixkOBWH_k9GbS8JQ"
).addTo(myMap);

console.log(mapData)
for (var i =0; i < mapData.length; i++) {
    var place = mapData[i];
    var popupText = "<h3>"+place.location+"</h3><hr>";

    for (var j=0; j<place.visits.length;j++){
        popupText = popupText+"<h4 id='mapHeaders'>"+place.visits[j].title+"</h4><h4 id='mapText'>Season: "+place.visits[j].season+"<br>Episode: "+place.visits[j].episode+"</h4><br>";
    }

    var marker = L.marker(place.coordinates,{
        title: place.location
    }).addTo(myMap).bindPopup(popupText);
}