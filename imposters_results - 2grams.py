# Paul Kull, 2024
import matplotlib.pyplot as plt 
import matplotlib.ticker as plticker
import numpy.ma as ma
import numpy as np

cullingRate = [20, 30, 40, 50, 60, 70, 80, 90]

jayZ = [0.36, 0.41, 0.76, 0.52, 0.62, 0.26, 0.28, 0.44]
cullingjay = 60
jayWinner = ma.masked_less(jayZ, 0.45)
jayLoser = ma.masked_greater(jayZ, 0.45)

snoopDogg = [0.95, 0.9, 0.85, 0.92, 0.59, 0.55, 0.69, 0.73]
cullingsnoop = 20

eminem = [0.24, 0.24, 0.3, 0.61, 0.73, 0.73, 0.92, 0.79]
cullingem = 20 #nicht bei 90
emWinner = ma.masked_less(eminem, 0.45)
emLoser = ma.masked_greater(eminem, 0.45)

kendrickLamar = [0.55, 0.43, 0.63, 0.46, 0.43, 0.42, 0.75, 0.46]
cullingken = 50
kenWinner = ma.masked_less(kendrickLamar, 0.45)
kenLoser = ma.masked_greater(kendrickLamar, 0.45)

#50% culling -> 552 words
#70% -> 199
#90% -> 38

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
