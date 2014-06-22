__author__ = 'root'

import os
import json
import __builtin__
import verinfo
from bcolors import bcolors
import sys
import time

__builtin__.va = __appname__
__builtin__.vv = __version__
__builtin__.vauth = __author__

bh = bcolors.HEADER
bf = bcolors.FAIL
be = bcolors.ENDC
bw = bcolors.WARNING
bo = bcolors.OKBLUE

class skerrorhandler():

	def __init__(self):
		pass

	def allserverfail(self,reporterror):
		print "\t[?] " +va+" v."+vv+" - CRASH in server_kicker.py during import of both server: " + \
		      bf + str(reporterror) + "\n" +be
		sys.exit(0)


class sferrorhandler():

	def __init__(self):
		pass

	def kbicatcher(self):
		pid = os.getpid()
		os.popen("iptables -t nat -F")
		print bo+"\t[!] User initialized exit - flushed IPTABLES and killed server pid " + \
		      bf + str(pid)+" ...\n" + be
		killer = "kill -9 "+str(pid)
		os.popen(killer)
		sys.exit(0)

	def sfbothfail(self,reporterror):
		print bo+"\t[?] " +va+" v."+vv+" - CRASH in server_func.py during import of both servers: " + \
		      bf + str(reporterror) + "\n" +be
		sys.exit(0)

	def sftcpfail(self,reporterror):
		print bo+"\t[?] " +va+" v."+vv+" - CRASHED during import of tcp server: " + \
		      bf + str(reporterror) + "\n" +be
		sys.exit(0)

	def sfudpfail(self,reporterror):
		print bo+"\t[?] " +va+" v."+vv+" - CRASHED during import of udp servers: " + \
		      bf + str(reporterror) + "\n" +be
		sys.exit(0)

class logenablehandler():

	def __init__(self):
		pass

	def logimportfail(self,reporterror):
		print bo+"\t[?] " +va+" v."+vv+" - " + str(logtype).upper() + " CRASHED due to: " + \
		      bf + str(reporterror) + "\n" +be
		sys.exit(0)

class contamloghandler():

	def __init__(self):
		pass

	def jsonreadfail(self,reporterror):
		print bo+"\t[?] " +va+" v."+vv+" - CRASHED Couldn\'t read from file: Contaminated_log-"+str(date)+".json : " + \
		      bf + str(reporterror) + "\n" +be

	def jsonrwritefail(self,reporterror):
		print bo+"\t[?] " +va+" v."+vv+" - CRASHED Couldn\'t write to file: Contaminated_log-"+str(date)+".json : " + \
		      bf + str(reporterror) + "\n" +be

	def jsonrkeepfail(self,reporterror):
		print bo+"\t[?] " +va+" v."+vv+" - CRASHED Couldn't properly format: Contaminated_log-"+str(date)+".json : " + \
		      bf + str(reporterror) + "\n" +be



