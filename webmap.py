import folium

# Create a map centered at a specific location
map = folium.Map(location=[37.7749, -122.4194], zoom_start=5)

# Add markers
locations = [
    {"name": "San Francisco", "coords": [37.7749, -122.4194]},
    {"name": "Los Angeles", "coords": [34.0522, -118.2437]},
    {"name": "New York", "coords": [40.7128, -74.0060]}
]

for loc in locations:
    folium.Marker(
        location=loc["coords"],
        popup=loc["name"],
        icon=folium.Icon(color="green", icon="cloud")
    ).add_to(map)

# Add a circle
folium.Circle(
    radius=1000,
    location=[37.7749, -122.4194],
    popup="San Francisco",
    color="crimson",
    fill=True,
    fill_color="crimson"
).add_to(map)

# Save the map
map.save("web_map.html")
print("Web map saved as 'web_map.html'.")
