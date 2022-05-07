import React, { Component } from "react";
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import Leaflet from 'leaflet';
import 'leaflet/dist/leaflet.css';

Leaflet.Icon.Default.imagePath =
'../node_modules/leaflet'

delete Leaflet.Icon.Default.prototype._getIconUrl;

Leaflet.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

class Map extends Component {


  state = {
     lat: 51.505,
     lng: -0.09,
     zoom: 11
   };

   render() {
       const position = [this.state.lat,this.state.lng]
        return (
          <>
            <MapContainer style={{ height: "80vh" }} center={position} zoom={this.state.zoom}  scrollWheelZoom={false}>
              <TileLayer
                    attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a>  contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              />
              <Marker position={position}>
              </Marker>
            </MapContainer >
          </>
     )
 }
}

export default Map;