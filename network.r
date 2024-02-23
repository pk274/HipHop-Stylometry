# Paul Kull, 2024

library("stylo")

setwd("C:/Users/paulk/OneDrive/Desktop/Unistuff/1.sem/dh/HipHop-Stylometry/Data/corpus")

tokenized.texts = load.corpus.and.parse(files = "all", corpus.lang = "English.all", preserve.case = "FALSE", ngram.size = 1)

features = make.frequency.list(tokenized.texts, head = 2000)

data = make.table.of.frequencies(tokenized.texts, features, relative = TRUE)

filtered.data <- delete.stop.words(data, stop.words = stylo.pronouns(corpus.lang = "English"))

filtered.data <- delete.stop.words(filtered.data, stop.words = c("nigga", "niggas"))

stylo(gui = FALSE, network = TRUE, analysis.type = "BCT", consensus.strength = 0.5, frequencies= filtered.data,
        mfw.min = 100, mfw.max = 2500, mfw.incr = 200, culling.min = 10, culling.max = 70, culling.incr = 10,
        write.svg.file = TRUE, filename.column = "filename", grouping.column = "artist")

#stylo(gui = FALSE, network = TRUE, analysis.type = "PCR", frequencies= filtered.data,
#        mfw.min = 100, mfw.max = 100, mfw.incr = 200, culling.min = 30, culling.max = 30, culling.incr = 10,
#        write.svg.file = FALSE, filename.column = "filename", grouping.column = "artist", pca.visual.flavour = "loadings")