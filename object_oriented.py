class Fraction():
    def __init__(self,n,d):

        self.numerator=n
        self.denominator=d

    #methods
    def sum(self):
        ...
    def subtract(self):
        ...
    def multiplay(self):
        ...
    def division(self):
        ...
 
fraction_equal_to_zero=Fraction(0,...)
fraction_equal_to_one=Fraction(...,...)
fraction_equal_to_infinity=Fraction(...,0)
fraction_greater_than_one=Fraction(...,...)
Fraction_smaller_than_unit=Fraction(...,...)





class Time():
    def __init__(self,ms,s,m,h):
        self.milisec=ms
        self.sec=s
        self.min=m
        self.hour=h

#methods:
    def convert_milisec_to_sec(self):
        ...
    def convert_milisec_to_min(self):
        ...
    def convert_milisec_to_hour(self):
        ...
    def convert_sec_to_min(self):
        ...
    def convert_sec_to_hour(self):
        ...
    def convert_min_to_sec(self):
        ...
    def convert_min_to_hour(self):
        ...
    def convert_hour_to_sec(self):
        ...
    def convert_hour_to_min(self):
        ...
    def convert_day_to_hour(self):
        ...
    def convert_week_to_hour(self):
        ...
    def convert_month_to_hour(self):
        ...
    def convert_year_to_hour(self):
        ...
    def convert_day_to_min(self):
        ...
    def convert_week_to_min(self):
        ...
    def convert_month_to_min(self):
        ...
    def convert_year_to_min(self):
        ...
    def convert_day_to_sec(self):
        ...
    def convert_week_to_sec(self):
        ...
    def convert_month_to_sec(self):
        ...
    def convert_year_to_sec(self):
        ...
    def convert_day_to_milisec(self):
        ...
    def convert_week_to_milisec(self):
        ...
    def convert_month_to_milisec(self):
        ...
    def convert_year_to_milisec(self):
        ...
    
day=Time(86.4,86400,1440,24)
weeh=Time(604.8,604800,10080,168)
month=Time(2419.2,2419200,40320,672)
year=Time(29030.4,29030400,483840,8064)




class Date():
    def __init__(self,d,m,y):

        self.day=d
        self.month=m
        self.year=y

    #methods
    def Convert_solar_date_to_lunar_date(self):
        ...
    def Convert_solar_date_to_Gregorian_date(self):
        ...
    def Convert_lunar_date_to_solar_date(self):
        ...
    def Convert_lunar_date_to_Gregorian_date(self):
        ...
    def Convert_Gregorian_date_to_solar_date(self):
        ...
    def Convert_Gregorian_date_to_lunar_date(self):
        ...


Date_of_marriage=Date(25,1,1391)
Date_of_birthday=Date(18,10,1369)
Date_of_Enghelab=Date(22,11,1357)
