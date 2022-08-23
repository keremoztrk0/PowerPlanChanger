import subprocess

class PowerManager:

    __PowerPlans = []

    def getPowerPlans(self):
        list = subprocess.Popen(
            ['powercfg', '-list'], stdout=subprocess.PIPE).communicate()[0].decode().splitlines()

        # first 3 item is not necessary item. Codeline deleting unnecessary items
        for i in range(3):
            list.pop(0)

        for plan in list:
            plan = plan.split(" ")

            #deleting non using indexes
            willDeleteIndexes= [0,1,2,4]
            for index in sorted(willDeleteIndexes,reverse=True):
                del plan[index]
            
            #this code block combining the string between pharanteses to one index item
            pharantesisStartIndex=0
            pharantesisEndIndex=0
            isActive=False
            for i in range(len(plan)):
                if plan[i].startswith("("):
                    pharantesisStartIndex = i
                elif plan[i].endswith(")"):
                    pharantesisEndIndex = i
                    plan[pharantesisStartIndex] = " ".join(plan[pharantesisStartIndex:pharantesisEndIndex+1])
                    plan.pop(pharantesisEndIndex)
                    break



            if plan[-1] == "*":
                isActive=True
                
            
            #Index 0 for GUID
            #Index 1 for Plan Name
            

            self.__PowerPlans.append(PowerPlan(plan[0], plan[1],isActive))
        return self.__PowerPlans
    def setPowerPlan(self,guid:str):
        subprocess.run(["powercfg","-s",guid])
        for plan in self.__PowerPlans:
            if plan.Guid == guid:
                plan.Active = True
            else:
                plan.Active = False

class PowerPlan:
    def __init__(self, guid, name,active=False):
        self.Guid = guid
        self.Name = name
        self.Active=active
