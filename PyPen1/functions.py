print("I am learning ethical hacking with Python") 
file = open("pentest_report.txt")

def sys_info(): 
    return os.system("systeminfo > sysinfo.txt")

sys_info()

def simple_calc(a,b,c):
    return (a+b)**c  

simple_calc(9,5,1) 
simple_calc(3,4,2) 


