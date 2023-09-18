"""
This will import all modules with name tweetN.py (1 <= N <= 50)
and print the result of the corresponding tweet() function
implemented in tweetN.py.
"""

for i in range(1, 51):
    module_name = "tweet{}".format(i)
    try:
        module = __import__(module_name)
        print("tweet {0} says: {1}".format(i, module.tweet()))
    except ImportError:
        pass
