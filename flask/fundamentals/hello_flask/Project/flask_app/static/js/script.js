function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
            
    }
    }
    
    function showPosition(position) {
    var x = document.getElementById("longitude")
    x.value = position.coords.longitude
    var y = document.getElementById("latitude")
    y.value = position.coords.latitude
    var mapProp= {
    center:new google.maps.LatLng(position.coords.latitude, position.coords.longitude),
    
    zoom:15,
};
var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
}
