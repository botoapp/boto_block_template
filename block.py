def block(parameters=None, completed_nodes=None, last_run=None, app_auth=None, test=False, above_limit=False):
    """
    Arguments:
        parameters: 
        completed_nodes:
        last_run:
        app_auth:
        test:
        above_limit:
    Returns:
        A dictionary with:
    Raises:
        Nothing intentional.
    """
    # Write some defaults for the incoming arguments
    parameters = {} if parameters is None else parameters
    completed_nodes = {} if completed_nodes is None else completed_nodes
    last_run = {} if last_run is None else last_run
    app_auth = [] if app_auth is None else app_auth


    response = {
        'status' : '',
        'message' : '',
        'offset' : '',
        'condition' : '',
        'action' : 0,
        'data': {},
        'data_type': 'single',
        'parameters': parameters
    }
    return response
