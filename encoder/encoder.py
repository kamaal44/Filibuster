#!/usr/bin/python2
# encoding: utf-8
#
# module author: subinacls
#


import base64 as b64
import __builtin__
from itertools import cycle, izip
import lzma
import binascii

class clientencoder(object):


	def __init__(self):
		pass

	def dataencode(self, ident):
		if encodedata == "base85":
			__builtin__.ident = b64.b85encode(ident)
		if encodedata == "base64":
			__builtin__.ident = b64.b64encode(ident)
		if encodedata == "base32":
			__builtin__.ident = b64.b32encode(ident)
		if encodedata == "base16":
			__builtin__.ident = b64.b16encode(ident)
		if encodedata == "rot13":
			__builtin__.ident = str(ident).encode('rot13')
		if encodedata == "xor":
			key = 'filterbuster'
			__builtin__.ident = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(ident, cycle(key)))
		if encodedata == "url":
			pass  # do url
		if encodedata == "lzma":
			__builtin__.ident = lzma.compress(ident)
		if encodedata in ["gz", "gzip", "zlib"]:
			__builtin__.ident = ident.encode("zlib")
		if encodedata in ["binary", "bytestring"]:
			__builtin__.ident = binascii.b2a_uu(ident)
		if encodedata in ["plain", "plaintext", "cleartext", "clear"]:
			pass  # do gzip


	def datadecode(self, ddata):
		if str(proto).lower() == "udp":
			if encodedata == "base85":
				__builtin__.data = b64.b85decode(ddata[0])
			if encodedata == "base64":
				__builtin__.data = b64.b64decode(ddata[0])
			if encodedata == "base32":
				__builtin__.data = b64.b32decode(ddata[0])
			if encodedata == "base16":
				__builtin__.data = b64.b16decode(ddata[0])
			if encodedata == "rot13":
				__builtin__.data = str(ddata[0]).decode('rot13')
			if encodedata == "xor":
				key = 'filterbuster'
				__builtin__.data = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(ddata[0], cycle(key)))
			if encodedata == "url":
				pass  # do url
			if encodedata == "lzma":
				__builtin__.data = lzma.decompress(ddata)
			if encodedata in ["gz", "gzip", "zlib"]:
				__builtin__.data = ddata.encode("zlib")
			if encodedata in ["binary", "bytestring"]:
				__builtin__.data = binascii.a2b_uu(ddata)
			if encodedata in ["plain", "plaintext", "cleartext", "clear"]:
				__builtin__.data = ddata[0]

		if str(proto).lower() == "tcp":
			if encodedata == "base85":
				__builtin__.data = b64.b85decode(ddata)
			if encodedata == "base64":
				__builtin__.data = b64.b64decode(ddata)
			if encodedata == "base32":
				__builtin__.data = b64.b32decode(ddata)
			if encodedata == "base16":
				__builtin__.data = b64.b16decode(ddata)
			if encodedata == "rot13":
				__builtin__.data = str(ddata).decode('rot13')
			if encodedata == "xor":
				key = 'filterbuster'
				__builtin__.data = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(ddata, cycle(key)))
			if encodedata == "url":
				pass  # do url
			if encodedata == "lzma":
				__builtin__.data = lzma.decompress(ddata)
			if encodedata in ["gz", "gzip", "zlib"]:
				__builtin__.data = ddata.encode("zlib")
			if encodedata in ["binary", "bytestring"]:
				__builtin__.data = binascii.a2b_uu(ddata)
			if encodedata in ["plain", "plaintext", "cleartext", "clear"]:
				__builtin__.data = ddata

		return ddata