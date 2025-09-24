import json
class task:
    def __init__(self,title,description,status="pending"):
        self.title=title
        self.description=description
        self.status=status
    def mark_done(self):
        self.status="done"
    def update(self,newtitle=None,newdescription=None):
        if newtitle: 
            self.title=newtitle
        if newdescription:
            self.description=newdescription
    def __str__(self):
        return (f"title:{self.title},description:{self.description},status:{self.status}")
class taskmanager:
    def __init__(self):
        self.tasks=[]
    def addtask(self,title,description):
        newtask=task(title,description)
        self.tasks.append(newtask)
        print(f"task {newtask.title} added successfully")
    def deletetask(self,title):
        found=False
        for task in self.tasks:
            if task.title==title:
                self.tasks.remove(task)
                print("removed")
                found=True
                break
        if not found:
            print("not found")
    def update(self,title,newtitle=None,newdescription=None):
        found=False
        for task in self.tasks:
            if task.title==title: 
                task.update(newtitle,newdescription)
                print(f"task {task.title} updated")
                found=True
                break
        if not found:
            print("task not found")
    def markdone(self,title):
        found=False
        for task in self.tasks:
            if task.title==title:
                task.mark_done()
                print(f"task {title} marked as done")
                found=True
                break
        if not found:
            print("task not found")
    def show(self):
        for t in self.tasks:
            print(t)
        if not self.tasks:
            print("tasks not found")
    def showstatus(self):
        for task in self.tasks:
                print(f"{task.title},{task.status}")
    def save(self,filename="tasks.json"):
        sdata=[tasktodic(s) for s in self.tasks]
        with open(filename, "w") as f:
            json.dump(sdata,f,indent=4)
    def load(self,filename="tasks.json"):
        try:
            with open(filename,"r") as f:
                data=json.load(f)
                self.tasks=[dictotask(d) for d in data]
        except FileNotFoundError:
            print("no file exsists")


def tasktodic(task):
    return {
        "title" : task.title,
        "description" : task.description,
        "status" : task.status
    }
def dictotask(d):
    return task(d["title"],d["description"],d["status"])
    
manager=taskmanager()
manager.addtask("assignment","complete python project")
manager.update("assignment",newdescription="start working on django")
manager.addtask("presentation","practice interview")
manager.markdone("assignment")
manager.show()
manager.showstatus()
manager.save()