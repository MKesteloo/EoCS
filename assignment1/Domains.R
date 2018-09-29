# Import dataset
ransomwareDataset <- read.csv(file="dataset_ransomware.csv", header=TRUE, sep=",", skip = 8)

# Create domain column
domain <- function(x){
  if(x!=""){
      splitted <- strsplit(strsplit(gsub("http://|https://|www\\.", "", x), "/")[[c(1, 1)]], ".", fixed = TRUE)
      lastelem <- tail(splitted[[1]], n=1)
      if(is.na(as.numeric(lastelem))){
        lastelem
      }
      else{
        'unknown'
      }
  }
}

splitedvec <- unlist(lapply(ransomwareDataset$Host, domain), use.names=FALSE)

domainfreq <- as.data.frame(table(splitedvec))
names(domainfreq)[1] = "Domains"

# Order on size and pick the top 20
orderedFreq <- domainfreq[with(domainfreq, order(Freq, decreasing = TRUE)), ]
top20 <- orderedFreq[1:20,]
rownames(top20) <- NULL
top20 <- droplevels(top20)

# Plot a graph
bp <- barplot(top20$Freq, names.arg = top20$Domain, cex.names = 0.5, las = 1, horiz = TRUE, xlim=c(0,6400))
values <- as.matrix(top20$Freq)
text(values+120, bp, labels=as.character(values), cex = 0.5)
