#include "guetzli.hpp"

#include <guetzli/quality.h>
#include <guetzli/processor.h>

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>


// GuetzliImage

GuetzliImage* guetzliImageNew(GuetzliImageType type, int length) {
    auto image = new GuetzliImage;
    image->type = type;
    image->length = length;
    image->data = new char[image->length];
    return image;
}

void guetzliImageFree(GuetzliImage* image) {
    delete[] image->data;
    image->data = nullptr;
    image->length = 0;
    delete image;
}

GuetzliImage* guetzliImageReadFile(const char* filename) {
    std::ifstream inFile(filename, std::ios::binary);
    std::vector<char> inBuffer((std::istreambuf_iterator<char>(inFile)), (std::istreambuf_iterator<char>()));

    if (inBuffer.size() == 0) {
        return nullptr;
    }

    // Deducing type
    auto type = GUETZLI_IMAGE_TYPE_UNKNOWN;
    if (inBuffer.size() >= 3 && memcmp(inBuffer.data(), "\xFF\xD8\xFF", 3) == 0) {
        type = GUETZLI_IMAGE_TYPE_JPEG;
    }
    else if (inBuffer.size() >= 8 && memcmp(inBuffer.data(), "\x89PNG\x0D\x0A\x1A\x0A", 8) == 0) {   
        type = GUETZLI_IMAGE_TYPE_PNG;
    }

    // The image indeed
    GuetzliImage* image = guetzliImageNew(type, inBuffer.size());
    memcpy(image->data, inBuffer.data(), image->length);
    return image;
}

void guetzliImageWriteFile(const char* filename, GuetzliImage* image) {
    std::ofstream outFile(filename, std::ios::binary);
    outFile.write(image->data, image->length);
}

GuetzliImage* guetzliImageProcess(GuetzliImage* in, int quality) {
    if (in->type == GUETZLI_IMAGE_TYPE_UNKNOWN) {
        std::cerr << "Unknown image file format." << std::endl;
        return nullptr;
    }

    if (in->type == GUETZLI_IMAGE_TYPE_PNG) {
        std::cerr << "PNG images not supported yet." << std::endl;
        return nullptr;
    }

    std::string inData;
    std::string outData;
    inData.assign(in->data, in->length);

    guetzli::Params params;
    params.butteraugli_target = static_cast<float>(guetzli::ButteraugliScoreForQuality(quality));
    Process(params, nullptr, inData, &outData);

    GuetzliImage* outImage = guetzliImageNew(GUETZLI_IMAGE_TYPE_JPEG, outData.size());
    memcpy(outImage->data, outData.c_str(), outData.length());
    return outImage;
}


// GuetzliRgbArray

GuetzliRgbArray* guetzliRgbArrayNew(int width, int height) {
    auto array = new GuetzliRgbArray;
    array->width = width;
    array->height = height;
    array->data = new char[3 * array->width * array->height];
    return array;
}

void guetzliRgbArrayFree(GuetzliRgbArray* array) {
    delete[] array->data;
    array->data = nullptr;
    array->width = 0;
    array->height = 0;
    delete array;
}

GuetzliImage* guetzliRgbArrayProcess(GuetzliRgbArray* in, int quality) {
    std::vector<uint8_t> inData;
    std::string outData;
    inData.assign(in->data, in->data + (3 * in->width * in->height));

    guetzli::Params params;
    params.butteraugli_target = static_cast<float>(guetzli::ButteraugliScoreForQuality(quality));
    Process(params, nullptr, inData, in->width, in->height, &outData);

    GuetzliImage* outImage = guetzliImageNew(GUETZLI_IMAGE_TYPE_JPEG, outData.size());
    memcpy(outImage->data, outData.c_str(), outData.length());
    return outImage;
}

