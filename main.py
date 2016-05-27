# -*- coding: utf-8 -*-

from concepts import *
from recommendation import *
from scaling import *
from pandas101 import *
from graphviz101 import *

def main():

    p = int(input("Number of people in database (<=90)? "))
    f = int(input("Number of movies in database (<50)? "))

    seuilfreq = int(input("What is the frequence threshold (non zero-integer <= people )? "))
    seuilconf = float(input("What is the confidence threshold (percentage) ? "))
    # Query database and find all lattices
    df = data(p,f)
    dfs=scaling(df)
    M = dfs.as_matrix()
    t = compute_lattice(M)
    print(df)
    # Mini UI
    names=dfs.index
    play=1
    while play:
        name=''
        i=0
        print(50*'-')
        while name not in names:
            if i==1:
                print('%s is not a valid name.'%str(name))
            name = input("Name of person to recommend: ")
            type(name)
            i=1
        print(50*'-')

        n=dfs.index.get_loc(name)
        size=len(dfs.columns)
        # Recommendation
        r = recommendation(M, t, n, seuilfreq, seuilconf) # personne, seuil de fréquence, seuil de confiance
        rec = recommendation_str(dfs,df,r,name)
        # Display back
        print(" -- Display dataframe \n")
        print(df)
        #lviz=latticeviz([],[],[],[],['people','movies'],name="ConceptLattice")
        #root2viz(dfs,t,lviz,0)
        #lviz.printf()
        print(rec)
        play = input("Do you want to recommend someone else? ")
        if play in ['Yes','yes','oui','Oui','Ok','ok','OK',1]:
            play=1
        else:
            play=0

main()
