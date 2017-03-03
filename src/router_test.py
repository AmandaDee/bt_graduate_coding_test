#!/usr/bin/python
'''
Created on Mar 2, 2017
@author: Amanda Bamford
'''
# Check python version and try to import python libraries
import sys
if sys.version_info < (2,6):
        print("Must use python version 2.6.x or greater")
        sys.exit(1)
else:
    try:
        from Router import *
        import re, subprocess, os, glob, sys, argparse, socket
    except ImportError as error:
        print '>> Import Error. %s' % (str(error))
        sys.exit()

# Reads a specified file and generates a list of valid Router objects
def read_file(file_path, delimiter):
	router_objs =[]
	try:
		# Opens the file for reading
		with open(file_path, 'r') as file:
			for line in file:
				if not line:
					continue
				router_info_list = line.split(delimiter)
				if len(router_info_list) == 5:
						router_objs.append(Router(router_info_list))
			return router_objs
	except IOError:
		print '>> File not found'
    	sys.exit()

# Prints routers in a valid format if it has not been patched
# and the os version is greater than the specified os version.
def print_routers(router_objs, os):
	for router in router_objs:
		count = 0
		current_ip = router.ipAddress
		current_hostname = router.hostname
		if router.patched == 'no' and router.osVersion >= os:
			for routerCheck in router_objs:
				if routerCheck.ipAddress == router.ipAddress or routerCheck.hostname == router.hostname:
					count += 1
			if count == 1: 
				if validation(router): print router.toString()
			count = 0



# Checks router fields are valid
def validation(router):
	if isNull(router.hostname):
		return False
	elif isNull(router.ipAddress) or not ip_validation(router.ipAddress):
		return False
	elif isNull(router.patched) or not patched_validation(router.patched):
		return False
	elif isNull(router.osVersion):
		return False
	else:
		return True


# Returns true if an empty value is provided.
def isNull(value):
	return True if value == None or value =='' else False

# Returns true if a valid IPV4 or IPV6 adress is provided
def ip_validation(ipAddress):
	try:
		socket.inet_pton(socket.AF_INET, ipAddress)
		return True
	except socket.error:
		try:
			socket.inet_pton(socket.AF_INET6, ipAddress)
			return True
		except socket.error:
			return False

# Returns true if a patch value of 'yes' or 'no' is provided, this is not case sensitive.
def patched_validation(patched):
	return True if patched.lower() == "yes" or patched.lower() == "no" else False


def main():
	directory = delimiter = ''
	os = 0

	parser = argparse.ArgumentParser(description='Router patch check')
	# Required arguments
	parser.add_argument(
	  'directory',  help='The directory path of the CSV file containing router information.')
	parser.add_argument(
	  '-o', '--operating_system', required=True, 
	  default='12',
	  help='The minimun operating system version to be patched. This is 12 by default. For exmple: patchTest.py filename.csv -o 14. ')
	# Optional arguments
	parser.add_argument(
	  '-d', '--delimiter', required=False, 
	  default=',',
	  help='The delimiter seperating values, to be used for file formats other than CSV. This must be a unique identifier. This is , by default')


	args = parser.parse_args()
	directory = args.directory
	os = args.operating_system
	delimiter = args.delimiter if args.delimiter !='' else ','

	print_routers(read_file(directory, delimiter), os)


# To call main method..
if  __name__ == '__main__':
  main()