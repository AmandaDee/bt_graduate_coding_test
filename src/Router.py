#!/usr/bin/python
'''
Created on Mar 2, 2017
@author Amanda Bamford
'''

class Router:
	hostname = ipAddress = patched = osVersion = notes = ''

	def __init__(self, hostname, ipAddress, patched, osVersion, notes):
		self.hostname = hostname.lower().strip()
		self.ipAddress = ipAddress.strip()
		self.patched = patched.lower().strip()
		self.osVersion = osVersion.strip()
		self.notes = notes.strip('\n')

	def __init__(self, infoList):
		self.hostname = infoList[0].lower().strip()
		self.ipAddress = infoList[1].strip()
		self.patched = infoList[2].lower().strip()
		self.osVersion = infoList[3].strip()
		self.notes = infoList[4].strip('\n')

	def toString(self):
		output = '%s (%s) OS version %s %s' % (self.hostname, self.ipAddress, self.osVersion, '[%s]' % self.notes if self.notes !='' else '' ) 
		return output

