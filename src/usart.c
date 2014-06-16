#include "usart.h"

#include <avr/io.h>

// from datasheet - baudrate 115.2k @ 14.7456MHz
#define BAUD_PRESCALE 7

void USART_Init(void) {
  UCSRB = (1<<RXEN)|(1<<TXEN);

  UCSRC = (1<<URSEL)|(1<<UCSZ0)|(1<<UCSZ1);

  UBRRL = BAUD_PRESCALE;
  UBRRH = (BAUD_PRESCALE >> 8);
}
 
void USART_Transmit(uint8_t data) {
  while((UCSRA &(1<<UDRE)) == 0);
  UDR = data;
}

uint8_t USART_Receive(void) {
  while((UCSRA&(1<<RXC)) == 0);
  return UDR;
}

