import os

ping = "ping -c 5 api.github.com"
one_ping = os.system(ping)  # returns the exit code in unix


