from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[1]

def test_analog_policy_and_calendar():
    source=ROOT/'.tmp/policy.c';binary=ROOT/'.tmp/policy'
    source.write_text('''#include <assert.h>
#include "policy.h"
int main(void){
 assert(!leap_year(1900));assert(leap_year(2000));assert(leap_year(2024));assert(!leap_year(2100));
 for(int y=1900;y<=2099;y++)for(int m=1;m<=12;m++)for(int d=1;d<=month_days(y,m);d++){
  Calendar now={y,m,d};assert(valid_date(now));Calendar n=next_day(now),p=previous_day(now),round=previous_day(n),back=next_day(p);
  assert(round.year==y && round.month==m && round.day==d);assert(back.year==y && back.month==m && back.day==d);
 }
 assert(!valid_date((Calendar){2023,2,29}));assert(valid_date((Calendar){2024,2,29}));
 assert(!valid_date((Calendar){2026,0,1}));assert(!valid_date((Calendar){2026,13,1}));assert(!valid_date((Calendar){2026,1,0}));
 for(int h=0;h<24;h++)for(int m=0;m<60;m++){
  assert(hour_angle(h,m)>=0 && hour_angle(h,m)<3600);assert(minute_angle(m)==m*60);
  assert(display_hour(h,2,false)==h);assert(display_hour(h,1,true)==(h%12?h%12:12));
  assert(display_hour(h,0,true)==h);assert(display_hour(h,0,false)==(h%12?h%12:12));
 }
 assert(hour_angle(10,8)==3040);assert(minute_angle(15)==900);assert(second_angle(45)==2700);
 assert(mix_color(0,0xFFFFFF,1)==0x555555);assert(mix_color(0,0xFFFFFF,2)==0xAAAAAA);
 return 0;}
''')
    subprocess.run(['cc','-Wall','-Wextra','-Werror','-I',str(ROOT/'watchface/src/c'),str(source),'-o',str(binary)],check=True)
    subprocess.run([str(binary)],check=True)


def test_fixture_calendar_validation(monkeypatch):
    import runpy
    import pytest
    validate=runpy.run_path(str(ROOT/'watchface/wscript'))['validate_fixture_date']
    for key in ['RAIL_YEAR','RAIL_MONTH','RAIL_DAY']:monkeypatch.delenv(key,raising=False)
    validate()
    for year,month,day in [(0,11,6),(2026,0,6),(2026,11,0),(2026,2,31),(1900,2,29),(2100,1,1)]:
        monkeypatch.setenv('RAIL_YEAR',str(year));monkeypatch.setenv('RAIL_MONTH',str(month));monkeypatch.setenv('RAIL_DAY',str(day))
        with pytest.raises(ValueError):validate()
    monkeypatch.setenv('RAIL_YEAR','2000');monkeypatch.setenv('RAIL_MONTH','2');monkeypatch.setenv('RAIL_DAY','29');validate()
