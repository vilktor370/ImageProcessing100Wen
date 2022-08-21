
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <vector>

using namespace cv;

Mat getGrayScale(Mat &m) {
    std::vector<Mat> channels;
    split(m, channels);
    Mat gray = channels[0] * 0.0722 + channels[1] * 0.7152 + channels[2] * 0.2126;
    return gray;
}

int main() {
    Mat image;
    image = imread("/home/haochen/Projects/ImageProcessing100Wen/Question_31_40/imori.jpg");
    if (!image.data) {
        printf("No image data \n");
        return -1;
    }
    Mat gray = getGrayScale(image);
    // add extra dimension
    Mat plane[2] = {Mat_<float>(gray), Mat::zeros(gray.size(), CV_32FC1)};
    Mat dft;
    merge(plane, 2, dft);
    cv::dft(dft, dft);
    cv::split(dft, plane);
    Mat res;
    cv::magnitude(plane[0], plane[1], res);
    std::cout << dft;
    namedWindow("Display Image", WINDOW_GUI_NORMAL);
    imshow("Display Image", res);
    waitKey(0);
    return 0;
}