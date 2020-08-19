/*
 * File:   clkController.c
 * Author: Andres Colon
 *
 * Created on August 18, 2020, 3:56 PM
 */


#include <xc.h> //header file for compiler
#include <pic18f4321.h> //header file for microcontroller
//bit initializations
#pragma config WDT = OFF
#pragma config LVP = OFF
#pragma config BOR = OFF
#pragma config OSC = INTIO2

void main(void) {
    TRISE = 0;//set port E as an output
    
    //for loops act as a delay in between alternating bit between high and low
    for(int i = 0; i < 255; i++){
        PORTEbits.RE0 = 1;
    }
    
    for(int i = 0; i < 255; i++){
        PORTEbits.RE0 = 0;
    }
    
    return;
}
