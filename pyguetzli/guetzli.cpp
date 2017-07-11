extern "C" {
    #include "guetzli.h"
}

#include <guetzli/quality.h>
#include <guetzli/processor.h>

#include <cstring>  // memcpy
#include <vector>

void guetzli_free_bytes(char** bytes) {
    delete[] *bytes;
    *bytes = nullptr;
}

int guetzli_process_jpeg_bytes(char* bytes_in, int length_in, char** bytes_out, int quality) {
    // Construct the string expected by Guetzli
    std::string inData;
    inData.assign(bytes_in, length_in);

    // Let Guetzli write to a string
    std::string outData;
    guetzli::Params params;
    params.butteraugli_target = static_cast<float>(guetzli::ButteraugliScoreForQuality(quality));
    Process(params, nullptr, inData, &outData);

    // Convert back to specified location
    *bytes_out = new char[outData.size()];
    memcpy(*bytes_out, outData.c_str(), outData.size());
    return outData.size();
}

int guetzli_process_rgb_bytes(char* bytes_in, int width, int height, char** bytes_out, int quality) {
    // Construct the vector expected by Guetzli
    std::vector<uint8_t> inData;
    inData.assign(bytes_in, bytes_in + (3 * width * height));

    // Let Guetzli write to a string
    std::string outData;
    guetzli::Params params;
    params.butteraugli_target = static_cast<float>(guetzli::ButteraugliScoreForQuality(quality));
    Process(params, nullptr, inData, width, height, &outData);

    // Convert back to specified location
    *bytes_out = new char[outData.size()];
    memcpy(*bytes_out, outData.c_str(), outData.size());
    return outData.size();
}

