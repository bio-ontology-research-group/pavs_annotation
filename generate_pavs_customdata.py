import sys
import json

ref="GRCh"+sys.argv[1]


proc_str=[]

#phenopacket	hgvsAllele	allele	assembly	spdi_inserted_sequence	spdi_deleted_sequence	phenotype_labels	hpo_classes
#http://pavs.phenomebrowser.net/Phenopacket/pavs20	NC_000005.9:g.45262146del	chr5:g.45262146del	GRCh37	GGGGG	GGGGGG	Bimanual synkinesia|Enuresis	http://purl.obolibrary.org/obo/HP_0000805|http://purl.obolibrary.org/obo/HP_0001335

print ("#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO")
filef="pavs_final.tsv"
with open(filef, 'r') as f:
 for line in f:
   line_list=line.split("\t")
   if ref in line_list[3]:
      proc_str=line_list[2].replace('"','').split(":g.")
      reference=line_list[5].replace('"','')
      alt=line_list[4].replace('"','')
      start_ind=proc_str[1]
      if '>' in start_ind:
        #NC_000010.11:g.121520052T>G
        r=start_ind[-3:].split(">")
        reference=r[0]
        alt=r[1]
        start_ind=start_ind[:-3]
        end_ind=start_ind
      elif '=' in start_ind:
        start_ind=start_ind[:-1]
        end_ind=start_ind
      elif '_' in start_ind:
        tmps=start_ind.split("_")
        start_ind=tmps[0]
        if "d" in tmps[1]:
          tmpe=tmps[1].split("d")
          end_ind=tmpe[0]
        elif "i" in tmps[1]:
          tmpe=tmps[1].split("i")
          end_ind=tmpe[0]
      elif "del" in start_ind:
        start_ind=start_ind[:-3]
        end_ind=start_ind
      elif "dup" in start_ind:
        start_ind=start_ind[:-3]
        end_ind=str(int(start_ind)+1)
      #else:
      #  print (str(line_list[2]))      
      hpos=line_list[7].rstrip()
      hpos=hpos.replace("http://purl.obolibrary.org/obo/", "").replace('"','')
      hpos=hpos.replace("|","##")
      chrom=proc_str[0].replace("chr","")
      if len(hpos)>1:
          print (chrom+"\t"+start_ind+"\t"+hpos+"\t"+reference+"\t"+alt+"\t50\tPASS\t"+hpos)
     
