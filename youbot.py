#!/usr/bin/env python3

# Copyright © Moch Aang Ardiansyah XD. | Open source 
# Tools ini digunakan untuk mendownload/mengunduh video YouTube

import os, pytube
from pytube import YouTube

peler = "/sdcard/YouBot"

class YouBot():
	
	def Input(self):
		os.system("clear")
		link = input("Masukan link : ")
		self.Convert(link, peler)
		
	def Convert(self, kontol, peler):
		yt = YouTube(kontol)
		stream = yt.streams.get_highest_resolution()
		stream.download(peler)
		print("\n\n[√] Berhasil mendownload!")
		print(f"[•] Video tersimpan di : {peler}")
	
YouBot().Input()