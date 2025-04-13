Instructions for reproducing the scatter plot of Figure 5.

This figure was produced using MATLAB version R2024b and PAST version 4.17.

In MATLAB:
- Set working directory to folder supplied for reproducing this figure (i.e. folder named figure_5).
- Run format_data script.
- Copy the output of the variable 'RAWpast' into PAST. 


In PAST:
- Paste the output from the variable'RAWpast' into an empty PAST worksheet
- Select all data with ctr+a
- Click Geometry > Outlines (2D) > Elliptic Fourier > EFA PCA
- In the window that opens, keep Modes set to 20, tick 'invariant to rotation+start, and click Compute
- In the scores tab, copy the output (EFA PCs)


In MATLAB:
- Save the first two PCs from the PAST EFA PCA as separate variables called 'pc1' and pc2'
- Run plot_scatter script


References:
Qianqian Fang (2024). JSONLab: portable, robust JSON/binary-JSON encoder/decoder (https://www.mathworks.com/matlabcentral/fileexchange/33381-jsonlab-portable-robust-json-binary-json-encoder-decoder), MATLAB Central File Exchange.

