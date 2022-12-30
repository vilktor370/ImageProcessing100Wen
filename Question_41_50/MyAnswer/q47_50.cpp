#include <opencv2/opencv.hpp>
#include <iostream>

using std::cout;
using std::endl;
using namespace cv;


const int BIN_THRESHOLD = 127;

int main(){
    Mat image = imread("/Users/haochenyu/Desktop/ImageProcessing100Wen/Question_41_50/test.png", 0);
    if(image.empty()){
        cout << "Fail to load image\n";
        return -1;
    }
    int rows = image.rows;
    int cols = image.cols;
    
    // binarization 
    Mat bin(rows, cols, CV_8UC1, Scalar(255));
    for(int i =0;i< rows;i++){
        for(int j =0;j< cols;j++){
            if(image.at<uchar>(i, j) < BIN_THRESHOLD){
                bin.at<uchar>(i, j) = 0;
            }
        }
    }
    

    Mat kernel(3,3, CV_64FC1, Scalar(1));
    cout << kernel << endl;

    // eroision
    Mat max_img;
    cv::dilate(image, max_img, kernel);
    Mat min_img;
    cv::erode(image, min_img, kernel);

    Mat result, temp;
    cv::erode(image, temp, kernel);
    cv::dilate(temp, result, kernel);

    cv::hconcat(min_img, max_img, min_img);
    cv::hconcat(result, min_img, result);
    cv::hconcat(image, result, image);
    imshow("Errosion, Dialation, E+D, Original", image);
    waitKey(0);
}