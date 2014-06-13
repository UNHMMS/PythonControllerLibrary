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
    def setMinOut(self):
        #sets the minimum output of the controller
        return

    @abc.abstractmethod
    def setMaxOut(self):
        #sets the maximum output of the controller
        return

    @abc.abstractmethod
    def setGains(self):
        #change the gains of the controller
        return
    
    def __str__(self):
        return 'This is a controller'

#classic PID library, one of the most popular control schemes
class PID( AbstractController ):

    #takes initial gains, desired value, and min and max output
    def __init__(self, kp, ki, kd, desired, minout, maxout):
        self.kp = float(kp)
        self.ki = float(ki)
        self.kd = float(kd)
        self.desired = float( desired )
        self.minout = minout
        self.maxout = maxout
        self.rollingSum = 0.0
        self.lastVal = 0.0

    #prints the current gains, desired, and min/max output
    def __str__(self):
        string = 'PID Controller:\n'
        string += 'P Gain : ' + str(self.kp) + '\n'
        string += 'I Gain : ' + str(self.ki) + '\n'
        string += 'D Gain : ' + str(self.kd) + '\n'
        string += 'Desired: ' + str(self.desired) + '\n'
        string += 'MaxOut : ' + str(self.maxout) + '\n'
        string += 'MinOut : ' + str(self.minout) + '\n'
        return string

    #takes the current value and returns the controller output
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

    #sets the desired value of the controller to the passed in value
    def setDesired(self, newdesired):
        self.desired = newdesired

    #sets the minimum output of the controller to the passed in value
    def setMinOut(self, newmin):
        self.minout = newmin

    #sets the maximum output of the controller to the passed in value
    def setMaxOut(self, newmax):
        self.maxout = maxout

    #sets the controller gains to the passed in values
    def setGains(self, kp, ki, kd):
        self.setPGain(kp)
        self.setIGain(ki)
        self.setDGain(kd)

    #sets the P gain to the passed in value
    def setPGain(self, kp):
        self.kp = kp

    #sets the I Gain to the passed in value
    def setIGain(self, ki):
        #multiply the rolling sum by the ratio of the new gain to the old gain
        self.rollingSum *= (ki/self.ki)

        #set the i gain to the new gain
        self.ki = ki
        

    #sets the D Gain to the passed in value
    def setDGain(self, kd):
        self.kd = kd

    #clears the reolling sum, allowing for a reset of the controller
    def resetRollingSum(self):
        self.rollingSum = 0.0
        
        
#Linear Quadratic Regulator controller, linear matrix controller
class LQR( AbstractController ):

    #checks to make sure the matrix matches up with the desired values and saves the values
    def __init__(self, matrix, desired,):
        if not len(desired) == len(matrix[0]):
            print 'You need to have the same amount of desired states as the height of the k matrix'
            self.k = -1
            self.desired = -1
            return

        self.k = np.asarray( matrix )
        self.desired = desired
        
        print 'LQR consctructor'

    #prints the current gains and desired state
    def __str__(self):
        string = 'LQR Controller:\n"
        string += 'K matrix: ' + str(self.k) + '\n' 
        string += 'Desired : ' + str(self.desired)
        return string

    #does the lqr and returns a list of outputs
    def doControl(self, curState):
        if not len(self.desired) == len( curState )
            print 'Your State matrix does not have enough values'
            return -1

        #calculate the errors of all the states
        errors = [ desired - acutal for desired, acutal in zip (self.desired, curState ) ]

        #multiply the errors by the K matrix and return the matrix 
        return self.k.dot( errors )
        

    def setDesired(self, newdesired):
        self.desired = newdesired

    def setMinOut(self, newmin):
        self.minout = newmin

    def setMaxOut(self, newmax):
        self.maxout = maxout

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
