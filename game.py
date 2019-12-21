import random

# 參加人員
relatedPersons = ["Ru","jerry","andy","yuji","wu"]

#抽
def PickOut():
    pickList = []
    copyRelatedPersons = relatedPersons.copy()
    while(len(copyRelatedPersons)):
        pickName = copyRelatedPersons[random.randint(0,len(copyRelatedPersons)-1)]
        if (pickName not in pickList) and (pickName is not relatedPersons[len(pickList)]):
            pickList.append(pickName)
            copyRelatedPersons.remove(pickName)
    return pickList

def game():
    showpickList = PickOut()
    for i in range(len(showpickList)):
        print(relatedPersons[i] + "的禮物給" + showpickList[i])
        

if __name__ == '__main__':
    game()