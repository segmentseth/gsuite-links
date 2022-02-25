library(readr)

##### Finalized Simple Setup #####
links <- read_csv("links.csv")
get_new <- links$twilio
names(get_new) <- links$segment

##### Perform a Lookup #####
get_new['https://drive.google.com/open?id=1o-gqHYxvXb9YvqGCzLoduCQBxXIBC8hW_DENMa3AqRs'] 
