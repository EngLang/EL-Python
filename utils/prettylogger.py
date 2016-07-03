# Functions to do colorful log printing in the terminal

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class plogger(object):
    
    @staticmethod
    def warn(message):
        print(bcolors.WARNING + message + bcolors.ENDC)
        
    @staticmethod
    def head(message):
        print(bcolors.HEADER + message + bcolors.ENDC)
        
    @staticmethod
    def okblue(message):
        print(bcolors.OKBLUE + message + bcolors.ENDC)
        
    @staticmethod
    def okgreen(message):
        print(bcolors.OKGREEN + message + bcolors.ENDC)
        
    @staticmethod
    def fail(message):
        print(bcolors.FAIL + message + bcolors.ENDC)
        
    @staticmethod
    def bold(message):
        print(bcolors.BOLD + message + bcolors.ENDC)
        
    @staticmethod
    def underline(message):
        print(bcolors.UNDERLINE + message + bcolors.ENDC)