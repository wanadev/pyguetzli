// JPEG OR PNG

typedef enum {
    GUETZLI_IMAGE_TYPE_UNKNOWN,
    GUETZLI_IMAGE_TYPE_JPEG,
    GUETZLI_IMAGE_TYPE_PNG,
} GuetzliImageType;

typedef struct {
    char* data;
    int length;
    GuetzliImageType type;
} GuetzliImage;

GuetzliImage guetzliImageOptimize(GuetzliImage in, int quality);
GuetzliImage guetzliImageRead(const char* filename, GuetzliImageType type);
GuetzliImage guetzliImageNew(GuetzliImageType type, int length);
void guetzliImageFree(GuetzliImage* image);


// PIXEL ARRAY

typedef struct {
    unsigned char* data;
    int width;
    int height;
} GuetzliRgbArray;

GuetzliImage guetzliRgbArrayOptimize(GuetzliRgbArray in, int quality);
GuetzliRgbArray guetzliRgbArrayNew(int width, int height);
void guetzliRgbArrayFree(GuetzliRgbArray* array);

