import React, { Component } from "react";
import 'leaflet/dist/leaflet.css';
import Dashboard from "./Dashboard/Dashboard"

class App extends Component {


  state = {
     lat: 51.505,
     lng: -0.09,
     zoom: 11
   };

   render() {
       const position = [this.state.lat,this.state.lng]
        return (
          <>
            <Dashboard />
          </>
     )
 }
}

export default App;

