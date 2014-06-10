import abc

class AbstractController(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        # constructor
        return

    @abc.abstractmethod
    def doControl(self):
        #performs Control algorithm, likely will be broken into lots of small steps
        return

    @abc.abstractmethod
    def setDesired(self):
        #sets the desired value of this controller
        return

    @abc.abstractmethod
    def landing():
        #performs the land command
        return
    
    @abc.abstractmethod
    def flying(self):
        #performs the fly command
        return
    
    @abc.abstractmethod
    def killing(self):
        #performs the kill command
        return
    
    def __str__(self):
        return 'This is a controller'


class PID( AbstractController ):

    def __init__(self):
        print 'PID Constructor'

    def __str__(self):
        return 'This is a PID Controller'

    def doControl(self):
        print 'doing PID'

    def setDesired(self):
        print 'set PID Desired'

    def flying(self):
        print 'flying PID'

    def landing(self):
        print 'landing PID'

    def killing(self):
        print 'killing PID'

class LQR( AbstractController ):

    def __init__(self):
        print 'LQR consctructor'

    def __str__(self):
        return 'This is a LQR Controller'

    def doControl(self):
        print 'doing LQR'

    def setDesired(self):
        print 'setting LQR desired'

    def flying(self):
        print 'flying LQR'

    def landing(self):
        print 'landing LQR'

    def killing(self):
        print 'killing LQR'

class SMC( AbstractController ):

    def __init__(self):
        print 'SMC constructor'

    def __str__(self):
        return 'This is a LQR Controller'

    def doControl(self):
        print 'doing SMC'

    def setDesired(self):
        print 'setting SMC desired'

    def flying(self):
        print 'flying SMC'

    def landing(self):
        print 'landing SMC'

    def killing(self):
        print 'killing SMC'

class HInfinity( AbstractController ):

    def __init__(self):
        print 'H Infinity constructor'

    def __str__(self):
        return 'This is an H Infinity Controller'

    def doControl(self):
        print 'doing H infinity'

    def setDesired(self):
        print 'setting HI desired'

    def flying(self):
        print 'flying H infinity'

    def landing(self):
        print 'landing H infinity'

    def killing(self):
        print 'killing H infinity'
