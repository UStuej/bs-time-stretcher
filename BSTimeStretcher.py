from time import sleep
from os import remove

def popinstring(strg,pops):
    pops.sort()
    strg_list = list(strg)
    strg_out = str()
    for i in pops:
        strg_list.pop(i)
        for i2 in range(len(pops)):
            pops[i2] -= 1
    for char in strg_list:
        strg_out += char
    return(strg_out)

def leastvalue(lst):
    lst.sort()
    return(lst[0])

    for char in strg_list:
        strg_out += char
    return(strg_out)

def clynb(strg):
    strg = strg.lower()
    if strg == "y":
        return(True)
    elif strg == "n":
        return(False)
    else:
        print("try again...")
        sleep(1)
        quit()

lvlp = "CustomSongs/" + input("Please provide path to level folder (use /):\t.../CustomSongs/")

f = None
try:
    f = open(lvlp+"/info.json","r")
    f.close()
except FileNotFoundError:
    print("FileNotFoundError:  Level does not exist!")
    sleep(1)
    quit()

for dif in ("Easy","Normal","Hard","Expert","ExpertPlus"):
    try:
        f = open(lvlp+"/"+dif+".json","r")
        data_list = f.read().split('"')
        f.close()
        
        sf = None
        so = None
        if dif == "ExpertPlus":
            sf = float(popinstring(data_list[6],[0,len(data_list[6]) - 1])) / float(input("Please provide old BPM for Expert+ difficulty:\t"))
            so = clynb(input("Do you want to stretch obstacle durations for Expert+ difficulty? (y/n):\t"))
        else:
            sf = float(popinstring(data_list[6],[0,len(data_list[6]) - 1])) / float(input("Please provide old BPM for "+dif+" difficulty:\t"))
            so = clynb(input("Do you want to stretch obstacle durations for "+dif+" difficulty? (y/n):\t"))
        final_data_tw = str()
        offseti = 18
        
        try:
            while True:
                if so:
                    if leastvalue([data_list.index("_time",offseti) - offseti,data_list.index("_duration",offseti) - offseti]) == data_list.index("_time",offseti):
                        offseti = data_list.index("_time",offseti) + 1
                        data_list[offseti] = ":" + str(float(popinstring(data_list[offseti],[0,len(data_list[offseti]) - 1])) * sf) + ","
                    elif leastvalue([data_list.index("_time",offseti) - offseti,data_list.index("_duration",offseti) - offseti]):
                        offseti = data_list.index("_duration",offseti) + 1
                        data_list[offseti] = ":" + str(float(popinstring(data_list[offseti],[0,len(data_list[offseti]) - 1])) * sf) + ","
                elif not so:
                    offseti = data_list.index("_time",offseti) + 1
                    data_list[offseti] = ":" + str(float(popinstring(data_list[offseti],[0,len(data_list[offseti]) - 1])) * sf) + ","
        except ValueError:
            pass
        
        for i in range(len(data_list)):
            final_data_tw += data_list[i]
            if i != len(data_list)-1:
                final_data_tw += '"'
                
        remove(lvlp+"/"+dif+".json")
        f = open(lvlp+"/"+dif+".json","w")
        f.write(final_data_tw)
        f.close()
    
    except FileNotFoundError:
        pass

print("Done!")
sleep(0.25)
