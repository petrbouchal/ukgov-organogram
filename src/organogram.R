# library(pbtools)
# library(plyr)
library(dplyr)
library(data.table)
library(stringr)

junior <- read.csv('./data-input/Cabinet_Office_31_March_2014_junior_data.csv')

summary(junior)
summary(senior)

junior <- as.data.table(junior)

senior$name[senior$fte==min(senior$fte)]

senior <- read.csv('./data-input/Cabinet_Office_31_March_2014_senior_data.csv')
names(senior) <- tolower(str_replace_all(names(senior),'\\.',''))
senior <- as.data.table(senior)
senior <- senior %>% 
  group_by(postuniquereference) %>%
  mutate(seniorreports = n())
