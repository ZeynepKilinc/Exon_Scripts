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

xr_name = input("Please enter the xr sample name: ")
dm_name = input("Please enter the damage name: ")
out_name = input("Please enter the output file name: ")

f = open(out_name, 'a')

data = open(xr_name, "r")

data_dict={ }

damage_dict = { }

data_line = data.readlines()


for x in data_line:
    x = x.split()
    data_list=[]
    for i in x:
        data_list.append(i)
        
    gene_name = data_list[0]
    gene_strand = data_list[1]
    region = data_list[2]
    length = data_list[3]
    rraw = data_list[4]
    rrpkm = data_list[5]
    strain = data_list[6]
    replicate = data_list[7]
    damage = data_list[8]
    repair = data_list[9]
    ts = data_list[10]
    draw = 0
    drpkm = 0
    ratio = 0
    gene_spec = gene_name + gene_strand + region + length + strain + replicate + damage + repair + ts
    
    dict_in={"gene_name":gene_name,"gene_strand":gene_strand,"region":region,"length":length,"repair_raw":rraw,"repair_rpkm":rrpkm,"strain":strain,"replicate":replicate,"damage":damage,"repair_strand":repair,"transcribed":ts,"damage_raw":draw,"damage_rpkm":drpkm,"ratio":ratio}
    data_dict[gene_spec] = dict_in


data2 = open(dm_name, "r")

data_line_2 = data2.readlines()

for x in data_line_2:
    x = x.split()
    data_list=[]
    for i in x:
        data_list.append(i)

        
    gene_name = data_list[0]
    gene_strand = data_list[1]
    region = data_list[2]
    length = data_list[3]
    ddraw = data_list[4]
    ddrpkm = data_list[5]
    strain = data_list[6]
    replicate = data_list[7]
    damage = data_list[8]
    repair = data_list[9]
    ts = data_list[10]
    gene_spec2 = gene_name + gene_strand + region +length+ "WT" + replicate +damage +  repair +ts
    if float(ddrpkm) != 0:
        data_dict[gene_spec2]["damage_raw"] = ddraw
        data_dict[gene_spec2]["damage_rpkm"] = ddrpkm
        data_dict[gene_spec2]["ratio"] = str(float(data_dict[gene_spec2]["repair_rpkm"])/float(ddrpkm))
          




for dict_gene, dict_gene_list in data_dict.items():
    a = []
    for key in dict_gene_list:
        a.append(dict_gene_list[key])
    for item in a:
       f.write(("%s" % item)+"\t")
    f.write("\n")


f.close()

