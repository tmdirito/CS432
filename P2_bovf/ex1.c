//gcc -fno-stack-protector -no-pie -o ex1 ex1.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void openFlag() {
    FILE *file;
    char c = 0;

    file = fopen("flag.txt", "r");
    if (file) {
        c = fgetc(file);
        while (c != EOF) {
            printf("%c", c);
            c = fgetc(file);
        }
        printf("\n");
    }
}

int main() {
    printf("Allocating 16 characters\n");

    char buffer[16];
    memset(buffer, 0, 16);

    scanf("%s", buffer);

    printf("You wrote %s\n", buffer);

    return 0;
}