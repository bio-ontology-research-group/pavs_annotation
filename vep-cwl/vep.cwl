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
    inputBinding:
      position: 2
      prefix: '--custom'
  custom_args:
    type: string
    inputBinding:
      position: 3
      prefix: ','

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
   