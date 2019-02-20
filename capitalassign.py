from itertools import groupby
class named_solution:
    def groupAnagrams(ar):
        a2=[list(group) for key,group in groupby(sorted(ar,key=sorted),sorted)]
        a2.sort(reverse=True,key=len)
        print("[",sep="")
        for i in a2:
            print("\n",i,)

        print("\n]")

    if __name__=="__main__":
        a=['eat','tea','tan','ate','nat','bat']
        groupAnagrams(a)