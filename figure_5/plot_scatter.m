%%Script for plotting Figure 5
%input: first two PCs of EFA imported from PAST (define them as variables: 'pc1' and 'pc2')
%output: scatter plot of EFA PC1 v PC2 of corded ware and bell beaker grave outlines

%extract period information per grave outline
    for i = 1:length(dat)
        period{i} = [dat(1,i).culture_label];
    end
    Period = ordinal(period);
    Period = reorderlevels(Period,{'CW','BB'});

%plot scatter of EFA PC1 v PC2 grouped by period
    figure(); hold on; axis equal
    set(gca, 'XAxisLocation', 'origin', 'YAxisLocation', 'origin')
    scatter(pc1(Period=='CW'),pc2(Period=='CW'),35,[43,131,186]/255,'filled','s','MarkerEdgeColor',[43,131,186]/255)
    scatter(pc1(Period=='BB'),pc2(Period=='BB'),25,[215,25,28]/255,'filled','^','MarkerEdgeColor',[215,25,28]/255)
    legend('Corded Ware','Bell Beaker')