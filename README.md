# Hopper fork of tangent v0.3.1

First, perform the following steps: 

1. run `make` from the `tangent` directory. This will compile the C++ program called `mathindex`. 
2. Add the `tangent-v031` top-level directory to your `PYTHONPATH`. 

## Generating tuples from a list of MathML files
1. Create a directory containing only MathML files. Make sure they end with the extension `.mml`. The `.pmml` extension is not currently supported.
2. Create a file that contains the full paths of each of the MathML files. One path per line. In what follows, assume this file is called `$EQ-PATHS-FILE`.
3. In the config file named `hopper.cntl`, change the `doc_list` line to point to the `$EQ-PATHS-FILE` you created above. 
4. From the tangent directory, run `python3 index.py hopper.cntl` to create a database of symbol layout trees (SLTs). These trees will be written to `tangent/db-index/`. 
5. Write the tuples for all of the SLTs to a file `$ALL-TUPLES`. From the `tangent` directory, run: `cat db-index/* | ./mathindex.exe -v 2> $ALL-TUPLES`
6. **(DLMF-only)** Organize the tuples into the original directory structure, with 1 directory per chapter, and 1 file per equation. Assume you want all chapters directories in `$DLMF-TUPLE-DIR` From the top-evel tangent-v031 directory: `python hop-postProcess.py --eq_paths $EQ-PATHS-FILE --all_tuples $ALL-TUPLES --outdir t$DLMF-TUPLE-DIR`
