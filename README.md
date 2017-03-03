BT Graduate Coding Test 2016/2017
======

Information
------

The following script will print routers matching the specified requirements outlined in the coding test brief.

To run the script, navigate into the src directory and run the following command: 
'''
python router_test.py ../test.csv -o 12
'''

A test CSV file has been provided. The script has the capability of handling a specified delimiter and OS version. The script will also ignore invalid CSV entries, such as: blank lines, invalid IPs, an invalid number of fields, duplicated host names, invalid OS versions and invalid patched fields.

For more information, the following command line argument will provide detailed help information.

'''
python router_test.py -h 
'''


