import ctypes
lib = ctypes.CDLL('./helpLib.dll')
try:
    lib.Run()
except:
    print("Ups...")
