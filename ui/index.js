var map = L.map('map');

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var filters = document.getElementById('filters');

var realtime = L.realtime({url: 'get_map_objects.json', type: 'json'}, {
  interval: 10 * 1000,
  style: function(feature) { return feature.properties; },
  pointToLayer: simplestyle,

  filter: function(feature) {
    if (!loaded) {
      return true;
    }

    var enabled = {};
    for (var i = 0; i < checkboxes.length; i++) {
      if (checkboxes[i].checked) {
        enabled[checkboxes[i].id] = true;
      }
    }
    return (feature.properties['marker-symbol'] in enabled);
  },
  onEachFeature: function (feature, layer) {
    layer.bindPopup(feature.properties.title);
  }
}).addTo(map);

var checkboxes = [];
var loaded = false;
realtime.on('update', function(updateEvent) {
  if(!loaded) {
    loaded = true;
    //Set the view after the first load
    map.fitBounds(realtime.getBounds(), {maxZoom: 16});

    var typesObj = {}, types = [];
    var features = updateEvent.features
    for (prop in features) {
      typesObj[features[prop].properties['marker-symbol']] = true;
    }
    for (var k in typesObj) types.push(k);

    for (var i = 0; i < types.length; i++) {
      var item = filters.appendChild(document.createElement('div'));
      var checkbox = item.appendChild(document.createElement('input'));
      var label = item.appendChild(document.createElement('label'));
      checkbox.type = 'checkbox';
      checkbox.id = types[i];
      checkbox.checked = true;
      label.innerHTML = types[i];
      label.setAttribute('for', types[i]);
      checkboxes.push(checkbox);
    }
  }
});

function simplestyle(f, latlon) {
    var sizes = {
      small: [20, 50],
      medium: [30, 70],
      large: [35, 90]
    };
    var fp = f.properties || {};
    var size = fp['marker-size'] || 'medium';
    var symbol = (fp['marker-symbol']) ? '-' + fp['marker-symbol'] : '';
    var color = fp['marker-color'] || '7e7e7e';
    color = color.replace('#', '');
    var url = 'http://a.tiles.mapbox.com/v3/marker/' +
          'pin-' +
          // Internet Explorer does not support the `size[0]` syntax.
          size.charAt(0) + symbol + '+' + color +
          ((window.devicePixelRatio === 2) ? '@2x' : '') +
          '.png';
    return new L.Marker(latlon, {
        icon: new L.icon({
            iconUrl: url,
            iconSize: sizes[size],
            iconAnchor: [sizes[size][0] / 2, sizes[size][1] / 2],
            popupAnchor: [sizes[size][0] / 2, 0]
        })
    });
}
