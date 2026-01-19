#! /usr/bin/Rscript

library('seriation')

args = commandArgs(trailingOnly=TRUE)

n =  as.numeric(args[1])
outfile <- args[2]
m <- random.robinson(n, anti=TRUE)
write.table(m, file="random_robinson_matrix.csv", sep=",",row.names=FALSE, col.names=FALSE)
