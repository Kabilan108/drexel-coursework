function plot_intfire(V_trace)
    % Plot data
    plot(V_trace)
    
    % Show major and minor grids in gray with alpha 0.4 and 0.3
    grid on;
    set(gca, 'GridAlpha', 0.4, 'MinorGridAlpha', 0.3, 'GridColor', [0.5 0.5 0.5]);
    grid minor;
    
    % Set axis labels
    xlabel('Time (ms)');
    ylabel('Voltage (mV)');

    % Y limits
    ylim([min(V_trace(1, :)) max(V_trace(1, :))*1.10]); 
end
