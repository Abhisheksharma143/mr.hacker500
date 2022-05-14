import os, sys
try:
    __import__("abhi").Main()
except Exception as e:
    exit(str(e))