f = open("pelican.txt", "a")
f.write("A wonderful bird is the pelican,\n")
f.write("His bill holds more than his belican,\n")
pelican_lines = ["he can take in his beak, \n", "Enough food for a week, \n",
                 "But i'm damned if i see how the helican.\n",]
f.writelines(pelican_lines)
