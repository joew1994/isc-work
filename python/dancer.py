import sys
from dancing.dance import boogie
moves = sys.argv[1:]
boogie(moves)

#sys.argv allows us to add arguments = if we put in dance moves it will feed them through to 'damce.py' because we have imported boogie from there into this script (dancer.py). It will input the arguments into the brackets of the defined function in this case def boogie()
