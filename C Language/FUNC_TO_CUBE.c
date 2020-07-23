#include<stdio.h>
double cube(double a);
int main()
{
    double a,b;
    scanf("%lf",&a);
    b=cube(a);
    printf("the cube is: %lf",b);
    return 0;

}
double cube(double d)
{
    double e=d*d*d;
    return e;
}
