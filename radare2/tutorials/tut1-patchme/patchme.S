BITS 32
extern puts
section .data
	mystring db "Hello there! Can you patch me up to call my function?",0
	secret db "Thank you!",0
section .text
global main
callme:
	push ebp
	mov ebp, esp
	push secret
	call puts
	leave
	ret
main:
	push ebp
	mov ebp, esp
	push mystring
	call puts
	nop
	nop
	nop
	nop
	nop
	leave
	ret
