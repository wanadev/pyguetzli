// GuetzliImage

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

GuetzliImage* guetzliImageNew(GuetzliImageType type, int length);
void guetzliImageFree(GuetzliImage* image);
GuetzliImage* guetzliImageReadFile(const char* filename);
void guetzliImageWriteFile(const char* filename, GuetzliImage* image);
GuetzliImage* guetzliImageProcess(GuetzliImage* in, int quality);


// GuetzliRgbArray

typedef struct {
    char* data;
    int width;
    int height;
} GuetzliRgbArray;

GuetzliRgbArray* guetzliRgbArrayNew(int width, int height);
void guetzliRgbArrayFree(GuetzliRgbArray* array);
GuetzliImage* guetzliRgbArrayProcess(GuetzliRgbArray* in, int quality);
