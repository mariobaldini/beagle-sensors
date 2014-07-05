/*
  Source para Arduino;
  Autores: Mario Baldini / Joao Baggio
  
  Aquisicao de dados para ARTIGO CBEB
  24/05/2014
  
 */

int sensorValue;
int data[500];
double tic1,tic2,toc;


void setup() {                

  Serial.begin(115200);
 
 
 
}


void loop() {
  
  tic1 = millis();
 
  for (int i=0; i < 500; i++){
      data[i] = analogRead(A0);
      //Serial.println(data[i]); 
   } 
//  Serial.println(data[]); 
  tic2 = millis();

 

   
   
   
   
   
   
   
  toc = tic2 - tic1;
  Serial.println("----------------------");
  Serial.println(toc);      
     
  delay(5 *1000);
}

