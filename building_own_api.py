from flask import Flask, jsonify, request
from flights_data import flights
from utils import search_flight, get_index

app = Flask(__name__)


# GETTING INFORMATION
# GET is used to request data from a specified resource.
# It is the default HTTP method so we don't specify it in these methods

@app.route('/')
def hello():
    return {'hello': 'Universe'}

# GET ALL FLIGHTS
@app.route('/flights')
def get_flights():
    # return jsonified flights data imported from flights_data
    return jsonify(flights)

# GET A FLIGHT BY ID
@app.route('/flights/<int:id>')
def get_flight_by_id(id):
    #set up a variable to store results and pass flight id and list of flights data to search_flights utility function
    flight_data = search_flight(id, flights)
    # return jsonified results
    return jsonify(flight_data)

# ADD NEW FLIGHT DATA
# POST is used to send data to a server to create/update a resource
@app.route('/flights', methods=['POST'])
def add_flight():
    # set up a variable to store JSON from request
    flight = request.get_json()
    # add this to our list of flights
    flights.append(flight)
    # return jsonified flights
    return jsonify(flights)

# UPDATE A FLIGHT
# PUT is used to create or update an existing resource
# The difference between PUT and POST is that PUT is 'idempotent'
# This just means PUT always returns the same result.
# Multiple PUT requests return the same result
# Mulitple POST requests create the same resource multiple times
@app.route('/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    # set variable flight_to_update to store update json data from request
    flight_to_update = request.get_json()
    # set variable to get index of flight with this ID in flights from get_index utility
    index = get_index(id, flights)
    # update flight data by setting flights[index] to update data
    flights[index] = flight_to_update

    # return jsonified updated flight data
    return jsonify(flights)


# DELETE FLIGHT
# DELETE method is used to delete a specified resource (but you guessed that, right?)
@app.route('/flights/<int:id>', methods=['DELETE'])
def delete_flight(id):
    # set variable to get index of flight with this ID in flights from get_index utility
    index = get_index(id, flights)
    # add safeguard - IGNORE FOR NOW
    # set variable to store flight from pop(index) on flights
    deleted_flight = flights.pop(index)
    # return jsonified deleted data OR the updated flight data now we've deleted one
    #return jsonify(deleted_flight)
    # OR
    return jsonify(flights)

if __name__ == '__main__':
    # what do I want to happen when this file runs?
    # I want to call the 'run' method on my Flask app
    # and I want it to do it in debug mode
    app.run(debug=True)
