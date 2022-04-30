# snakemake workflow for genotype-based demultiplexing of scRNA-seq

This snakemake workflow allows genotype-based demultiplexing of scRNA-seq samples using vireoSNP and bam files of scRNA-seq samples comprising
transcriptome information of several donors. The workflow can be applied when genotype information are missing for all donors and a mulitplexing
strategy, e.g. AB-based, was included during sample processing in the lab allowing the back mapping of genotype-identity to the donors' meta data
via the labelling approach. Therefore, the main purpose of this pipeline is to validate cell origin identified by the labelling approach or to
improve the demultiplexing in cases where the labelling approach did not work optimally, e.g. when for a fraction of cells the labelling was too
weak to infere donor identity accurately.

## Workflow description
In short, the pipeline sorts and indexes the bam files. The genotype of each cell is called using cellsnp light and the most likely donor origin
is identified utilizing the tool vireoSNP.

## required input
- bam files and matching file, listing all barcodes
- reference vcf file comprising known genomic variants
- samples.txt, listing sample name, path to bam and barcode files, number of multiplexed donors in the sample

## Running the pipeline
1. Start a docker container in interactive mode using [jsschrepping/bioinfo-base-image:jss_v0.0.3](https://hub.docker.com/r/jsschrepping/bioinfo-base-image). 
   Make sure to mount all necessary files so that you get the following folder structure. Input files are exemplary, they can have different naming
   schems or can be placed in subfolder - just put the right path in the samples.txt:

`/	data<br/>
	├── config<br/>
	│   ├── config.yaml<br/>
	│   └── samples.txt<br/>
	├── input<br/>
	│   ├── S1.bam<br/>
	│   ├── S1_barcodes.csv<br/>
	│   ├── S2.bam<br/>
	│   └── S2_barcodes.csv<br/>
	├── resources<br/>
	│   └── {genomicSNP_collection}.vcf.gz<br/>
	└── workflow<br/>
		├── Snakefile<br/>
		├── report<br/>
		│   └── workflow.rst<br/>
		└── scripts<br/>
			└── vireo_plots.py<br/>`

2. Run snakemake workflow, e.g.: `/snakemake -rp --cores 16`

3. Generate report with some summary plots: `/snakemake --report report.html`
