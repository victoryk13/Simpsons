var myMap = L.map("locationMap", {
    center: [40.42, -3.70],
    zoom: 2
  });

L.tileLayer(
    "https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
    "access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ." +
    "T6YbdDixkOBWH_k9GbS8JQ"
).addTo(myMap);


for (var i =0; i < mapData.length; i++) {
    var place = mapData[i];
    var popupText = "<h1>Episodes</h1><hr>";

    for (var j=0; j<place.visits.length;j++){
        popupText = popupText+"<h2>"+place.visits[j].title+"</h2><br><h3>Season: "+place.visits[j].season+"<br>Episode: "+place.visits[j].episode+"</h3><br><br>";
    }

    var marker = L.marker(place.coordinates,{
        title: place.location
    }).addTo(myMap).bindPopup(popupText);
}