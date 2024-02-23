# Paul Kull, 2022

library("stylo")

setwd("C:/Users/paulk/OneDrive/Desktop/Unistuff/1.sem/dh/HipHop-Stylometry/Data/corpus")

tokenized.texts = load.corpus.and.parse(files = "all", corpus.lang = "English.all", preserve.case = "FALSE", ngram.size = 1)

features = make.frequency.list(tokenized.texts, head = 2000)

data = make.table.of.frequencies(tokenized.texts, features, relative = TRUE)

filtered.data <- delete.stop.words(data, stop.words = stylo.pronouns(corpus.lang = "English"))

filtered.data <- delete.stop.words(filtered.data, stop.words = c("nigga", "niggas"))

culled.data <- perform.culling(filtered.data, culling.level = 25)

#x = imposters.optimize(culled.data)
#print(x)

print("Forgot about Dre:")
imposters(reference.set = culled.data[-c(1, 2, 3, 4, 5, 6, 7),], test = culled.data[1,], distance = "wurzburg", imposters = 1)
print("Whats the Difference:")
imposters(reference.set = culled.data[-c(1, 2, 3, 4, 5, 6, 7),], test = culled.data[2,], distance = "wurzburg", imposters = 1)
print("Still Dre:")
imposters(reference.set = culled.data[-c(1, 2, 3, 4, 5, 6, 7),], test = culled.data[3,], distance = "wurzburg", imposters = 1)
print("Deep Water:")
imposters(reference.set = culled.data[-c(1, 2, 3, 4, 5, 6, 7),], test = culled.data[4,], distance = "wurzburg", imposters = 1)
print("Genocide:")
imposters(reference.set = culled.data[-c(1, 2, 3, 4, 5, 6, 7),], test = culled.data[5,], distance = "wurzburg", imposters = 1)
print("The Recipe:")
imposters(reference.set = culled.data[-c(1, 2, 3, 4, 5, 6, 7),], test = culled.data[6,], distance = "wurzburg", imposters = 1)
print("Deep Cover:")
imposters(reference.set = culled.data[-c(1, 2, 3, 4, 5, 6, 7),], test = culled.data[7,], distance = "wurzburg", imposters = 1)


#stylo()