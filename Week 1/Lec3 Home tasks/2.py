"""
1. A GPS navigation system stores a flight route as a nested tuple of checkpoints, where each checkpoint is (checkpoint_id, latitude, longitude, elevation_meters):
waypoints = ((101, 31.5204, 74.3587, 217), (102, 31.5500, 74.3800, 225), (103, 31.5800, 74.4100, 210), (104, 31.6100, 74.4400, 240))

Perform the following tasks:
- Unpack the first waypoint and the last waypoint to extract their checkpoint IDs and elevations.
- Extract the intermediate waypoints (excluding first and last) using slicing with stride step, and reverse them using slicing [::-1].
- Convert the 2nd waypoint into a list to update its elevation to 230 meters, convert it back to a tuple, and construct a new updated 'waypoints' tuple.
- Extract all 4 elevation values into a single tuple 'elevations' using indexing and tuple concatenation.
- Calculate and display the maximum elevation, starting elevation, elevation gain from start to peak, and average route elevation using an f-string.
"""

waypoints = (
    (101, 31.5204, 74.3587, 217),
    (102, 31.5500, 74.3800, 225),
    (103, 31.5800, 74.4100, 210),
    (104, 31.6100, 74.4400, 240)
)

start_id, start_lat, start_lon, start_elevation = waypoints[0]
end_id, end_lat, end_lon, end_elevation = waypoints[-1]
print(f"Start Waypoint #{start_id} at elevation: {start_elevation}m")
print(f"End Waypoint #{end_id} at elevation: {end_elevation}m")

intermediate_waypoints = waypoints[1:-1]
reversed_intermediate = intermediate_waypoints[::-1]
print(f"Intermediate Waypoints Reversed: {reversed_intermediate}")

wp2_list = list(waypoints[1])
wp2_list[3] = 230
wp2_modified = tuple(wp2_list)

updated_waypoints = (waypoints[0], wp2_modified) + waypoints[2:]
print(f"Updated Waypoints Tuple: {updated_waypoints}")

elevations = (
    updated_waypoints[0][3],
    updated_waypoints[1][3],
    updated_waypoints[2][3],
    updated_waypoints[3][3]
)
print(f"Elevations Tuple: {elevations}")

peak_elevation = max(elevations)
elevation_gain = peak_elevation - start_elevation
average_elevation = sum(elevations) / len(elevations)

print(f"Route Elevation Summary -> Peak: {peak_elevation}m, Elevation Gain: {elevation_gain}m, Average: {average_elevation:.2f}m")
