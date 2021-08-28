#include <Mouse.h>

float moveX = 0;
float moveY = 0;
char caractere;
String message;

void setup(){

    Serial.begin(115200);
}

void loop(){

    if(Serial.available()>0){
        caractere = Serial.read();
        if (caractere == '!'){    
            check_message(message);
            message = "";
            Mouse.move(moveX, moveY, 0);
            Mouse.move(moveX, moveY, 0);
            Mouse.move(moveX, moveY, 0);
            Mouse.move(moveX, moveY, 0);
        } else message.concat(caractere);
    }   
      
}

void check_message(String read){
  int index = 0; 
    if(read.startsWith("move/X")){
        read.replace("move/X", "");
        for(int i = 0; i < read.length(); i++){
          if(read[i] == '|'){
            index = i;
            break;
          }
        }
        String valueX = read.substring(0, index);
        moveX = valueX.toInt();
        read.replace(valueX+'|', "");
    } if(read.startsWith("move/Y")){
        read.replace("move/Y", "");
        moveY = read.toInt();
    }
}
