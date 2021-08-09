import math

#controls (on drop-down)
species = ''
#controls (on sliders)
dbh = 14 #inches
height = 90 #feet
w = 2 #inches
d = 4 #inches
l = 16 #feet
k_w = 0.125 #inches
k_d = 0.125 #inches

def milling(species, dbh, height, w, d, l, k_w, k_d):

    dob_i = dbh
    dib_i = dbh

    if (((dib_i/2)**2 - (0.5*w)**2)**(0.5) < 0.5*d) is True:
        return 0

    n = math.floor(height/(l)) #at some point change to merchantable limit

    for i in range(1, n):
        if i > 1: break #until taper is implemented
        x_total = [0,0]
        for sub in range(0, 2):
            m = math.floor((dib_i + k_w)/(w + k_w) - sub) #maximum number of rows
            m_half = math.ceil(m/2) #half of the maximum number of rows
            x_list = []
            x_sum = 0
            if (((dib_i/2)**2 - (0.5*w)**2)**(0.5) < 0.5*d) is True: #checking merchantable limit
                return 0
            for j in range(1, m_half+1):
                if (m % 2) == 0: #even number of rows
                    a = j*(w + k_w) - 0.5*k_w
                    b = ((dib_i/2)**2 - a**2)**(0.5)
                    f = b*2
                    x = math.floor((f + k_d)/(d + k_d))
                    x_list.append(x)
                    x_sum += x
                elif (m % 2) != 0: #odd number of rows
                    a = j*(w + k_w) - (0.5*w + k_w)
                    b = ((dib_i/2)**2 - a**2)**0.5
                    f = b*2
                    x = math.floor((f + k_d)/(d + k_d))
                    x_list.append(x)
                    if j == 1: x_sum1 = x
                    x_sum += x

            if (m % 2) == 0: x_total[sub] = x_sum*2
            elif (m % 2) != 0: x_total[sub] = x_sum*2 - x_sum1
            print(x_list)
    print(x_total)
    return max(x_total)

print(milling(species, dbh, height, w, d, l, k_w, k_d))
