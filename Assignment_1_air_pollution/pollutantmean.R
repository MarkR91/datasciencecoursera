pollutantmean<-function(directory,pollutant,id=1:332){
  

  files<-list.files(directory,full.names=TRUE,pattern="*.csv")
  
  pollutant_acc<-NULL
  
  for(i in id){
    
    input<-files[i]
    
    data<-read.csv(input)
    
    pollutant_acc<-rbind(pollutant_acc,data)
    
    
  }
  #print(class(data))
  View(pollutant_acc)
    
  #Use df[!is.na(df$col_name),] to remove NA values
  pollutant_acc<-pollutant_acc[!is.na(pollutant_acc[[pollutant]]),]
  #print(data)
  #print(class(data))
  #print(data[[pollutant]])

  
  print(mean(pollutant_acc[[pollutant]]))
  
  
      
}
 
  
  