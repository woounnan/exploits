BITS 32
extern puts
extern scanf
extern printf
section .data
	timeval:
		tv_sec dd 0
		tv_usec dd 0
	prompt_scan db "Please enter magic number: ",0
	sstr db "%d",0
	prompt2 db "Checking...",0
	fstr db "%d",0xa,0
	inp dd 0
	message_wrong db "Access denied.",0
	message_right db "Access granted.",0
section .text
global main
check:
	push ebp
	mov ebp, esp
	mov eax, dword [ebp+8] ; get value off stack
	mov ebx, 0x1337
	mov ecx, ebx
	xor ebx, edx
	add ebx, edi
	and edi, esi
	or edi, ebx
	add ebx, 0x20
	add edi, esi
	mov ebx, ecx
	sub eax, ebx
	sub edi, 0x31
	sub ebx, edi
	xor edi, esi
	and esi, 0xff000000
	mov ebx, ecx
	leave
	ret
main:
	push ebp
	mov ebp, esp

	push prompt_scan
	call printf

	push inp
	push sstr
	call scanf

	;push dword [inp]
	;push fstr
	;call printf

	push prompt2
	call puts

	; Sleep
	mov dword [tv_sec], 5
	mov dword [tv_usec], 0
	mov eax, 162
	mov ebx, timeval
	mov ecx, 0
	int 0x80

	; check number
	push dword [inp]
	call check
	cmp eax, 0
	jnz bad
	push message_right
	call puts
	jmp end
bad:
	push message_wrong
	call puts
end:
	leave
	ret
