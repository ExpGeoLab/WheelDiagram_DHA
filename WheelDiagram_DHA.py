import matplotlib.pyplot as plt
import numpy as np  # Import numpy for mathematical functions
from matplotlib.patches import Patch

# Define the categories and their possible states
categories = ["Reservoir", "Seal", "Charge", "Trap"]
states = ["Present", "Ambiguous", "Not Present", "Unevaluated"]

# Define the colors for each category
colors = {
    "Reservoir": "#FAFFB0",
    "Seal": "#EBAC99",
    "Charge": "#FF5C5C",
    "Trap": "#A3FF99"
}

# Function to determine the color and fraction of the pie slice based on the state
def get_color_and_fraction(state, color):
    if state == "Present":
        return color, 1.0
    elif state == "Ambiguous":
        return [color, 'white'], [0.5, 0.5]
    elif state == "Not Present":
        return 'white', 1.0
    elif state == "Unevaluated":
        return 'gray', 1.0

# Hypothetical example inputs
wellName = "RP-54st" # Well Name
play = "Devonian" # Play
category_states = { # The state of the Properties. You can change the names but do not forget to change in the chart as well
    "Reservoir": "Present", 
    "Seal": "Present",
    "Charge": "Present",
    "Trap": "Present"
}

# Prepare data for pie chart
labels = []
wedge_colors = []
wedge_fractions = []
diameter = 2  # Adjust this value if needed to fit your chart

for category, state in category_states.items():
    color, fraction = get_color_and_fraction(state, colors[category])
    if isinstance(fraction, list):
        labels.extend([f"{category} - {state}"] * len(fraction))
        wedge_colors.extend(color)
        wedge_fractions.extend(fraction)
    else:
        labels.append(f"{category} - {state}")
        wedge_colors.append(color)
        wedge_fractions.append(fraction)

# Create the pie chart
fig, ax = plt.subplots()
wedges, texts = ax.pie(wedge_fractions, colors=wedge_colors, startangle=90, 
                       wedgeprops={"edgecolor": "black", 'linewidth': 0.5, 'antialiased': True}, radius=diameter/2)

# Add the labels to show the states of the properties
ax.pie(x=[0.25, 0.25, 0.25, 0.25], startangle=90, labels=category_states.keys(), # If you need to display the state of the property labels=category_states.values()
       wedgeprops={"alpha": 0}, radius=diameter/4)

# Set aspect ratio to be equal so that pie is drawn as a circle.
ax.axis('equal')

# Create custom legend handles for the properties (categories)
legend_handles = [Patch(facecolor=colors[category], edgecolor='black', label=category) for category in categories]

# Add the legend to the plot (lower center)
#plt.legend(handles=legend_handles, title="Properties", loc='lower center', bbox_to_anchor=(0.5, -0.1), ncol=len(categories))

# Add title
plt.title(f"Well: {wellName}, Play: {play}", fontweight='bold')
#plt.title(f"Discovery!!", fontweight='bold')

# Display the plot
plt.show()