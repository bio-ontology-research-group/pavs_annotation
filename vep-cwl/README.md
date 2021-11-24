# Running VEP with custom annotations including PAVS annotation using CWL:

In order run VEP through cwl, you will need a cwl-runner. One way to install cwl-runner is using pip package manager:

First, create an virtual environment and activate it:

```
virtualenv venv
source venv/bin/activate
```

Secondly, install cwl-runner:
```
pip install cwl-runner
```
Finally you can run the VEP workflow in cwl using following command:

```
cwl-runner vep.cwl vep-job.yml
```
The first parameter in the command for cwl file which describes the workflow and the second contains the values for input parameters to workflow. You can change the input vcf file by changing the value of **input_file** in vep-job.yml file. Similarly, you can change paramerters like assembly and location of custom annotation files.
