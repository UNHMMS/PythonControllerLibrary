import abc
import numpy as np

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

    @abc.abstractmethod
    def setMinOut(self):
        #sets the minimum output of the controller
        return

    @abc.abstractmethod
    def setMaxOut(self):
        #sets the maximum output of the controller
        return
    
    def __str__(self):
        return 'This is a controller'


class PID( AbstractController ):
    
    def __init__(self, kp, ki, kd, desired, minout, maxout):
        self.kp = float(kp)
        self.ki = float(ki)
        self.kd = float(kd)
        self.desired = float( desired )
        self.minout = minout
        self.maxout = maxout
        self.rollingSum = 0.0
        self.lastVal = 0.0

    def __str__(self):
        string = 'PID Controller:\n'
        string += 'P Gain : ' + str(self.kp) + '\n'
        string += 'I Gain : ' + str(self.ki) + '\n'
        string += 'D Gain : ' + str(self.kd) + '\n'
        string += 'Desired: ' + str(self.desired) + '\n'
        string += 'MaxOut : ' + str(self.maxout) + '\n'
        string += 'MinOut : ' + str(self.minout) + '\n'
        return string

    def doControl(self, current):
        #calculate error
        error = desired - current

        #calculate rolling sum 
        self.rollingSum += error * self.ki

        #calculate D term
        dTerm = self.kd * ( current - self.lastVal )

        #calculate final output
        output = (self.ki * error) + self.rollingSum + dTerm

        #reset the last value for the next iteration
        self.lastVal = current

        #make sure the value if within the specified range
        if output > self.maxout:
            output = self.maxout

        if output < self.minout:
            output = self.minout

        #and return the calculated value
        return output
    
    def setDesired(self, newdesired):
        self.desired = newdesired

    def setMinOut(self, newmin):
        self.minout = newmin

    def setMaxOut(self, newmax):
        self.maxout = maxout

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

    def setDesired(self, newdesired):
        self.desired = newdesired

    def setMinOut(self, newmin):
        self.minout = newmin

    def setMaxOut(self, newmax):
        self.maxout = maxout

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
        return 'This is a SMC Controller'

    def doControl(self):
        print 'doing SMC'

    def setDesired(self, newdesired):
        self.desired = newdesired

    def setMinOut(self, newmin):
        self.minout = newmin

    def setMaxOut(self, newmax):
        self.maxout = maxout

    def flying(self):
        print 'flying SMC'

    def landing(self):
        print 'landing SMC'

    def killing(self):
        print 'killing SMC'


#Unimplemented because I don't know how to implement it yet
class HInfinity( AbstractController ):

    def __init__(self):
        print 'H Infinity constructor'

    def __str__(self):
        return 'This is an H Infinity Controller'

    def doControl(self):
        print 'doing H infinity'

    def setDesired(self, newdesired):
        self.desired = newdesired

    def setMinOut(self, newmin):
        self.minout = newmin

    def setMaxOut(self, newmax):
        self.maxout = maxout

    def flying(self):
        print 'flying H infinity'

    def landing(self):
        print 'landing H infinity'

    def killing(self):
        print 'killing H infinity'
