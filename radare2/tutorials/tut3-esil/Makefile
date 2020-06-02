all: esil

clean: clean_esil

esil.o: esil.S
	nasm -f elf32 -o $@ $<

esil: esil.o
	gcc -m32 -o $@ $<

clean_esil:
	rm -f esil
	rm -f esil.o
