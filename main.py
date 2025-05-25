import ctypes

lib = ctypes.CDLL('./libcpmtool.so')
lib.Run()  # Запустит вашу функцию Run из Go
