#include <opencv2/opencv.hpp>

#include <iostream>
using std::cout;
using std::endl;
using namespace cv;
int main(int argc, char** argv){

    Mat circle(100, 100, CV_8UC1, Scalar(0));
    cv::Point center(50, 50);
    int radius = 20;
    cv::Scalar color(255);
    int thickness = -1;
    cv::circle(circle, center, radius, color,thickness);
    Mat min_img, max_img;
    Mat ones(3, 3, CV_64FC1, cv::Scalar(1));
    cv::erode(circle, min_img, ones);
    cv::dilate(circle, max_img, ones);
    
    Mat diff = max_img - min_img;
    cv:hconcat(diff, circle, diff);
    imshow("diff original", diff);
    waitKey(0);

}