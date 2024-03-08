# Paul Kull, 2024
import matplotlib.pyplot as plt 
import matplotlib.ticker as plticker
import numpy.ma as ma
import numpy as np

cullingRate = [20, 30, 40, 50, 60, 70, 80, 90]

jayZ = [0, 0.11, 0.16, 0.48, 0.48, 0.56, 0.60, 0.86]
cullingjay = 60
jayWinner = ma.masked_less(jayZ, 0.40)
jayLoser = ma.masked_greater(jayZ, 0.40)

snoopDogg = [0.96, 1, 0.93, 0.84, 0.93, 0.93, 0.77, 0.89]
cullingsnoop = 20

eminem = [0.16, 0.27, 0.31, 0.52, 0.51, 0.53, 0.27, 0.22]
cullingem = 20 #nicht bei 90
emWinner = ma.masked_less(eminem, 0.40)
emLoser = ma.masked_greater(eminem, 0.40)

kendrickLamar = [0.06, 0.10, 0.3, 0.62, 0.61, 0.82, 0.68, 0.60]
cullingken = 50
kenWinner = ma.masked_less(kendrickLamar, 0.40)
kenLoser = ma.masked_greater(kendrickLamar, 0.40)

#50% culling -> 596 words
#70% -> 313
#90% -> 113

optimized_score = [0.59, 0.6, 0.54, 0.55, 0.47, 0.49, 0.55, 0.56, 0.56]

figure = plt.figure()
fig = figure.add_subplot()
fig.plot(cullingRate, jayZ, 'g-', label = 'Jay-Z confidence')
fig.plot(cullingRate, eminem, 'r-', label = 'Eminem confidence')
fig.plot(cullingRate, snoopDogg, 'k-', label = 'Snoop Dogg confidence')
fig.plot(cullingRate, kendrickLamar, 'b-', label = 'Kendrick Lamar confidence')
fig.set_title('Confidence scores of the actual ghostwriters')
fig.set_xlabel('culling rate')
fig.set_ylabel('confidence score')
plt.legend(["Jay-Z", "Eminem", "Snoop Dogg", "Kendrick Lamar"])

fig.plot(cullingRate, jayLoser, 'g.', label = 'Jay-Z confidence')
fig.plot(cullingRate, emLoser, 'r.', label = 'Eminem confidence')
fig.plot(cullingRate, kenLoser, 'b.', label = 'Kendrick Lamar confidence')

fig.plot(cullingRate, jayWinner, 'go', label = 'Jay-Z confidence')
fig.plot(cullingRate, emWinner, 'ro', label = 'Eminem confidence')
fig.plot(cullingRate, snoopDogg, 'ko', label = 'Snoop Dogg confidence')
fig.plot(cullingRate, kenWinner, 'bo', label = 'Kendrick Lamar confidence')

plt.show()
