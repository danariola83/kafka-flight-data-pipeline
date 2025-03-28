from country_bounding_boxes import country_bounding_boxes

def get_min_bbox(country):
    country = country.title()

    country_bbox_list = []

    for country_tuple in country_bounding_boxes.values():
        country_bbox_list.append(country_tuple[0])

    if country in country_bbox_list:
        country_index = country_bbox_list.index(country)
        
        lon_min = list(country_bounding_boxes.values())[country_index][1][0]
        lat_min = list(country_bounding_boxes.values())[country_index][1][1]

        return lon_min, lat_min
    else:
        print(f"{country} not in bounding box dict")
        return None
    
def get_max_bbox(country):
    country = country.title()

    country_bbox_list = []

    for country_tuple in country_bounding_boxes.values():
        country_bbox_list.append(country_tuple[0])

    if country in country_bbox_list:
        country_index = country_bbox_list.index(country)
        
        lon_min = list(country_bounding_boxes.values())[country_index][1][2]
        lat_min = list(country_bounding_boxes.values())[country_index][1][3]

        return lon_min, lat_min
    else:
        print(f"{country} not in bounding box dict")
        return None
