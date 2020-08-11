import ctypes
import time

time.sleep(5)
ctypes.windll.user32.MessageBoxW(0, "Testing yeah media", "Title", 0)