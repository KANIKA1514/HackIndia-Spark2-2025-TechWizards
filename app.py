from flask import Flask, render_template, request
import geopy
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        start_location = request.form['start']
        end_location = request.form['end']

        geolocator = Nominatim(user_agent="flight_map")
        start_coords = geolocator.geocode(start_location)
        end_coords = geolocator.geocode(end_location)
        

        if start_coords and end_coords:
            start_lat = start_coords.latitude
            start_lon = start_coords.longitude
            end_lat = end_coords.latitude
            end_lon = end_coords.longitude

            # Return the coordinates to the template for the map
            return render_template('index.html', start_lat=start_lat, start_lon=start_lon,
                                   
            end_lat=end_lat, end_lon=end_lon, start_location=start_location, 
                                   end_location=end_location)

        else:
            return render_template('index.html', error="Invalid locations. Please try again.")
    
    return render_template('index.html')

if __name__== '_main_':
    app.run(debug=True)