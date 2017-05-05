#include "guetzli.h"

#include <stdio.h>
#include <assert.h>

int main(void)
{
    // --- JPEG image

    GuetzliImage* image = guetzliImageReadFile("./test/image.jpg");
    assert(image->type == GUETZLI_IMAGE_TYPE_JPEG);

    GuetzliImage* outImage = guetzliImageProcess(image, 84);

    guetzliImageFree(image);
    guetzliImageFree(outImage);

    // --- RGB Array

    GuetzliRgbArray* array = guetzliRgbArrayNew(10, 10);

    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < 10; ++j) {
            int index = 3 * (10 * i + j);
            array->data[index + 0] = 255;
            array->data[index + 1] = 0;
            array->data[index + 2] = 0;
        }
    }

    outImage = guetzliRgbArrayProcess(array, 84);

    guetzliRgbArrayFree(array);
    guetzliImageFree(outImage);

    return 0;
}
