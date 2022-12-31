#include <opencv2/opencv.hpp>

#include <iostream>
using std::cout;
using std::endl;
using namespace cv;

int main(int argc, char** argv){
    Mat img = imread("/Users/haochenyu/Desktop/ImageProcessing100Wen/Question_71_80/imori.jpg", 1);

    // Gaussian pyramid


    Mat down;
    cv::pyrDown(img , down);

    Mat up;
    cv::pyrUp(down, up);

    // laplacian = original_img = upsample(downSample(img) 
    Mat result = img - up;
    cout << result.channels() << "\n";
    imshow("gray", result);
    waitKey(0);
}