import subprocess
import time
def contact():
    subprocess.call(['notepad.exe', 'docs\contact.txt'])
def docmain():
    subprocess.call(['notepad.exe', 'docs\doc1.txt'])
def docex():
    subprocess.call(['notepad.exe', 'docs\doc2.txt'])
def main():
    print("This is free and open source software, if you paid for this you were scammed")
    print("Made by EZTLI on earth by humans roughly 2024 rotations around the sun after the death of our savior")
    print("Version MAIN1.1")
    # the following is obsolete due in the s3header version
    #help = input("Would you like to read documentation?: y/n?")
    #if help == "y":
       #subprocess.call(['notepad.exe', "docs\doc1.txt"])
        #exit(0)
    #elif help == "n":
        #print("okay")
    #else:
        #print("exit code 0")
        #exit()
    fn = input("Enter filename: ")
    print(fn)
    with open(fn, "r", encoding="utf-8") as file:
        ksfile = file.read()
    print(ksfile)
    print("-----------\n\n")
    new_string0 = ksfile.replace(">", "age:            ")
    new_string1 = new_string0.replace("~", "name:           ")
    new_string2 = new_string1.replace("#", "phone:          ")
    new_string3 = new_string2.replace("&", "family:         ")
    new_string4 = new_string3.replace("^", "associates:     ")
    new_string5 = new_string4.replace("_@", "emails:         ")
    new_string6 = new_string5.replace("!", "address:        ")
    new_string7 = new_string6.replace("*", "state/province: ")
    new_string8 = new_string7.replace("$", "city/town:      ")
    new_string9 = new_string8.replace("-", "apt/suite:      ")
    new_stringa = new_string9.replace("//", "comments:       ")
    new_stringb = new_stringa.replace("`", "file/image:     ")
    new_stringc = new_stringb.replace(";", "ip address:     ")
    new_stringd = new_stringc.replace("_tt", "tiktok          ")
    new_stringe = new_stringd.replace("_yt", "youtube         ")
    new_stringf = new_stringe.replace("_sc", "snapchat        ")
    new_stringg = new_stringf.replace("_dc", "discord         ")
    new_stringh = new_stringg.replace("_ds", "discord server  ")
    new_stringi = new_stringh.replace("_ex", "extra social    ")
    new_stringj = new_stringi.replace("'\\'", "end comment     ")
    new_stringk = new_stringj.replace(",", ", ")
    fstr = new_stringk.replace("?", "unknown ")
    print(fstr)
    fn2 = input("Enter output filename: ")
    fw = open(fn2, "w", encoding="utf-8")
    fw.write(fstr)
    print("Done writing output file")

def ex():

    print("This is free and open source software, if you paid for this you were scammed")
    print("Made by EZTLI on earth by humans roughly 2024 rotations around the sun after the death of our savior")
    print("Version EX1.1 ")
    # the following is obsolete due in the s3header version
    #help = input("Would you like to read documentation?: y/n?: ")
    #if help == "y":
    #    subprocess.call(['notepad.exe', "docs\doc2.txt"])
    #    exit()
    #elif help == "n":
    #    print("okay")
    #else:
    #    print("exit code 0")
    #    exit()
    fn = input("Enter filename: ")
    print(fn)
    with open(fn, "r", encoding="utf-8") as file:
        ksfile = file.read()
    print(ksfile)
    print("-----------\n\n")
    new_string0 = ksfile.replace("_ag", "age:            ")
    new_string1 = new_string0.replace("_n", "name:           ")
    new_string2 = new_string1.replace("_p", "phone:          ")
    new_string3 = new_string2.replace("_f", "family:         ")
    new_string4 = new_string3.replace("_w", "work:           ")
    new_string5 = new_string4.replace("_e", "emails:         ")
    new_string6 = new_string5.replace("_ad", "address:        ")
    new_string7 = new_string6.replace("_sp", "state/province: ")
    new_string8 = new_string7.replace("_ct", "city/town:      ")
    new_string9 = new_string8.replace("_as", "apt/suite:      ")
    new_stringa = new_string9.replace("//", "comments:       ")
    new_stringb = new_stringa.replace("_h", "file/image:     ")
    new_stringc = new_stringb.replace("_ip", "ip address:     ")
    new_stringd = new_stringc.replace("_tt", "tiktok          ")
    new_stringe = new_stringd.replace("_yt", "youtube         ")
    new_stringf = new_stringe.replace("_sc", "snapchat        ")
    new_stringg = new_stringf.replace("_dc", "discord         ")
    new_stringh = new_stringg.replace("_ds", "discord server  ")
    new_stringi = new_stringh.replace("_ex", "extra social    ")
    new_stringj = new_stringi.replace("'\\'", "end comment     ")
    new_stringk = new_stringj.replace(",", ", ")
    fstr = new_stringk.replace("?", "unknown ")
    print(fstr)
    fn2 = input("Enter output filename: ")
    fw = open(fn2, "w", encoding="utf-8")
    fw.write(fstr)
    print("Done writing output file")
# new r/w functions
def readfile(fnr):
    with open(fnr, "r", encoding="utf-8") as file:
        fr = file.read()
    print(fr)
    input()
def writefile(fnw, data):
    fw = open(fnw, "w", encoding="utf-8")
    fw.write(data)
    print(fw)