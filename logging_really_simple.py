import logging
logging.basicConfig(level=logging.DEBUG)

for i in range(10):
    print(i)

logging.info("starting program")
logging.warning("Ouch!")
logging.debug('a')
logging.debug('b')
logging.debug('c')

print("platypus")
logging.error("My hair is on fire!")
logging.info("ending program")
