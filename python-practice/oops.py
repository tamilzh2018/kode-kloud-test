""" class person:
    
    def people(self,name,age, gender):
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        gender=input("Enter you gender: ")
        print(f"Person Name is: {name}, his age is: {age} and his gender is: {gender}")
p=person()
p.people('name','age','gender') """

#Area of a Room
class Room:
    
    def cal_area_of_room(self,length,breadth):
        length=float(input("Enter the length of the room: "))
        breadth=float(input("Enter the breadth of the room: "))
        print("Area of the Room is:", length*breadth)
area=Room()
area.cal_area_of_room('length','breadth')
