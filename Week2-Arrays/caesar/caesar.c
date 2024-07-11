// Project URL: https://cs50.harvard.edu/x/2024/psets/2/caesar/

#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{

    // Make sure program was run with just one command-line argument
    if (argc != 2) {
        printf("Usage: ./caesar key\n"); 
        return 1;
    }

    // Make sure every character in argv[1] is a digit
    for (int i = 0; i < strlen(argv[1]); i++) {
        if (!isdigit(argv[1][i])) {
            printf("Usage: ./caesar key\n"); 
            return 1;
        }
    }

    // Convert argv[1] from a `string` to an `int`
    int key = atoi(argv[1]);

    // Prompt user for plaintext
    string plaintext = get_string("Plaintext: ");
    printf("Ciphertext: ");

    // For each character in the plaintext: 
    for (int i = 0, length = strlen(plaintext); i < length; i++) {

        // Rotate the character if it's a letter
        if(isupper(plaintext[i])) {
            
            printf("%c", (plaintext[i] - 65 + key) % 26 + 65);

        } else if (islower(plaintext[i])) {
            
            printf("%c", (plaintext[i] - 97 + key) % 26 + 97);

        } else {

            printf("%c", plaintext[i]);

        }
    }

    printf("\n");
    return 0;
}