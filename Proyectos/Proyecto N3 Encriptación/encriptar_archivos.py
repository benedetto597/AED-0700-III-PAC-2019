# *-* coding: utf-8 -*-

from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
from time import time 
import sys


class encriptar_archivos():

	key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'	
	def pad(self, s):
		return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

	def encrypt(self, message, key, key_size=256):
		message = self.pad(message)
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(key, AES.MODE_CBC, iv)
		return iv + cipher.encrypt(message)


	def encrypt_file(self, file, ruta):
		self.dirs = file
		self.dirr = self.dirs.split(' ')
		self.val = len(self.dirr)-1
		self.tiempo_inicial = time()
		for j in self.dirr:
			for i in range(0,len(self.dirr)-self.val):
				filename = [j]
				dirname = os.path.dirname(filename[i])
				f = open(filename[i], 'r')
				f.name
				nombre = os.path.basename(f.name)
				nombre_fichero = os.path.join(os.sep, ruta, nombre)			
				if not os.path.exists(dirname):
		   			os.makedirs(dirname)
				with f as fo:
					plaintext = fo.read()
				enc = self.encrypt(plaintext, self.key)
				with open(nombre_fichero + ".enc", 'wb') as fo:
					fo.write(enc)
		self.tiempo_final = time()
		#medir tiempo de encriptacion de archivos
		self.tiempo_ejecucion = str(self.tiempo_final - self.tiempo_inicial)	
		#creando archivo.txt que guarda el tiempo de ejecucion.
		t = open("log_encrypt_files.txt", 'w')
		t.write("El tiempo en encriptar los archivos fue de: "+self.tiempo_ejecucion+ " segundos")
		t.close()

