import logging
class Filelog():
    def __int__(self):
        logging.basicConfig(filemode='logfile.txt',level=logging.WARNING)
        logging.info("hi")

if __name__=='__main__':
    obj=Filelog()