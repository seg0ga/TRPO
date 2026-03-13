#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include <thread>

using namespace std;
using namespace chrono;

void gemm_parallel(int M,int N,int K,double alpha,const double* A,const double* B,double beta,double* C,int num_threads){
    vector<thread> threads;
    int rows_per_thread=M/num_threads;

    for (int t=0;t<num_threads;++t){
        int start_row=t*rows_per_thread;
        int end_row=(t==num_threads-1)?M:start_row+rows_per_thread;

        threads.emplace_back([=,&A,&B,&C](){
            for (int i=start_row;i<end_row;++i){
                for (int j=0;j<N;++j){
                    double sum=0;
                    for (int k=0;k<K;++k){
                        sum+=A[i*K+k]*B[k*N+j];}
                    C[i*N+j]=alpha*sum+beta*C[i*N+j];}}});}

    for (auto& t:threads){t.join();}}

double test_gemm(int M,int N,int K,int num_threads){
    vector<double> A(M*K);
    vector<double> B(K*N);
    vector<double> C(M*N,0.0);

    for (int i=0;i<M*K;i++) A[i]=rand()%100;
    for (int i=0;i<K*N;i++) B[i]=rand()%100;

    double alpha=1.0,beta=0.0;

    auto start=high_resolution_clock::now();

    gemm_parallel(M,N,K,alpha,A.data(),B.data(),beta,C.data(),num_threads);

    auto end=high_resolution_clock::now();
    return duration<double>(end-start).count();}

int main(){
    cout<<"Моя реализация GEMM - ДВОЙНАЯ ТОЧНОСТЬ\n";
    int M=3000, N=3000, K=3000;
    cout<<"Размер матриц: "<<M<<" x "<<N<<" x "<<K<< "\n\n";
    cout<<"-----------------------------------------\n";
    cout<<"| Потоки | Попытка |   Время (сек)     |\n";
    cout<<"-----------------------------------------\n";

    int threads[]={1,2,4,8,16};

    for (int t:threads){
        for (int run=0;run<10;run++){
            double time=test_gemm(M,N,K,t);
            cout<<"|   "<<setw(2)<<t<<"    |   "<<setw(2)<<run+1<<"    | "
                 <<fixed<<setprecision(3)<<setw(12)<<time<<"     |\n";}
        cout<<"-----------------------------------------\n\n";}
}