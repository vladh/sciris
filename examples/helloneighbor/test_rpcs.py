"""
test_rpcs.py -- A testing file for installing RPCs outside of the caller of
    scirisapp.py
    
Last update: 5/23/18 (gchadder3)
"""

# Imports
from sciris2gc.rpcs import make_register_RPC
import sciris2gc.datastore as ds
import uuid
#import pandas as pd
#from pylab import figure
#import mpld3
#import model
#import os
#from sciris2gc import fileio

#
# Globals
#

# Dictionary to hold all of the registered RPCs in this module.
RPC_dict = {}

# RPC registration decorator factory created using call to make_register_RPC().
register_RPC = make_register_RPC(RPC_dict)

#
# RPC functions
#
    
@register_RPC(override=True)  # Override any other test_func() defined before
def test_func():
    # Create a test dict.
    test_dict = { 'optima': 'developer', 'sciris': 'product' }
    
    # Add the test_dict object to the DataStore.
    new_uid = ds.data_store.add(test_dict, instance_label='testdict')
    
    return '<h1>test_dict added to database with UID %s</h1>' % new_uid.hex

@register_RPC()
def test_func2():
    test_dict_uid = ds.data_store.get_uid_from_instance('obj', 'testdict')
    if test_dict_uid is not None:
        test_dict = ds.data_store.retrieve(test_dict_uid)
        
        print('here be the test_dict:')
        print test_dict
        
        ds.data_store.delete(test_dict_uid)
        
        return '<h1>test_dict removed from database</h1>'
    else:
        return '<h1>test_dict not in database</h1>'
    
@register_RPC()
def test_func3():
    return '<h1>Test Me Testily!</h1>'

#@register_RPC(call_type='upload')
#def show_csv_file(full_file_name):
##    x = 1 / 0  # uncomment to test exceptions with ZeroDivisionError
##    return {'error': 'show_csv_file() just does not feel like working.'}  # uncomment to test custom error
#
#    # Extract the data from the .csv file.
#    df = pd.read_csv(full_file_name)
#    
#    # Create the figure from the data.
#    new_graph = figure()
#    ax = new_graph.add_subplot(111)
#    ax.scatter(df.x, df.y)
#    
#    # Convert the figure to a JSON-able dict.
#    graph_dict = mpld3.fig_to_dict(new_graph)
#    
#    # Return the dict.
#    return graph_dict
#
#@register_RPC(call_type='download')
#def download_graph_png():
##    x = 1 / 0  # uncomment to test exceptions with ZeroDivisionError
##    return {'error': 'download_graph_png() just does not feel like working.'}  # uncomment to test custom error
#    
#    # Make a new graph with random data.
#    new_graph = model.makegraph()
#    
#    # Save a .png file of this graph.
#    full_file_name = '%s%sgraph.png' % (fileio.downloads_dir.dir_path, os.sep)
#    new_graph.savefig(full_file_name)
#    
#    # Return the full filename.
#    return full_file_name