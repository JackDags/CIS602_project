'''
scan list
if object at element not in unique list, add it
if object in unique list, go to object, add to appropriate lists
return list
done
'''

def unique(list):

    uniqueList = []
    uniqueList.append(list[0])

    for i in range(1, len(list)-57):
        equal = False
        for j in range(len(uniqueList)):
            if list[i].data == uniqueList[j].data:
                equal = True
                print("{} and {} which is {} and {}".format(i, j, list[i].d.get("filename"), uniqueList[j].d.get("filename")))
                uniqueList[j].d.get("mac_daddr").extend(list[i].d.get("mac_daddr"))
                uniqueList[j].d.get("src_ipn").extend(list[i].d.get("src_ipn"))
                uniqueList[j].d.get("dst_ipn").extend(list[i].d.get("dst_ipn"))
                uniqueList[j].d.get("srcport").extend(list[i].d.get("srcport"))
                uniqueList[j].d.get("dstport").extend(list[i].d.get("dstport"))
        if not equal:
            uniqueList.append(list[i])

    return uniqueList



