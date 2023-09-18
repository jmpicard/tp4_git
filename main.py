"""
This will import all modules with name annonceN.py (1 <= N <= 50)
and print the result of the corresponding annonce() function
implemented in annonceN.py.
"""

for i in range(1, 51):
    module_name = "annonce{}".format(i)
    try:
        module = __import__(module_name)
        print("annonce {0}: {1}".format(i, module.annonce()))
    except ImportError:
        pass
