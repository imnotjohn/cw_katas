#
# Bouncing Balls Kata
#

def bouncingBall(h, bounce, window):
    sum = 0
    if (h>0):
        if (bounce > 0 and bounce < 1):
            if (h > window):
                while (h > window):
                    h = h*bounce
                    if (h > window): #mother views bouncing ball as it falls and bounces back up
                        sum += 2
                    else:
                        sum+=1 #mother only views ball as it falls since it doesn't bounce beyond window height
                return sum
    return -1
