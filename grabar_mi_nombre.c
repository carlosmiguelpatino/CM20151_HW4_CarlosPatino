#include <stdio.h>
#include <stdlib.h>
//El asume que en el computador esta instalado sox. La grabacion se interrumpira en el segundo 4.

int main(){
	char command[100];
	system("rec -c 1 -b 16 minombre.wav silence -l 0 1 00:00:4 1\%");
	return 0;

}
