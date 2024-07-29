// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>


typedef uint8_t BYTE;

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    uint8_t header[HEADER_SIZE]; // declares array of size 44 bytes (size of .wav header)
    fread(header, HEADER_SIZE, 1, input); // read 1 * HEADER_SIZE bytes from input file and store them in header array
    fwrite(header, HEADER_SIZE, 1, output); // read 1 * HEADER_SIZE bytes from header array and store them in output file

    // TODO: Read samples from input file and write updated data to output file

    int16_t buffer; // int16_t is the size of .wav sample
    while (fread(&buffer, sizeof(int16_t), 1, input)) { // will continue reading until fread returns 0 (false) indicating end of file
        buffer *= factor; //
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

    // Close files
    fclose(input);
    fclose(output);
}
