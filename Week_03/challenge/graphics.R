#--------------------------------------------------------------------------
# Create 2x2 multiplot based on data of Auckland's Maunga Whau Volcano
#--------------------------------------------------------------------------

options(warn=-1)

par(mfrow=c(2,2))
image(volcano, col=rainbow(100))
image(volcano, col=heat.colors(100))
image(volcano, col=terrain.colors(100))
image(volcano, col=gray.colors(100))


#--------------------------------------------------------------------------
# Create a 2x2 multiplot with histogram, boxplot, barchart and piechart
#--------------------------------------------------------------------------

par(mfrow=c(2,2))

#--------------------------------
# Histogram (example)
#--------------------------------

hist(rnorm(10000), 
     main = "Histogram",
     xlab = "Values",
     col = "yellow")

#--------------------------------
# Boxplot (example)
#--------------------------------

boxplot(rnorm(10000), 
        xlab = "Values",
        ylab = "Frequency", 
        main = "Boxplot",
        col = 'green',
        horizontal = TRUE
)

#--------------------------------
# Barchart (example)
#--------------------------------

colors = c("green","orange","brown")
months  <- c("Mar","Apr","May","Jun","Jul")
regions <- c("East","West","North")
values  <- matrix(c(2,9,3,11,9,4,8,7,3,12,5,2,8,10,11), 
                 nrow = 3, 
                 ncol = 5, 
                 byrow = TRUE)
barplot(values, 
        main = "Bar chart", 
        names.arg = months, 
        xlab = "month", 
        ylab = "revenue", col = colors)
legend("topleft", regions, cex = 1.0, fill = colors)

#--------------------------------
# Piechart (example)
#--------------------------------
x <- c(21, 62, 10, 53)
labels <- c("London", "New York", "Singapore", "Berlin")
pie(x, 
    labels, 
    main = "Pie chart", 
    col = rainbow(length(x)))