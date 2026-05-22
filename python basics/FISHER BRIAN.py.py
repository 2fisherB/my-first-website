#NAME : FISHER BRIAN
#LEVEL : 100LEVEL
#CLASS : COMPUTER SCIENCE DEPARTMENT
#REG NO. : 2501640
#MATRIC NO. : 25CD011690
# QUESTION 1 : A PROGRAM ASSIGNING REG NO TO ALL STUDENTS OF 100LVL STUDENTS

names = [
"John","David","Israel","Moses","Abraham","Ade","Dami","Josh","Paul","Peter",
"James","Samuel","Daniel","Joseph","Michael","Emmanuel","Isaac","Jacob","Noah","Elijah",
"Ethan","Liam","Lucas","Mason","Logan","Henry","Jackson","Aiden","Matthew","Sebastian",
"Olu","Tunde","Sola","Kemi","Bola","Femi","Tosin","Kunle","Yemi","Bisi",
"Zainab","Aisha","Fatima","Hassan","Usman","Sadiq","Ibrahim","Abdul","Yusuf","Ali",
"Chinedu","Emeka","Ifeanyi","Obinna","Uche","Kelechi","Nnamdi","Chisom","Somto","Amaka",
"Blessing","Precious","Divine","Favor","Victory","Miracle","Angel","Joy","Peace","Grace",
"Hope","Faith","Charity","Glory","Queen","King","Prince","Princess","Bright","Smart",
"Excel","Success","Marvel","Wisdom","Knowledge","Power","Justice","Unity","Liberty","Freedom",
"Alpha","Beta","Gamma","Delta","Omega","Zion","Eden","Cyrus","Xavier","Zara"
]

for i in range(100):
    matric_no = "250CD10" + str(i+1).zfill(3)
    print("Name:", names[i], "| Reg No:", matric_no)

# QUESTION 2 : WRITE THE PYTHON PROGRAM THAT LISTS ALL THE MANAGEMENT STAFFS OF LANDMARK UNIVERSITY