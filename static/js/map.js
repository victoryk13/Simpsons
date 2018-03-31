
var myMap = L.map("locationMap", {
    center: [37.09, -95.71],
    zoom: 5
  });

L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
"access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ." +
"T6YbdDixkOBWH_k9GbS8JQ").addTo(myMap);


for (var i =0; i < mapData.length; i++) {
    var place = mapData[i];
    var popupText = "<h1>Episodes</h1><hr>";

    if (place.visits.length > 1) {
        
        for (var j=0; j<place.visits.length;j++){
            popupText = popupText+"<h2>"+place.visits[j].title+"</h2><br><h3>Season: "+place.visits[j].season+"<br>Episode: "+place.visits[j].episode+"<br>";
        }
    } 
    else {
        popupText - popupText + "<h2>"+place.visits[0].title+"</h2><br><h3>Season: "+place.visits[0].season+"<br>Episode: "+place.visits[0].episode+"<br>";

    }    

    L.marker(place.coordinates,{
        title: place.location
    }).addTo(myMap).bindPopup(popupText);
}