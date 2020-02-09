def seci(seconds):
    ans =""
    
    if seconds < 60:
        if seconds ==1:
            ans += str(seconds)+" second"
        else:
            ans += str(seconds)+" seconds"
        return ans

def minut(seconds):
    minu = seconds//60
    sec = seconds%60
    ans = ""
    if minu ==1:
        ans+= str(minu) +" "+ "minute"
    elif minu !=1:
        ans+= str(minu) +" "+ "minutes"
    if sec!=0:
        ans += " and"+" " +str(seci(sec))
    return ans

def hours(seconds):
    hour = seconds//3600
    min_sec = seconds%3600
    ans = ""
    if hour ==1:
        ans+= str(hour) +" "+ "hour"
    elif hour !=1:
        ans+= str(hour) +" "+ "hours"
    if min_sec!=0:
        mini_seci = str(minut(min_sec))
        if len([i for i in mini_seci.split()])==2:
            ans +=" " +str(minut(min_sec))
        else:
            ans += ","+ " " +str(minut(min_sec))
    return ans

def days(seconds):
    day = seconds//31536000
    ost = seconds%31536000
    ans = ""
    if day ==1:
        ans+=str(day) +" "+ "day"
    elif day !=1:
        ans+= str(day) +" "+ "days"
    if ost!=0:
        ost1 = str(hours(ost))
        if len([i for i in ost1.split()])==2:
            ans +=" " +str(hours(ost))
        else:
            ans += ","+ " " +str(hours(ost))
    return ans



def format_duration(seconds):
    if seconds ==0:
        ans = "now"
        return ans
    if seconds < 60:
        return seci(seconds)
    elif seconds<3600:
        return minut(seconds)
    elif seconds<86400:
        return hours(seconds)
    elif seconds<31536000:
        return days(seconds)

print(format_duration(2597743))
