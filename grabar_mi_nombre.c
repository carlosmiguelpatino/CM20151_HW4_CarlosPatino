#include <stdio.h>
#include <stdlib.h>
/*El asume que en el computador esta instalado sox. Para interrumpir la grabacion se debe usar el comando ^C
El archivo de audio queda guardado en la carpeta data*/
int main(){
	char command[100];
	system("rec -c 1 -b 16 ./data/minombre.wav");
	return 0;

}
