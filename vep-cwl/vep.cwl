cwlVersion: v1.0
class: CommandLineTool
# baseCommand:
#   - /usr/bin/perl
#   - /opt/vep/src/ensembl-vep/INSTALL.pl
baseCommand:
  - /usr/bin/perl
  - /opt/vep/src/ensembl-vep/vep 
hints:
  DockerRequirement:
    dockerPull: 'matmu/vep:103-GRCh38'
inputs:
  input_file:
    type: File
    inputBinding:
      position: 1
      prefix: '-input_file'
  assembly:
    type: string
    inputBinding:
      position: 2
      prefix: '-assembly'
  pavs_custom_file:
    type: File
    secondaryFiles:
      - .tbi
  pavs_custom_args:
    type: string
  go_custom_file:
    type: File
    secondaryFiles:
      - .tbi
  go_custom_args:
    type: string
  hpo_custom_file:
    type: File
    secondaryFiles:
      - .tbi
  hpo_custom_args:
    type: string
  ppi_custom_file:
    type: File
    secondaryFiles:
      - .tbi
  ppi_custom_args:
    type: string

outputs:
  console_out: stdout
  anno_file_out: 
    type: File
    outputBinding:
      glob: output.vcf

arguments:
  - valueFrom: $(inputs.pavs_custom_file.path),$(inputs.pavs_custom_args)
    prefix: --custom
  - valueFrom: $(inputs.go_custom_file.path),$(inputs.go_custom_args)
    prefix: --custom
  - valueFrom: $(inputs.hpo_custom_file.path),$(inputs.hpo_custom_file)
    prefix: --custom
  - valueFrom: $(inputs.ppi_custom_file.path),$(inputs.ppi_custom_file)
    prefix: --custom
  - '--cache'
  - valueFrom: '/opt/vep/.vep/'
    prefix: --dir_cache
  - valueFrom: 'b'
    prefix: --polyphen
  - valueFrom: 'b'
    prefix: --sift
  - valueFrom: '500'
    prefix: --buffer_size
  - valueFrom: 'homo_sapiens'
    prefix: --species
  - '--symbol'
  - '--transcript_version'
  - '--tsl' 
  - '--numbers'  
  - '--check_existing' 
  - '--hgvs' 
  - '--biotype'
  - '--cache' 
  - '--tab' 
  - '--no_stats' 
  - '--af' 
  - '--af_gnomad' 
  - '--canonical'
  - valueFrom: output.vcf
    prefix: --output_file   
