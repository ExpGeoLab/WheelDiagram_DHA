# Single Wheel Diagram Generator

This Python script generates a **Single Wheel Diagram** to visualize the state of play elements (Reservoir, Seal, Charge, Trap) for a specific well and play. It is a **limited version** of the [Well Penetration Chart Generator](https://github.com/ExpGeoLab/WellPenetrationChart), which creates multi-well visualizations and offers advanced features like exporting pie charts and updating input files.

![wagonWheelS](https://github.com/user-attachments/assets/7137a33d-6dfb-4a26-bc5e-b644d2bbbfdc)

---

## 📋 Table of Contents
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Input Data](#-input-data)
- [Output](#-output)
- [Well Penetration Chart Generator](#-well-penetration-chart-generator)
- [License](#-license)

---

## ✨ Features
- **Single Wheel Diagram**: Visualizes the state of play elements (Present, Ambiguous, Not Present, Unevaluated) using a pie chart.
- **Customizable Input**: Allows customization of well name, play name, and play element states.
- **Dynamic Colors**: Uses predefined colors for each play element.
- **Interactive Visualization**: Displays the diagram with a title and optional legend.

---

## 📦 Requirements
- Python 3.x
- Libraries:
  - `matplotlib`
  - `numpy`

Install the required libraries using:
```bash
pip install matplotlib numpy
```

---

## 🛠 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/single-wheel-diagram.git
   cd single-wheel-diagram
   ```
2. Install the required libraries (see [Requirements](#-requirements)).

---

## 🚀 Usage
Run the script with the following command:
```bash
python single_wheel_diagram.py
```

### Customization
- Modify the `wellName`, `play`, and `category_states` variables in the script to match your data.
- Adjust the `diameter` variable to change the size of the wheel diagram.

---

### 📂 Input Data
The script uses the following predefined inputs:
- **Well Name**: Name of the well (e.g., `RP-54st`).
- **Play**: Name of the play (e.g., `Devonian`).
- **Category States**: A dictionary defining the state of each play element. The possible states are:
  - `"Present"`: The play element is confirmed to be present.
  - `"Ambiguous"`: The play element is partially present or uncertain.
  - `"Not Present"`: The play element is confirmed to be absent.
  - `"Unevaluated"`: The play element has not been evaluated.

Example:
```python
category_states = {
    "Reservoir": "Present", 
    "Seal": "Ambiguous",
    "Charge": "Not Present",
    "Trap": "Unevaluated"
}
``` 


---

## 📤 Output
- **Single Wheel Diagram**: A pie chart visualizing the state of play elements for the specified well and play.
- **Title**: Displays the well name and play name.

---

## 🖼 Example
### Input
```python
wellName = "RP-54st"
play = "Devonian"
category_states = {
    "Reservoir": "Present", 
    "Seal": "Present",
    "Charge": "Present",
    "Trap": "Present"
}
```

### Output
- A pie chart showing the state of each play element (Reservoir, Seal, Charge, Trap) for the well `RP-54st` in the `Devonian` play.

---

## 🔗 Well Penetration Chart Generator
The **Well Penetration Chart Generator** is a more advanced tool that extends the functionality of this script. It allows you to:
- Generate **multi-well visualizations** with pie charts for multiple wells and plays.
- **Export pie charts** as PNG files for integration into QGIS or reports.
- **Update input files** with the paths of exported pie charts.
- Customize chart sizes, colors, and grid properties.
- Export updated data in **Excel** or **CSV** format.

For more details, visit the [Well Penetration Chart Generator repository](https://github.com/ExpGeoLab/WellPenetrationChart).

---

## 📄 License
This project is licensed under the Creative Commons License. See the [LICENSE](LICENSE.txt) file for details.

---

For questions or feedback, please open an issue or contact the author. 🚀
