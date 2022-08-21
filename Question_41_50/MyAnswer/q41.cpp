
#include <opencv2/opencv.hpp>
#include <iostream>
#include <cmath>

using namespace cv;

void show(const Mat arr[], int size, const std::string &s) {
    Mat output;
    cv::hconcat(arr, size, output);
    imshow(s, output);
    waitKey(0);
}

Mat get_angle(Mat &fx, Mat &fy) {
    Mat angle = cv::Mat::zeros(fx.size(), CV_8UC1);
    std::cout << angle;
    for (int i = 0; i < fx.rows; i++) {
        for (int j = 0; j < fx.cols; j++) {
            double division = fx.at<double>(i, j) / (fy.at<double>(i, j) + 1e-7);
            double tan = std::atan(division);
            if ((tan > 0.4142) && (tan <= 2.4142)) {
                angle.at<uchar>(i, j) = 45;
            } else if (abs(tan) >= 2.4142) {
                angle.at<uchar>(i, j) = 90;
            } else if ((tan > -2.4142) && (tan <= -0.4142)) {
                angle.at<uchar>(i, j) = 135;
            }
        }// cols
    }// rows
    return angle;
}

int main() {
    Mat gray = imread("/home/haochen/Projects/ImageProcessing100Wen/Question_41_50/large_img.jpg");
    cv::resize(gray, gray, Size(640, 480));
    cvtColor(gray, gray, COLOR_BGR2GRAY);

    // Gassuian blur
    Mat blur;
    GaussianBlur(gray, blur, Size(5, 5), 1.4);

    // Sobel filter on x and y
    Mat fx, fy;
    Sobel(blur, fx, CV_64FC1, 1, 0, 3);
    Sobel(blur, fy, CV_64FC1, 0, 1, 3);


    // compute edge
    Mat edge;
    cv::magnitude(fx, fy, edge);

    // compute angle
    Mat angle = get_angle(fx, fy);
//    imshow("edge", edge);
//    waitKey(0);
//    imshow("angle", angle);
//    waitKey(0);

}