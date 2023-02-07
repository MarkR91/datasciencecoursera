pollutantmean<-function(directory,pollutant,id=1:332){
  

  files<-list.files(directory,full.names=TRUE,pattern="*.csv")
  
  
  for(i in id){
    
    input<-files[i]
    
    data<-read.csv(input)
    #options(max.print=100000) #avoids reached 'max' limit
    
    #print(data)
    
  }
  #print(class(data))
  
    
  #Use df[!is.na(df$col_name),] to remove NA values
  data<-data[!is.na(data[[pollutant]]),]
  #print(data)
  #print(class(data))
  print(data[[pollutant]])

  
  print(mean(data[[pollutant]]))
  
  
      
}
 
  
  