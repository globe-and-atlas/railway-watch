#pragma once
#include <stdbool.h>
#include <stdint.h>
typedef struct{int year,month,day;} Calendar;
static inline bool leap_year(int y){return y%4==0 && (y%100!=0 || y%400==0);}
static inline int month_days(int y,int m){const int d[]={31,28,31,30,31,30,31,31,30,31,30,31};return m==2?28+leap_year(y):d[m-1];}
static inline bool valid_date(Calendar d){return d.year>=1900 && d.year<=2099 && d.month>=1 && d.month<=12 && d.day>=1 && d.day<=month_days(d.year,d.month);}
static inline Calendar previous_day(Calendar d){if(--d.day<1){if(--d.month<1){d.month=12;d.year--;}d.day=month_days(d.year,d.month);}return d;}
static inline Calendar next_day(Calendar d){if(++d.day>month_days(d.year,d.month)){d.day=1;if(++d.month>12){d.month=1;d.year++;}}return d;}
static inline int minute_angle(int m){return m*60;}
static inline int hour_angle(int h,int m){return (h%12)*300+m*5;}
static inline int second_angle(int second){return second*60;}
static inline bool uses24(int mode,bool watch24){return mode==2 || (mode==0 && watch24);}
static inline int display_hour(int h,int mode,bool watch24){return uses24(mode,watch24)?h:(h%12?h%12:12);}
static inline uint32_t mix_color(uint32_t a,uint32_t b,int weight){uint32_t result=0;for(int shift=0;shift<=16;shift+=8){int value=((((a>>shift)&255)*(3-weight)+((b>>shift)&255)*weight)/3);result|=(uint32_t)(((value+42)/85)*85)<<shift;}return result;}
