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
  custom_file:
    type: File
    secondaryFiles:
      - .tbi
  custom_args:
    type: string
arguments:
  - valueFrom: $(inputs.custom_file.path),$(inputs.custom_args)
    prefix: --custom
  - '--cache'
  - valueFrom: '/opt/vep/.vep/'
    prefix: --dir_cache
  - '--symbol --transcript_version --tsl --numbers  --check_existing --hgvs --biotype --cache --tab --no_stats --af --af_gnomad --canonical'
outputs:
  out1: stdout
   
