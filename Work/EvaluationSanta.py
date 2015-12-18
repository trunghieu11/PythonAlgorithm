north_pole = (90,0)
weight_limit = 1000
sleigh_weight = 10


import pandas as pd
import numpy as np
from haversine import haversine

def weighted_trip_length(stops, weights): 
    tuples = [tuple(x) for x in stops.values]
    # adding the last trip back to north pole, with just the sleigh weight
    tuples.append(north_pole)
    weights.append(sleigh_weight)
    
    dist = 0.0
    prev_stop = north_pole
    prev_weight = sum(weights)
    for location, weight in zip(tuples, weights):
        dist = dist + haversine(location, prev_stop) * prev_weight
        prev_stop = location
        prev_weight = prev_weight - weight
        writer.write("(" + str(location[0]) + " " + str(location[1]) + " " + str(weight) + ") ")
    return dist

def weighted_reindeer_weariness(all_trips):
    uniq_trips = all_trips.TripId.unique()
    
    if any(all_trips.groupby('TripId').Weight.sum() > weight_limit):
        raise Exception("One of the sleighs over weight limit!")
 
    dist = 0.0
    for t in uniq_trips:
        this_trip = all_trips[all_trips.TripId==t]
        curDist = weighted_trip_length(this_trip[['Latitude','Longitude']], this_trip.Weight.tolist())
        writer.write("," + str(curDist) + "\n")
        dist = dist + curDist
    writer.close()
    return dist    


writer = open('../input/total_distance.csv', 'w')
gifts = pd.read_csv('../input/gifts.csv')
sample_sub = pd.read_csv('../input/output.csv')

all_trips = sample_sub.merge(gifts, on='GiftId')

print("{:,}".format(weighted_reindeer_weariness(all_trips)))