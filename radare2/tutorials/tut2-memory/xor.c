#include <stdio.h>

int check(char input[32], char buffer[32])
{
  int i = 0;
  int j = 42;
  for(i = 0; i < 32; i++)
    {
      input[i] = input[i] ^ j;
      j += 3;
    }
  /*
    // TODO: For debugging purposes only
  for(i = 0; i < 32; i++)
    {
      printf("%d ", input[i]);
    }
  printf("\n");
  for(i = 0; i < 32; i++)
    {
      printf("%d ", buffer[i]);
    }
    printf("\n");
  */
    return !strncmp(buffer, input, 32);
}

int main(int argc, char* argv[])
{
  /* TODO: Future idea: input[32], buffer[32] */
  int ret = 0;
  char input[33];
  char buffer[33] = {0x67, 0x62, 0x7e, 0x7c, 0x6d, 0x4d, 0x54, 0x0b, 0x36, 0x1a, 0x3f, 0x2a,
  0x7b, 0x2f, 0x24, 0x25, 0x69, 0x29, 0x14, 0x1a, 0x5b, 0x0c, 0x0d, 0x5a,
		     0x0b, 0x2a, 0x0a, 0x4a, 0x19, 0xe9, 0xb3, 0xda};
  printf("Enter the password: ");
  ret = scanf("%32s", input);

  if(!check(input, buffer))
    printf("Wrong!\n");
  else
    printf("Good job! :)\n");

  return 0;
}
