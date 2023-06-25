# Python boshlgicch xpericelar

# If-elif_else
# 06.24
#yosh=int(input("Yoshingiz nechida ?"))
#if yosh<=4:
#  narx=5000 
#elif yosh<=10:
#  narxi=7000 
#elif yosh==18:
#   narxi=8000
#else:
  #narx=10000
##print(f"Sizga kirish narxi {narx}")

#kun=input("Bugun kun nima ?")
#if kun.lower()=="shanba " or kun.lower()=="yakshanba":print("bugun dam olish kuni")
#else: print("Bugun ish kuni")

#x=int(input("x son kiriting"))
#y=int(input("y sonni kiriting"))
#z=int(input("z sonini kiriting"))
#if x==y and y!=z: print("Bu teng yonli uchburchak")
#elif x!=y and y!=z: print("Bu turli tomoli uchburhak")
#else:print("Bu teng tomonl uchburchak")


#dostlar = []
#print("Which programming languages do you know?")

#for n in range(3):
#    dost = input(f"{n+1}--ismini kiriting: ")
#    dostlar.append(dost)

#print(f"Siz {dostlar}")

#skills = []
#print("Which programming languages do you know?")

#for n in range(2):
#    skill = input(f"{n+1} - Enter a programming language you know: ")
#    skills.append(skill)

#skills = list(set(skills))  # Convert the skills list to remove duplicates

#gpa = float(input("Enter your GPA score: "))

#if "Python" in skills and "C++" in skills and gpa >= 3.0:
#    print("You can apply to AI development.")
#elif "Python" in skills or "Html" in skills and gpa <= 3.0:
#    print("You can apply as a 3D designer.")
#elif "Html" in skills and ("C++" in skills or "C#" in skills) and gpa >= 3.0:
#    print("You can apply as a frontend developer.")
#else:
  #  print("You can choose your desired career path.")

#narh=50000           #mijoz 50000 so`mga ovqat oldi
#choy=1    # yoki      True choy oldi         True=1
#salat=0   # yoki     False #salat olmadi    False=0
#non= 1
#napitka=1
#if choy and salat:      #agar mijoz salat ham choy olgan bo`lsa
 #narh=narh+25000       #  narhga 25min qoshiladi
#elif choy or salat:     # choy yoki salat olgan bolsa
#  narh=narh+10000
#print(f" Jami {narh} bo`ldi") #natija Jami 60000 bo`ldi --> choy true olingan , salat false olinmagan uchun elif sharti bajarilib narhga 10min gqoshialdi
#//

#if choy:
  #print("Mijoz choy sotb oldi")
 # narh=narh+5000
#if napitka:
 # print("Mijoz cola oldi")
 # narh=narh+9000
#if non:
#  print("Mijoz non oldi")
 # narh=narh+15000
#print(f"Jami {narh}")

#menu=['osh','manti', 'qozonkabob','somsa']
#///////"somsa" in menu
#ovqat=input("Nima buyurtma qilasiz ? ")
#if ovqat.lower() not in menu:
#  print("Kechirasiz bunday ovqat yoq")
#else:
 # print("Buyurtma qabul qilindi")

#menu=['manti', 'qozonkabob','somsa',"biqtirma", "shashlik"]
#buyurtmalar=["osh","manti", "somsa","baliq"]
#if buyurtmalar:
#   for taom in buyurtmalar:
 #    if taom  in menu:
  #     print(f"Bizda {taom}bor")
   #  else:
    #   print(f"Kechirasiz bizda {taom} yoq")  #Kechirasiz bizda osh yoq
                                           #Bizda mantibor
                                           #Bizda somsabor
                                           #Kechirasiz bizda baliq yoq

# 06.25
#     Xatolar bilan ishlash

#print("yigirmagacha sanaymiz")
#for n in range(20):
# print(n+1)
# Type error
#son=input("Istalgan son kv toping")
#print(f"{son} ning kvadrati {son**2} ga teng") #TypeError: unsupported operand 
                                               #type(s) for ** or pow(): 'str' and 'int'

# Name error  kiritlgan so`z hatoligi
 # for examp. 
#prin(t)("Hello world") # natija NameError: name 'prin' is not defined. Did you mean: 'print'?

# Value error qiymat hatoligi
#son=int(input("istalgan sonni kiriting")) #masalan 34.6  bunday o`nlik sonlarni float() sifatida kiritiladi
#if son>=0:  
 # print("Musbat son")
#else:
 # print("Manfiy son")    #Natija: #ValueError: invalid literal for int() with base 10: '34.6'

# Index error  indeks xatoligi
#mevalar=['anor','olcha', 'orik'] # bu yerda 0dan 2gacha indekslangan
#print(mevalar[3]) #natija IndexError: list index out of range

# ZeroDivisionError qiymatni 0ga bo`lish xatoligi
#x,y=60,60
#z=342/(x-y)
#print(z) # natija :: ZeroDivisionError: division by zero chunki s

#son = float(input("Juft son kiriting: "))
#if son % 2== 0:
#  print("Bu juft son")
#else:
#  print("Bu juft son emas")

yosh = int(input("Yoshingiz nechida?"))
if yosh<=4 or yosh<=6:
     narh = 0
elif yosh < 18:
     narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")


    























