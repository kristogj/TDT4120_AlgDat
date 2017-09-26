
BASE = 26

def flexradix(A,d):
    if len(A) <= 1: return A

    ferdig = []
    hauger = [[] for _ in range(BASE)]

    for streng in A:
        if d >= len(streng):
            ferdig.append(streng)
        else:
            hauger[ord(streng[d]) - ord('a')].append(streng)

    hauger = [flexradix(haug, d + 1) for haug in hauger]
    return ferdig + [b for haugene in hauger for b in haugene]


def main():

    liste = [                                 "hest",
                                               "ape",
                                          "zinosaur",
                                              "gris",
                                       "tyranusarus",
                                              "hund",
                                              "katt",
                                                "oh",
            "overbuljongterningpakkemesterassistent"
                                                 ,"66"]

    liste2 = ['z','x','r','j','x','l','p','z','a','b','a','d','t','i','z','z','a','d','e','t']

    liste3 = ["adddddddsoifoidohatt","katt","matt","satt","datt","sldsgat"]

    liste4 = ['6','kobra','alge','agg','kort','hyblen']


    print(flexradix(liste4,0))

   # print(len(liste[0]))


main()