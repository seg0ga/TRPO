#include <cblas.h>
#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include <thread>

using namespace std;
using namespace chrono;

double test_gemm(int M,int N,int K,int num_threads){
    openblas_set_num_threads(num_threads);
    vector<double> A(M*K);
    vector<double> B(K*N);
    vector<double> C(M*N,0.0);

    for (int i=0;i<M*K;i++) A[i]=rand()%100;
    for (int i=0;i<K*N;i++) B[i]=rand()%100;

    double alpha=1.0,beta=0.0;

    auto start=high_resolution_clock::now();

    cblas_dgemm(CblasRowMajor,CblasNoTrans,CblasNoTrans,M,N,K,alpha,A.data(),K,B.data(),N,beta,C.data(),N);
    auto end=high_resolution_clock::now();
    return duration<double>(end-start).count();}

int main(){
    cout<<"Тестирование производительности GEMM (OpenBLAS)\n";
    int M=16000,N=16000,K=16000;
    cout<<"Размер матриц: "<<M<<" x "<<N<<" x "<<K<< "\n\n";
    cout << "-----------------------------------------\n";
    cout << "| Потоки | Попытка |   Время (сек)     |\n";
    cout << "-----------------------------------------\n";
    int threads[]={1,2,4,8,16};
    for (int t:threads){
        for (int run=0;run<10;run++){
            double time=test_gemm(M,N,K,t);
            cout<<"|   "<<setw(2)<<t<<"    |   "<< setw(2)<<run+1<<"    | "<<fixed<<setprecision(3)<<setw(12)<<time<<"     |\n";}
        cout << "-----------------------------------------\n\n";}}