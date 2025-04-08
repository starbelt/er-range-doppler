import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.lines import Line2D

def plot_processing_times(root_dir):
    # Create Time_Analysis directory
    analysis_dir = os.path.join(root_dir, "Time_Analysis")
    os.makedirs(analysis_dir, exist_ok=True)
    
    # Find all processed_data.csv files
    csv_files = glob.glob(os.path.join(root_dir, "**", "processed_data.csv"), recursive=True)
    
    if not csv_files:
        print(f"No processed_data.csv files found in {root_dir}")
        return
        
    # Create figure with two y-axes
    fig, ax1 = plt.subplots(figsize=(14, 8))
    ax2 = ax1.twinx()
    
    # Define colors for different series
    colors = plt.cm.tab10.colors
    
    # Keep track of legend entries
    legend_handles = []
    legend_labels = []
    
    # Store dataframes for individual plots
    all_dataframes = {}
    
    # Process each file
    for i, file_path in enumerate(csv_files):
        try:
            # Extract the parent folder name for the legend
            parent_folder = os.path.basename(os.path.dirname(file_path))
            
            # Read the CSV file
            df = pd.read_csv(file_path)
            
            # Store dataframe for individual plots
            all_dataframes[parent_folder] = df
            
            # Use color consistently for both plots from the same file
            color = colors[i % len(colors)]
            
            # Plot processing time as points on the left y-axis
            proc_plot = ax1.scatter(df['Frame'], df['Processing Time (s)'], 
                         color=color, marker='o', alpha=0.6, s=20)
            
            # Plot total time as a line on the right y-axis
            total_plot = ax2.plot(df['Frame'], df['Total Time (s)'], 
                         color=color, linestyle='-', linewidth=1.5)[0]
            
            # Add to legend
            legend_handles.append((proc_plot, total_plot))
            legend_labels.append(parent_folder)
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # Configure axes for combined plot
    ax1.set_xlabel('Frame Number', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Processing Time (s)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Total Time (s)', fontsize=12, fontweight='bold')
    
    # Add grid
    ax1.grid(True, which='major', linestyle='-', linewidth=0.5, alpha=0.7)
    ax1.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.4)
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    
    # Create a custom legend
    custom_legend = []
    
    for i, (label, (scatter, line)) in enumerate(zip(legend_labels, legend_handles)):
        color = colors[i % len(colors)]
        custom_legend.append(Line2D([0], [0], color=color, label=f"{label}",
                           marker='o', markersize=6, linestyle='-'))
    
    # Add explanation for dots and lines
    custom_legend.append(Line2D([0], [0], marker='o', color='black', label="Processing Time (s)",
                               markerfacecolor='black', markersize=6, linestyle='None'))
    custom_legend.append(Line2D([0], [0], color='black', label="Total Time (s)", linestyle='-'))
    
    # Add the legend
    plt.legend(handles=custom_legend, loc='center left', bbox_to_anchor=(1.05, 0.5), 
              title="Data Series")
    
    # Add title
    base_name = os.path.basename(os.path.normpath(root_dir))
    plt.title(f'Processing and Total Time Analysis - {base_name}', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    
    # Save figure to the Time_Analysis directory
    output_path = os.path.join(analysis_dir, 'processing_time_analysis.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Combined plot saved to: {output_path}")
    
    # Create individual plots for each series
    for i, (technique_name, df) in enumerate(all_dataframes.items()):
        # Create a new figure for each technique
        fig_ind, ax_ind = plt.subplots(figsize=(10, 6))
        ax_ind2 = ax_ind.twinx()
        
        color = colors[i % len(colors)]
        
        # Plot processing time as points on the left y-axis
        ax_ind.scatter(df['Frame'], df['Processing Time (s)'], 
                   color=color, marker='o', alpha=0.6, s=20)
        
        # Plot total time as a line on the right y-axis
        ax_ind2.plot(df['Frame'], df['Total Time (s)'], 
                 color=color, linestyle='-', linewidth=1.5)
        
        # Configure individual plot
        ax_ind.set_xlabel('Frame Number', fontsize=12, fontweight='bold')
        ax_ind.set_ylabel('Processing Time (s)', fontsize=12, fontweight='bold')
        ax_ind2.set_ylabel('Total Time (s)', fontsize=12, fontweight='bold')
        
        # Add grid
        ax_ind.grid(True, which='major', linestyle='-', linewidth=0.5, alpha=0.7)
        ax_ind.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.4)
        ax_ind.xaxis.set_minor_locator(AutoMinorLocator())
        ax_ind.yaxis.set_minor_locator(AutoMinorLocator())
        
        # Add legend for individual plot
        ind_legend = [
            Line2D([0], [0], marker='o', color=color, label="Processing Time (s)",
                   markerfacecolor=color, markersize=6, linestyle='None'),
            Line2D([0], [0], color=color, label="Total Time (s)", linestyle='-')
        ]
        
        ax_ind.legend(handles=ind_legend, loc='upper left')
        
        # Add title
        plt.title(f'{technique_name} - Processing and Total Time', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        
        # Create a safe filename from the technique name
        safe_name = technique_name.replace(' ', '_')
        
        # Save individual figure
        ind_output_path = os.path.join(analysis_dir, f'{safe_name}_time_analysis.png')
        plt.savefig(ind_output_path, bbox_inches='tight', dpi=300)
        print(f"Individual plot saved to: {ind_output_path}")
        
        # Close the individual plot to free memory
        plt.close(fig_ind)
    
    plt.show()

# Run the script with command line argument or user input
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = input("Enter the directory path to search: ")
    
    plot_processing_times(base_dir)