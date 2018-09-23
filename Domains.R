# Import dataset
ransomwareDataset <- read.csv(file="dataset_ransomware.csv", header=TRUE, sep=",", skip = 8)

# Create domain column
domain <- function(x){
  if(x!=""){
      splited <- strsplit(strsplit(gsub("http://|https://|www\\.", "", x), "/")[[c(1, 1)]], ".", fixed = TRUE)
      if(length(splited[[1]]) == 2){
        splited[[c(1,2)]]
      }
      else{
        'unknown'
      }
  }
}

ransomwareDataset$Host <- lapply(ransomwareDataset$Host, domain)
#domainfreq <- as.data.frame(table(ransomwareDataset$Host))
lol <- ransomwareDataset$Host