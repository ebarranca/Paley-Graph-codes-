import pygraphviz as gv
import sys
from math import *

def paley_draw(filename):
    graph = gv.AGraph()
    try:
        infile = open(filename, "r")
    except:
        sys.exit()
    dic = {}
    i=0
    for line in infile:
        app = []
        list_ = line.strip().split()
        length = len(list_)
        for x in list_ :
            app.append(int(x))
        dic[range(length)[i]]= app
        i+=1
    keys = list(range(length))

    #make a dictionary of dictionaries
    #get positions: 
    lis = []
    radius = 4
    for theta in range(length):
      x = cos((2*pi/float(length))*float(theta))*radius
      y = sin((2*pi/float(length))*float(theta))*radius
      lis.append([x,y])

    #field = ["0", "1", "x", "x^2", "x^3", "x^4", "x^5", "2", "x^7", "x^8", "x^9", "x^10", "x^11", "4", "x^13", "x^14", "x^15", "x^16", "x^17", "3", "x^19", "x^20", "x^21", "x^22", "x^23"]
    
    field = ["0", "1", "x", "x^2", "x^3", "2", "x^5", "x^6", "x^7"]

    """ P25
    set1 = [0,23,5,17,11]
    set2 = [12,23,14,22,19]
    set3 = [1,4,5,18,20]
    set4 = [24,5,8,9,22]
    set5 = [12,2,13,4,9]
    set6 = [1,24,14,16,21]
    set7 = [13,16,6,17,8]
    set8 = [14,4,15,6,11]
    set9 = [3,0,15,9,21]
    set10 = [15,18,8,19,10]
    set11 = [23,2,3,16,18]
    set12= [12,17,20,10,21]
    set13 = [2,24,7,10,11]
    set14 = [0,1,13,7,19]
    set15 = [3,6,7,20,22]
    sets = [set1,set2,set3,set4, set5, set6, set7,set8, set9, set10, set11,set12, set13, set14, set15]
    """
    
    #p9
    set1 = [2,4,5]
    set2 = [0,1,5]
    set3 = [1,6,8]
    set4 = [4,6,7]
    set5 = [0,3,7]
    set6 = [2,3,8]
    i=0

    """
    color_list = ["palevioletred", "olivedrab", "dodgerblue","orange", "darkorchid", "crimson", "yellow", "lightpink", "midnightblue", "saddlebrown", "black", "maroon4", "darkgreen", "firebrick", "indigo"]
    i =0
    color_dict = {}
    for key in dic:
      color_dict [key] =[]
    for s in range(len(sets)):
      for el in sets[s]:
        color_dict[el].append(color_list[s])

    for key in dic:
      if len(color_dict[key]) == 0:
        graph.add_node(key, pos = "%f,%f!" %(lis[i][0], lis[i][1]), label = "", shape = "circle")

      elif len(color_dict[key]) ==1:
        graph.add_node(key, pos = "%f,%f!" %(lis[i][0], lis[i][1]), label = "", color = "%s" % (color_dict[key][0]) , style = "filled", shape = "circle")

      elif len(color_dict[key]) ==2:
        graph.add_node(key, pos = "%f,%f!" %(lis[i][0], lis[i][1]), label = "", color = "%s:%s" % (color_dict[key][0], color_dict[key][1]) , style = "filled", shape = "circle")

      elif len(color_dict[key]) ==3:
        graph.add_node(key, pos = "%f,%f!" %(lis[i][0], lis[i][1]), label = "", color = "%s:%s:%s" % (color_dict[key][2], color_dict[key][1], color_dict[key][0]) , style = "filled", shape = "circle")
        
      """
    for key in dic:
      graph.add_node(key, pos = "%f,%f!" %(lis[i][0], lis[i][1]), label = field[i], shape = "circle")
  
      i+=1
      for j in range(len(dic[key])):
          
            if dic[key][j] == 1:
                if key in set1 and j in set1:
                  graph.add_edge(key, keys[j], color= "palevioletred", penwidth =2)
                elif key in set2 and j in set2:
                  graph.add_edge(key, keys[j], color = "olivedrab", penwidth = 2)
                elif key in set3 and j in set3:
                  graph.add_edge(key, keys[j], color = "dodgerblue", penwidth = 2)
                elif key in set4 and j in set4:
                  graph.add_edge(key, keys[j], color = "darkorange3", penwidth = 2)
                elif key in set5 and j in set5:
                  graph.add_edge(key, keys[j], color = "darkorchid", penwidth = 2)
                elif key in set6 and j in set6:
                  graph.add_edge(key, keys[j], color = "crimson", penwidth = 2)
                """
                elif key in set7 and j in set7:
                  graph.add_edge(key,keys[j], color = "goldenrod3", penwidth = 2)
                elif key in set8 and j in set8:
                  graph.add_edge(key, keys[j], color = "hotpink", penwidth = 2)
                elif key in set9 and j in set9:
                  graph.add_edge(key, keys[j], color = "midnightblue", penwidth = 2)
                elif key in set10 and j in set10:
                  graph.add_edge(key, keys[j], color = "saddlebrown", penwidth = 2)
                elif key in set11 and j in set11:
                  graph.add_edge(key, keys[j], color = "black", penwidth =2)
                elif key in set12 and j in set12:
                  graph.add_edge(key, keys[j], color = "maroon4", penwidth =2)
                elif key in set13 and j in set13:
                  graph.add_edge(key, keys[j], color = "darkgreen", penwidth = 2)
                elif key in set14 and j in set14:
                  graph.add_edge(key, keys[j], color = "firebrick4", penwidth =2)
                elif key in set15 and j in set15:
                  graph.add_edge(key, keys[j], color = "indigo", penwidth = 2)
                else:
                  graph.add_edge(key, keys[j], color = "lightgray")
                """


    graph.draw("Paley%dcliquesPosterVersion.png" % length, prog = "neato")

def Wq_draw(filename):
    graph = gv.AGraph()
    try:
        infile = open(filename, "r")
    except:
        sys.exit()
    dic = {}
    i=0
    for line in infile:
        app = []
        list_ = line.strip().split()
        length = len(list_)
        for x in list_ :
            app.append(int(x))
        dic[range(length)[i]]= app
        i+=1
    keys = list(range(length))

    #make a dictionary of dictionaries
    #get positions: 
    lis = []
    radius = 20
    half_rad = 10
    r3 = 5
    for theta in range(length):
      if theta%3 == 0 :
        r = radius
      elif theta%3 ==1:
        r = half_rad
      else:
        r = r3
      x = cos((2*pi/float(length))*float(theta))*r
      y = sin((2*pi/float(length))*float(theta))*r
      lis.append([x,y])


    i =0
    for key in dic:
        graph.add_node(key, pos = "%f,%f!" %(lis[i][0], lis[i][1]), fillcolor ="cyan3",style= "filled", label = "")
        i+=1
        for j in range(len(dic[key])):
            if dic[key][j] == 1:
                graph.add_edge(key, keys[j])


    graph.draw("W%d.png" % length, prog = "neato")
  

if __name__ == "__main__":

    #paley_draw("o5.txt")
    paley_draw("o9.txt")
    #paley_draw("o13.txt")
    #paley_draw("new.txt")
    #paley_draw("o17.txt")
    #paley_draw("o25.txt")
    #paley_draw("o29.txt")
    #paley_draw("o81.txt")
    #Wq_draw("w5.txt")
    #Wq_draw("w2.txt")
    #Wq_draw("w3.txt")
