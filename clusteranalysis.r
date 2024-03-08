#Paul Kull, 2024

library("stylo")

setwd("C:/Users/paulk/Desktop/Unistuff/1.sem/dh/HipHop-Stylometry/Data/corpus")

tokenized.texts = load.corpus.and.parse(files = "all", corpus.lang = "English.all", preserve.case = "FALSE", ngram.size = 1)

features = make.frequency.list(tokenized.texts, head = 1650)

data = make.table.of.frequencies(tokenized.texts, features, relative = TRUE)

filtered.data <- delete.stop.words(data, stop.words = stylo.pronouns(corpus.lang = "English"))

culled.data <- perform.culling(filtered.data, culling.level = 20)

stylo(gui = FALSE, analysis.type = "CA", frequencies= culled.data, mfw.min = 1500, mfw.max = 1500, culling.min = 20, culling.max = 20,
delete.pronouns = TRUE, custom.graph.title = "Cross-genre")
