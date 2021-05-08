def mapping(route_map, data_map):
    try:
        assert data_map is not None
        return route_map.get(data_map, )
    except OSError as error:
        print(error)
