## data_dict={
## "enst100110" : {"gene_strand":"+",
##                 "region":"exon",
##                 "length":"87",
##                 "repair_raw":"89",
##                 "repair_rpkm":"2.42",
##                 "strain":"wT",
##                 "replicate":"A",
##                 "damage":"CPD",
##                 "repair_strand":"+",
##                 "transcribed":"TS"}
##                  
##........
##          }

data_name = input("Please enter the sample name: ")
out_name = input("Please enter the output file name: ")

data = open(data_name, "r")
f = open(out_name, 'a')

data_line = data.readlines()


for x in data_line:
    a = x.split()
    data_list=[]
    for i in a:
        data_list.append(i)
        
    
    if data_list[6] == "WT":
       f.write(("%s" % x))
        
    
f.close()
