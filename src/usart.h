#ifndef USART_H_
#define USART_H_

#include <stdint.h>

void USART_Init(void);
void USART_Transmit(uint8_t data);
uint8_t USART_Receive(void);

#endif  // USART_H_
