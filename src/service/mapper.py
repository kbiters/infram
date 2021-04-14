def mapping(route_map, data_map):
    """
    Function to perform mapping, receiving by parameter the path of the map
    dictionary and the option that is chosen, then if the option is not 'None'
    we return the value corresponding to the map with the chosen option.
    """
    try:
        assert data_map is not None
        return route_map.get(data_map, )
    except OSError as error:
        print(error)
