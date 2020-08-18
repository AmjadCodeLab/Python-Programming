import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
logging.info("A new request came")
try:
    x=int(input("Enter Number1 :: "))
    y=int(input("Enter Number2 :: "))
    print(x/y)
except ZeroDivisionError as msg:
    print("Zero Cannot Be Divided")
    logging.warning("My message is warnning")
    logging.critical("My message is Critical")
    logging.exception(msg)
except ValueError as msg:
    print("Enter Only Int Value")
    logging.exception(msg)
    logging.error("My message is error")

logging.info("Reguest Processing Completed in Text File")


