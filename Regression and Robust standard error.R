install.packages("MASS")
install.packages('pacman')
install.packages('lmtest')
install.packages('lmtest')
install.packages('plm')
install.packages('car')
library('stargazer')
library('foreign')
library('data.table')
library('fixest')
library('magrittr')
library('sandwich')
library('lmtest')
library('plm')
library('MASS')
library('car')
attach(data1)

#Breusch-Pagan test:
bptest(growth ~ fdi + income + capital + trade +crisis, data=data1, studentize=F)

#OLS Regression
model= lm(growth ~ fdi + income + capital + trade + crisis, data=data1)
summary(model)

#Robust standard error:
a=coeftest(model, vcovHC)
stargazer(model,(coeftest(model, vcovHC)), type='text')

dt = data.frame(data1[,-2])
dt=data.frame(dt[,-1])
dt
round(cor(dt),4)
vif(model)











