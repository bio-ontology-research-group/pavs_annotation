module load tabix
module load bedtools
module load bcftools
python generate_pavs_customdata.py $1 >pavs.plugin.$1.vcf 

grep "^#" pavs.plugin.$1.vcf > sorted.pavs.plugin.$1.vcf
grep -v "^#" pavs.plugin.$1.vcf| sort -k1,1V -k2,2g >> sorted.pavs.plugin.$1.vcf
bgzip -c sorted.pavs.plugin.$1.vcf > sorted.pavs.plugin.$1.vcf.gz
tabix -p vcf sorted.pavs.plugin.$1.vcf.gz

