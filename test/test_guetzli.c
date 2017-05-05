#include "guetzli.h"

#include <stdio.h>

int main(void)
{
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

    GuetzliImage* image = guetzliRgbArrayOptimize(array, 84);
    guetzliRgbArrayFree(array);

    return 0;
}
