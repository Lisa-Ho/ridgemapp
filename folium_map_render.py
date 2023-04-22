import folium
from folium.plugins import Draw

def render_interactive_map():    
    m = folium.Map()
    Draw(draw_options={
                "rectangle": True,
                "polyline": False, 
                "circle": False,
                "circlemarker": False,
                "marker":False,
                "polygon":False
            }).add_to(m)
    return m

#generate static map
def render_static_map():
    m = folium.Map(
               zoom_control=False,
               scrollWheelZoom=False,
               dragging=False)
    return m

#generate static map with selected polygon
def render_static_map_with_input(initial_map):
    m = folium.Map(location=[initial_map["center"]["lat"], initial_map["center"]["lng"]],
               zoom_start=initial_map["zoom"],
               zoom_control=False,
               scrollWheelZoom=False,
               dragging=False)
    folium.GeoJson(initial_map["last_active_drawing"]).add_to(m)
    return m