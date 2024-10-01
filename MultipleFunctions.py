class MultipleFunctions():
    def Subfields():
        print("Sub Fields in AI are:")
        LISTS1=("Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing")
        for AI in LISTS1:
            print(AI)
    
    def OddEven():
        num=int(input("Enter the number :"))
        if ((num%2)==1):
            print("Given Number is Odd")
        else:
            print("Given Number is Even")
            
    def Marraige():
        gender=input("Enter the Gender is Male/Female: ")
        age=int(input("Enter the Age: "))
        if (gender=="Male" and age>=20) or (gender=="Female" and age>=18):
            print("Your Gender :",gender)
            print("Your Age :",age)
            print("Eligible")   
        else:
            print("Not Eligble")
            
    def percentage():
        Subject1=int(input("Enter your Subject1 Marks: "))
        Subject2=int(input("Enter your Subject2 Marks: "))
        Subject3=int(input("Enter your Subject3 Marks: "))
        Subject4=int(input("Enter your Subject4 Marks: "))
        Subject5=int(input("Enter your Subject5 Marks: "))
        Total=int(Subject1+Subject2+Subject3+Subject4+Subject5)
        Percentage=Total/5
        print("Total Marks: ",Total)
        print("Percentage :",Percentage)
        
    def triangle():
        Height=int(input("Enter Height of Triangle: "))
        Breadth=int(input("Enter Breadth of Triangle: "))
        area=(Height*Breadth)/2
        print("Area of Triange is: ",area)
        Height1=int(input("Enter Height1: "))
        Height2=int(input("Enter Height2: "))
        Breadth=int(input("Enter Breadth: "))
        perimeter=(Height1+Height2+Breadth)
        print("Perimeter of Triangle is: ",perimeter)
        
    