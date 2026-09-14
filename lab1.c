#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

double f(double x){return sqrt(x*(3.0-x))/(x+1.0);}

double SimpsonMethod(double a,double b,unsigned n){
    double h=(b-a)/n;
    double sum=0;
    #pragma omp parallel for reduction(+:sum)
    for (unsigned i=0;i<n;i++){
        double x0=a+i*h;
        double x1=x0+h;
        sum+=f(x0)+4*f(x0+h/2.0)+f(x1);}
    return (h/6.0)*sum;}

double SimpsonAdaptive(double a,double b,double eps,unsigned *n_out){
    unsigned n=4;
    double I_prev=SimpsonMethod(a,b,n);
    double I_curr;
    for (;;){
        n*=2;
        I_curr=SimpsonMethod(a,b,n);
        if (fabs(I_curr-I_prev)/15.0<eps) break;
        I_prev=I_curr;}
    *n_out=n;
    return I_curr;}

double get_time_us(){
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec*1e6+ts.tv_nsec/1e3;}

int main(void){
    const double a=1.0;
    const double b=1.2;
    const double eps=1e-6;

    double start,end,duration;
    double result;
    unsigned n_used;

    int threads[]={1,2,4,8,16,32,64};
    int num_threads=sizeof(threads)/sizeof(threads[0]);

    printf("Потоков | Время, мс |   n  |   Интеграл\n");
    printf("--------|-----------|------|----------------\n");

    for (int t=0;t<num_threads;t++){
        omp_set_num_threads(threads[t]);
        n_used=0;
        start=get_time_us();
        result=SimpsonAdaptive(a,b,eps,&n_used);
        end=get_time_us();
        duration=end-start;
        printf("  %3d   | %9.0f | %4u | %.10lf\n",threads[t],duration,n_used,result);}}
