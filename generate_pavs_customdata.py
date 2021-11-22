import sys
import json
import requests

target_url="http://pavs.phenomebrowser.net/sparql?query=PREFIX+%3A+%3Chttp%3A%2F%2Fpavs.phenomebrowser.net%2F%3E+++++++++%0D%0APREFIX+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E+++++++++%0D%0A+++++++++++%0D%0ASELECT+distinct+%3Fphenopacket+%3FhgvsAllele+%3Fallele+%3Fassembly+%3Fspdi_inserted_sequence+%3Fspdi_deleted_sequence+%28group_concat%28distinct+%3Fphenotype_label%3Bseparator%3D%22%7C%22%29+as+%3Fphenotype_labels%29++%28group_concat%28distinct+%3Fclass%3Bseparator%3D%22%7C%22%29+as+%3Fhpo_classes%29+%0D%0AFROM+%3Chttp%3A%2F%2Fpavs.phenomebrowser.net%3E%0D%0AWHERE+%7B%0D%0A+%3Fphenopacket+rdf%3Atype+%3APhenopacket+.%0D%0A+%3Fphenopacket+%3Abiosamples+%3Fsample+.%0D%0A+%3Fsample+%3Avariants+%3Fvariant+.%0D%0A+%3Fvariant+%3Ahgvs_allele+%3FhgvsAllele+.%0D%0A+%3Fvariant+%3Aallele+%3Fallele+.%0D%0A+%3Fvariant+%3Aassembly+%3Fassembly+.%0D%0A++OPTIONAL+%7B+%0D%0A+++++%3Fvariant+%3ASpdiAllele+%3Fspdi_allele+.+%0D%0A+++++OPTIONAL+%7B+%3Fspdi_allele+%3Ainserted_sequence+%3Fspdi_inserted_sequence+.+%7D%0D%0A+++++OPTIONAL+%7B+%3Fspdi_allele+%3Adeleted_sequence+%3Fspdi_deleted_sequence+.++%7D%0D%0A++%7D+%0D%0A%0D%0A++OPTIONAL+%7B+%0D%0A+++++%3Fphenopacket+%3Aphenotypic_features+%3Fpheno_features+.+%0D%0A+++++%3Fpheno_features+%3Atype+%3Fclass+.%0D%0A+++++OPTIONAL+%7B+%3Fclass+rdfs%3Alabel+%3Fphenotype_label+.++%7D%0D%0A++++OPTIONAL+%7B+%3Fpheno_features+dc%3Adescription+%3Fphenotype_label+.+%7D+%0D%0A++%7D+%0D%0A%7D+++++&format=text%2Ftab-separated-values&timeout=0&debug=on"

req = requests.get(target_url)
f = open("pavs_final.tsv", "w")
f.write(req.text)
f.close()

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
     
