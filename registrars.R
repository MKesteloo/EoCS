# Import dataset
ransomwareDataset <- read.csv(file="dataset_ransomware.csv", header=TRUE, sep=",", skip = 8)

# Get top 20 registrars
registrars <- as.data.frame(table(toupper(ransomwareDataset$Registrar)))
# Fix empty string
registrars$Var1 <- as.character(registrars$Var1)
registrars$Var1[registrars$Var1==""] <- "UNKNOWN"
registrars$Var1 <- as.factor(registrars$Var1)

orderedRegs <- registrars[with(registrars, order(Freq, decreasing = TRUE)), ]
top20regs <- orderedRegs[1:20,]


# Plot of top 20 registrars
op <- par(mar = c(5,18,4,2) + 0.1)
bp <- barplot(top20regs$Freq, names.arg = top20regs$Var1, cex.names = 0.5, las = 2, horiz = TRUE)
values <- as.matrix(top20regs$Freq)
text(values-50, bp, labels=as.character(values), cex = 0.5)
par(op) ## reset

