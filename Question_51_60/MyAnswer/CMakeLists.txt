cmake_minimum_required(VERSION 3.0)
project(answer)

# Find OpenCV
find_package(OpenCV REQUIRED)

# Include OpenCV directories
include_directories(${OpenCV_INCLUDE_DIRS})

# Add source files
add_executable(answer /Users/haochenyu/Desktop/ImageProcessing100Wen/Question_51_60/MyAnswer/q51.cpp)

# Link OpenCV libraries
target_link_libraries(answer ${OpenCV_LIBS})