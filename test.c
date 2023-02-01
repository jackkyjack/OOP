#include<stdio.h>
int main()
{
    long long n;
    printf("Enter an integer : ");
    scanf("%ld", &n);
    printf("Your number : %ld\n",n);
    printf("variable size : %ld bytes\n", sizeof (n));
    printf("last 3 digits : %ld\n",n%1000);
    printf("next 3 digits : %ld\n",n/1000%1000);
    printf("next 3 digits : %ld\n",n/1000000%1000);
    printf("next 3 digits : %ld\n",n/1000000000%1000);
    printf("comma format : %ld,%03ld,%03ld,%03ld\n", n/1000000000,n/1000000%1000,n/1000%1000,n%1000);
    return 0;
}