from controllers import PID, LQR, SMC, HInfinity

pid = PID( 1, 2, 3, 3.14159, 10, 32 )
print pid

print '\n'

lqr = LQR()
lqr.doControl()
lqr.flying()
lqr.landing()
lqr.killing()
print lqr

print '\n'

smc = SMC()
smc.doControl()
smc.flying()
smc.landing()
smc.killing()
print smc

print '\n'

hi = HInfinity()
hi.doControl()
hi.flying()
hi.landing()
hi.killing()
print hi

print '\n'

