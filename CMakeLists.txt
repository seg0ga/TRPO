cmake_minimum_required(VERSION 3.10)
project(GEMM_Test)

set(CMAKE_CXX_STANDARD 11)

find_package(OpenBLAS REQUIRED)

if(OpenBLAS_FOUND)
    include_directories(${OpenBLAS_INCLUDE_DIR})

    add_executable(test_gemm_openblas test_gemm_openblas_double.cpp)
    target_link_libraries(test_gemm_openblas ${OpenBLAS_LIBRARY})

    find_package(OpenMP)
    if(OpenMP_CXX_FOUND)
        target_link_libraries(test_gemm_openblas OpenMP::OpenMP_CXX)
    endif()
endif()