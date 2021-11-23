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
# inputs:
#   cfp:
#     type: string?
#     inputBinding:
#       position: 1
#       prefix: '-a'
#   species:
#     type: string?
#     default: 'homo_sapiens'
#     inputBinding:
#       position: 2
#       prefix: '-s'
#   assembly:
#     type: string?
#     default: 'GRCh38'
#     inputBinding:
#       position: 3
#       prefix: '-y'
#   PLUGINS:
#     type: string?
#     inputBinding:
#       position: 4
#       prefix: '-g'

outputs:
  out1: stdout
   
