pollutantmean<-function(directory,id){
  

  files<-list.files(directory,full.names=TRUE,pattern="*.csv")
  
  i=0
  
  for(i in id){
    
    input<-files[i]
    
    data<-read.csv(input)
    #print(data)
    
    View(data)
    
  }
  print(class(data))
  
    
  #Use df[!is.na(df$col_name),] to remove NA values
  data<-data[!is.na(data$sulfate),]
  #print(data)
  #print(class(data))
  print(data$sulfate)
  print(mean(data$sulfate))
  
  
      
}
 
  
  