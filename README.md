# snakemake workflow for genotype-based demultiplexing of scRNA-seq

This snakemake workflow allows genotype-based demultiplexing of scRNA-seq samples using the tool vireoSNP and bam files of scRNA-seq samples comprising
transcriptome information of several donors. The workflow can be applied when genotype information are missing for all donors and a multiplexing
strategy, e.g. AB-based, was included during sample processing in the lab allowing the back mapping of genotype-identity to the donors' meta data
via the labelling approach. Therefore, the main purpose of this pipeline is to validate cell origin identified by the labelling approach or to
improve the demultiplexing in cases where the labelling approach did not work optimally, e.g. when for a fraction of cells the labelling was too
weak to infer donor identity accurately.

## Workflow description
In short, the pipeline sorts and indexes the input bam files. The genotype of each cell is called using cellsnp light and the most likely donor origin
is identified utilizing the tool vireoSNP.

## Input
- bam files and matching file, listing all barcodes
- reference vcf file comprising known genomic variants
- samples.txt, listing sample name, path to bam and barcode files, number of multiplexed donors in the sample

## Running the pipeline
1. Start a docker container in interactive mode using [jsschrepping/bioinfo-base-image:jss_v0.0.3](https://hub.docker.com/r/jsschrepping/bioinfo-base-image). 
   Make sure to mount all necessary files so that you get the following folder structure. Input files are exemplary, they can have different naming
   schemes or can be located in subfolder (the paths need to be in the samples.txt):
   
 	data  
	│ ── config  
	│&nbsp; &nbsp; &nbsp; &nbsp; ├── config.yaml  
	│&nbsp; &nbsp; &nbsp; &nbsp; └── samples.txt  
	│── input  
	│&nbsp; &nbsp; &nbsp; &nbsp; ├── S1.bam  
	│&nbsp; &nbsp; &nbsp; &nbsp; ├── S1_barcodes.csv  
	│&nbsp; &nbsp; &nbsp; &nbsp; ├── S2.bam  
	│&nbsp; &nbsp; &nbsp; &nbsp; └── S2_barcodes.csv  
	│── resources  
	│&nbsp; &nbsp; &nbsp; &nbsp; └── {genomicSNP_collection}.vcf.gz  
	└── workflow  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;│── Snakefile  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;│── report  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;│&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;└── workflow.rst  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;└── scripts  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; └──vireo_plots.py  
			

2. Run snakemake workflow, e.g.: `snakemake -rp --cores 16`

3. Generate report with some summary plots: `snakemake --report report.html`
