# Import dataset
ransomwareDataset <- read.csv(file="dataset_ransomware.csv", header=TRUE, sep=",", skip = 8)

# Create a subset
#ransomwareUS <- subset(ransomwareDataset, Country == 'US')

# Create counted country list
cc <- as.data.frame(table(ransomwareDataset$Country))
names(cc)[1] = "Country"

# Order on size and pick the top 20
orderedCC <- cc[with(cc, order(Freq, decreasing = TRUE)), ]
top20 <- orderedCC[1:20,]
rownames(top20) <- NULL
top20 <- droplevels(top20)

# Plot a graph
barplot(top20$Freq, names.arg = top20$Country, cex.names = 0.5, las = 1, horiz = TRUE)

#axis(side = 1, at = bp, labels = countedCountries)

#bp <- barplot(t(ransomwareDataset$Host))
#axis(side = 1, at = bp, labels = ransomwareDataset$Host)

