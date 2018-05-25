Using R, I needed to convert some [long format data to wide format](https://en.wikipedia.org/wiki/Wide_and_narrow_data) in the form of a presence/absence dataset. The *why* doesn't really matter :)

Where the initial dataset is for example a vector of categories, the intended output will have as many columns as the unique values of the original. For example, where the original dataset looks like this:

```
"TILLD-DMTN"
"GFDUD-XSV"
"TILLD-DMTN"
```

We want to turn it into a matrix like this:

```
      "TILLD-DMTN"      "GFDUD-XSV"      "TILLD-DMTN"
1          1                               0                            0
2          0                               1                            0
3          0                               0                            1
```

This is achieved using the package `reshape2` and the function `dcast`.

First we'll create two example input datasets - one numeric and one character:

```R
landclass=factor(c(1,2,3,3,3,4,5,6,7,8,8,8,9))
rocks=c("TILLD-DMTN", "GFDUD-XSV", 
    "TILLD-DMTN",
    "TILLD-DMTN",
    "NONE_RECORDED ",
    "TILLD-DMTN",
    "TILLD-DMTN",
    "TILLD-DMTN",
    "NONE_RECORDED ",
    "TILLD-DMTN",
    "TILLD-DMTN",
    "TILLD-DMTN",
    "PEAT-P",
    "NONE_RECORDED",
    "TILLD-DMTN",
    "TILLD-DMTN",
    "TILLD-DMTN",
    "GFDUD-XSV",
    "PEAT-P",
    "ALV-XCZSV")
```

If we look at rocks for example, we have:

```R
> head(rocks)
[1] "TILLD-DMTN"     "GFDUD-XSV"      "TILLD-DMTN"     "TILLD-DMTN"    
[5] "NONE_RECORDED " "TILLD-DMTN" 
```

Now we import `reshape2` and construc a function using dcast to do the work:

```R
library(reshape2)

presence_absence <-function(data){
    tnt <- as.data.frame(data)
    # Create an ID column to hold the row index
    tnt$ID <- seq.int(nrow(tnt))
    out=dcast(tnt, ID ~data, length)
    
    # Get rid of the ID column from the matrix
    drops=c("ID")
    out=out[ , !(names(out) %in% drops)]

    return(out)
}
```

This will now work for inputs of varying type (character/numeric etc.):

```R
rocks_mat=presence_absence(rocks)
landclass_mat=presence_absence(landclass)
```

If we look at `rocks_mat`, we now have:

```R
> head(rocks_mat)

ALV-XCZSV GFDUD-XSV NONE_RECORDED NONE_RECORDED  PEAT-P TILLD-DMTN
1         0         0             0              0      0          1
2         0         1             0              0      0          0
3         0         0             0              0      0          1
4         0         0             0              0      0          1
5         0         0             0              1      0          0
6         0         0             0              0      0          1
```

Thanks to [Franziska Schrodt](http://fischrodt.wixsite.com/fisw) for helping with this!


