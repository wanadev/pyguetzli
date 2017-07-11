// Guetzli image

// Frees allocated bytes.
void guetzli_free_bytes(char** bytes);

// Returns *bytes_out length.
int guetzli_process_jpeg_bytes(char* bytes_in, int length_in, char** bytes_out, int quality);

// Returns *bytes_out length.
int guetzli_process_rgb_bytes(char* bytes_in, int width, int height, char** bytes_out, int quality);
