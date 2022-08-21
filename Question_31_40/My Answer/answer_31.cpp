
#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;


int main() {
    Mat image;
    image = imread("/home/haochen/Projects/ImageProcessing100Wen/Question_31_40/imori.jpg");
    if (!image.data) {
        printf("No image data \n");
        return -1;
    }
    Mat transMtx = cv::Mat::eye(2, 3, CV_32FC1);
    float tx = 30;
    float ty = 30;
    float x_axis = (float) (tx / image.rows);
    float y_axis = (float) (ty / image.cols);
    transMtx.at<float>(0, 1) = x_axis;
    transMtx.at<float>(1, 0) = y_axis;
    Mat final;
    cv::warpAffine(image, final, transMtx, image.size());

    namedWindow("Display Image", WINDOW_GUI_NORMAL);
    imshow("Display Image", final);
    waitKey(0);
    return 0;
}