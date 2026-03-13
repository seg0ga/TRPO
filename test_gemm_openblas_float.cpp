#include <cblas.h>
#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include <thread>

using namespace std;
using namespace chrono;

float test_gemm(int M,int N,int K,int num_threads){
    openblas_set_num_threads(num_threads);
    vector<float> A(M*K);
    vector<float> B(K*N);
    vector<float> C(M*N,0.0f);

    for (int i=0;i<M*K;i++) A[i]=rand()%100;
    for (int i=0;i<K*N;i++) B[i]=rand()%100;

    float alpha=1.0f,beta=0.0f;

    auto start=high_resolution_clock::now();

    cblas_sgemm(CblasRowMajor,CblasNoTrans,CblasNoTrans,M,N,K,alpha,A.data(),K,B.data(),N,beta,C.data(),N);
    auto end=high_resolution_clock::now();
    return duration<float>(end-start).count();}

int main(){
    cout<<"Тестирование производительности GEMM (OpenBLAS) - float\n";
    int M=3000, N=3000, K=3000;
    cout<<"Размер матриц: "<<M<<" x "<<N<<" x "<<K<< "\n\n";
    cout << "-----------------------------------------\n";
    cout << "| Потоки | Попытка |   Время (сек)     |\n";
    cout << "-----------------------------------------\n";
    int threads[]={1,2,4,8,16};
    for (int t:threads){
        for (int run=0;run<10;run++){
            float time=test_gemm(M,N,K,t);
            cout<<"|   "<<setw(2)<<t<<"    |   "<< setw(2)<<run+1<<"    | "<<fixed<<setprecision(3)<<setw(12)<<time<<"     |\n";}
        cout << "-----------------------------------------\n\n";}}