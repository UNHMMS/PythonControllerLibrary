from controllers import PID, LQR, SMC, HInfinity

pid = PID()
pid.doControl()
pid.setDesired()
pid.flying()
pid.landing()
pid.killing()
print pid

print '\n'

lqr = LQR()
lqr.doControl()
lqr.setDesired()
lqr.flying()
lqr.landing()
lqr.killing()
print pid

print '\n'

smc = SMC()
smc.doControl()
smc.setDesired()
smc.flying()
smc.landing()
smc.killing()
print pid

print '\n'

hi = HInfinity()
hi.doControl()
hi.setDesired()
hi.flying()
hi.landing()
hi.killing()
print pid

print '\n'

