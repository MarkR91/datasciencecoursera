complete <- function(directory, id = 1:332){

  files<-list.files(directory,full.names=TRUE,pattern="*.csv")
 
  acc<-c()
  
  for(i in id){
    
    input<-files[i]
    
    data<-read.csv(input)
    
    #Use df[!is.na(df$col_name),] to remove NA values.
    #If a reading existed for sulfates,then there will be a corresponding one for nitrates.
    data<-data[!is.na(data$sulfate),]
    
    # print(count(data))
    # Need to load dplyr library in order to use count function.
    acc<-c(acc,count(data))

  }
  #print(acc)
  
  df <-as.data.frame(acc)
  
  print(df)

  #View(df)
  
  

}
 
