const byte redPin = 3, whitePin = 4;
const int btnDelay = 50;
unsigned long longPressDur = 2000;
int redBtnLstState = LOW, whiteBtnLstState = LOW;
bool btnLongPress = false;
unsigned long longPressMillis, lstBtnMillis, pressDur, crntMillis;

void setup() // SETUP HERE
{
  Serial.begin(9600);
  pinMode(redPin, INPUT_PULLUP); // liga pin 4 (para o botão vermelho)
  pinMode(whitePin, INPUT_PULLUP); // liga pin 3 (para o botão branco)
}

void loop() // LOOP HERE
{
  int redBtnState = !digitalRead(redPin); // vê o estado atual do botão 
  int whiteBtnState = !digitalRead(whitePin); // vê o estado atual do botão
  crntMillis = millis(); // vê o tempo atual de que o arduino está ligado
  
  if(crntMillis - lstBtnMillis > btnDelay) // permite que o botão seja clicado uma unica vez
  {
    // Vê se um dos botões foi premido
    if(redBtnState && !redBtnLstState && !btnLongPress) // estado do botão 'red' ativo e ultimo estado desativo e não é longPress
    {
      longPressMillis = crntMillis; // vai igualando a variavel de longPressMillis ao millis atual
      redBtnLstState = HIGH; // o ultimo estado do botão fica HIGH (ativo)
    }
    else if(whiteBtnState && !whiteBtnLstState && !btnLongPress) // estado do botão 'white' ativo e ultimo estado desativo e não é longPress
    {
      longPressMillis = crntMillis; // vai igualando a variavel de longPressMillis ao millis atual
      whiteBtnLstState = !whiteBtnLstState; // o ultimo estado do botão fica negado, ou seja HIGH (ativo)
    }
    
    pressDur = crntMillis - longPressMillis; // vê quanto tempo o botão está ativo e guarda na variavel pressDur
    
    // Vê quando se larga o botão, quando o estado estiver LOW (desativo) e o ultimo estado HIGH (ativo)
    if(!redBtnState && redBtnLstState) // Botão RED solto
    {
      Serial.println("R"); // RED
      // reseta as variaveis do ultimo estado do botão red e de longPress
      redBtnLstState = !redBtnLstState;
      btnLongPress = false;
    }
    else if(!whiteBtnState && whiteBtnLstState) // Botão WHITE solto
    {
      Serial.println("W"); // WHITE
      // reseta as variaveis do ultimo estado do botão white e de longPress
      whiteBtnLstState = !whiteBtnLstState; btnLongPress = false;
    }
    lstBtnMillis = crntMillis; // iguala o ultimo millis ao millis atual
  }
}
