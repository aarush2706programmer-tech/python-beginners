class student:
    school = "DPS Pune"
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = []
    
    def add_mark(self,subject,score):
        self.marks.append({"subject":subject,"score":score})
        print(f"Added {subject}:{score} for {self.name}")
    
    def avg(self):
        if not self.marks:
            return 0
        total = sum(m["score"] for m in self.marks)
        #for m in self.marks["score"]
        return round(total/(len(self.marks)))

    def is_passing(self,pass_mark =40):
        return self.avg()>=pass_mark
    
    def report(self):
        print(f"=== {self.name} === {self.grade}")
        for m in self.marks:
            print(f"{m["subject"]:12} {m["score"]}")
            print(f"Average : {self.avg()}")
            print(f"Status : {'Pass'if self.is_passing()else 'Fail'}")

s1 = student("Aarush",12,8,)
s1.add_mark("Maths",90)
s1.add_mark("Science",85)
s1.add_mark("English",91)
print(s1.avg())
print(s1.is_passing())
s1.report()


