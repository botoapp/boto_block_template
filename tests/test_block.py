from block import block

def test_block():
    assert block() == {
        'status' : '',
        'message' : '',
        'offset' : '',
        'condition' : '',
        'action' : 0,
        'data': {},
        'data_type': 'single',
        'parameters': {}
    }
