---
layout: post
title: Comparing input and output files
categories: Python
tags: FFT signal
---

When running jobs on multiple files, sometimes you might find that files are missed. To ensure that you process ALL files, you can compare your total input files with those already processed using `grep`. Here's an example of implementing this in R. You could couple this with a while loop for a script, making sure the script repeats until input files meet output files... This example assumes that your output files retain the original input file with the addition of an extension (\_output.csv) which we first have to remove.

```R
# Create a list of unprocessed files by comparing input and exisitng output files

# list of files e.g. Sys.glob(paste0(path, "*.csv")
fs_original_test=c(
"./outHP/coast_0_profile_000000_hp.csv",
"./outHP/coast_0_profile_000001_hp.csv",
"./outHP/coast_0_profile_000002_hp.csv",
"./outHP/coast_0_profile_000003_hp.csv",
"./outHP/coast_0_profile_000004_hp.csv",
"./outHP/coast_0_profile_000005_hp.csv",
"./outHP/coast_0_profile_000006_hp.csv",
"./outHP/coast_0_profile_000007_hp.csv",
"./outHP/coast_0_profile_000008_hp.csv",
"./outHP/coast_0_profile_000009_hp.csv")

# list of files e.g. Sys.glob(paste0(opath, "*.csv") with an extension 
fs_processed_test=c(
"coast_0_profile_000000_hp_output.csv",
"coast_0_profile_000000_hu_output.csv",
"coast_0_profile_000000_na_output.csv",
"coast_0_profile_000000_nb_output.csv",
"coast_0_profile_000000_nc_output.csv",
"coast_0_profile_000000_nd_output.csv",
"coast_0_profile_000000_nf_output.csv",
"coast_0_profile_000000_nf_output.csv",
"coast_0_profile_000000_ng_output.csv",
"coast_0_profile_000000_nm_output.csv")

# Remove extension of output files so they match the original file pattern
fs_processed_test=paste0(strsplit(fs_processed_test, "_output.csv"), ".csv")


	fs_original_basename=basename(fs_original_test)
	missing_files=setdiff(fs_original_basename, fs_processed_test)
	files_to_process=Sys.glob(paste0("./outHP/",missing_files)


<<<<<<<<<<<<<<<

# Create vector of things to match (e.g. processe file names - extensions have been removed)
toMatch_test=fs_processed_test

# Returns matching string value (in this case, the file name)
# taken from: https://stackoverflow.com/questions/7597559/grep-using-a-character-vector-with-multiple-patterns
matches_test <- unique (grep(paste(toMatch_test,collapse="|"), 
                        fs_original_test, value=TRUE))

# Returns numerical index position of matching string in vector
# matches <- unique (grep(paste(toMatch,collapse="|"), 
#                        fs_original, value=FALSE))

# subset original_fs to exclude any matches
to_process_test=fs_original_test[fs_original_test!=matches_test]

print(paste0(length(to_process), " files still to process..."))
```

