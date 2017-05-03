#include "guetzli.hpp"

#include <guetzli/quality.h>
#include <guetzli/processor.h>

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>

// ---- JPEG or PNG

GuetzliImage guetzliImageOptimize(GuetzliImage in, int quality) {
    if (in.type == GUETZLI_IMAGE_TYPE_PNG) {
        std::cerr << "PNG images not supported yet." << std::endl;
        exit(1);
    }

    std::string inData;
    std::string outData;
    inData.assign(in.data, in.length);

    guetzli::Params params;
    params.butteraugli_target = static_cast<float>(guetzli::ButteraugliScoreForQuality(quality));
    Process(params, nullptr, inData, &outData);

    GuetzliImage outImage = guetzliImageNew(GUETZLI_IMAGE_TYPE_JPEG, outData.size());
    // @todo outImage.data = outData.c_str();
    return outImage;
}

GuetzliImage guetzliImageRead(const char* filename, GuetzliImageType type) {
    std::ifstream inFile(filename, std::ios::binary);
    std::vector<char> inBuffer((std::istreambuf_iterator<char>(inFile)), (std::istreambuf_iterator<char>()));

    // The image indeed
    GuetzliImage image = guetzliImageNew(type, inBuffer.size());
    memcpy(image.data, inBuffer.data(), image.length);

    return image;
}

GuetzliImage guetzliImageNew(GuetzliImageType type, int length) {
    GuetzliImage image;
    image.type = type;
    image.length = length;
    image.data = new char[image.length];
    return image;
}

void guetzliImageFree(GuetzliImage* image) {
    delete[] image->data;
    image->data = nullptr;
    image->length = 0;
}

// ---- RGB Array

GuetzliImage guetzliRgbArrayOptimize(GuetzliRgbArray in, int quality) {
    std::vector<uint8_t> inData;
    std::string outData;
    inData.assign(in.data, in.data + (in.width * in.height));

    guetzli::Params params;
    params.butteraugli_target = static_cast<float>(guetzli::ButteraugliScoreForQuality(quality));
    Process(params, nullptr, inData, in.width, in.height, &outData);

    GuetzliImage outImage = guetzliImageNew(GUETZLI_IMAGE_TYPE_JPEG, outData.size());
    // @todo outImage.data = outData.c_str();
    return outImage;
}

GuetzliRgbArray guetzliRgbArrayNew(int width, int height) {
    GuetzliRgbArray array;
    array.width = width;
    array.height = height;
    array.data = new unsigned char[array.width * array.height];
    return array;
}

void guetzliRgbArrayFree(GuetzliRgbArray* array) {
    delete[] array->data;
    array->data = nullptr;
    array->width = 0;
    array->height = 0;
}
