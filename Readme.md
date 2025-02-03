# GradeCalculator

### Description

**GradeCalculator** is a Python program designed to help students keep track of their grades throughout the school term. It allows users to input their grades for courses, calculate averages, and display an overall GPA at the bottom. 

I created this project during the 1st class, 1st semester of my Computer Engineering studies to improve my Python skills. Since then, I have also been using it to track my grades.


---

### Features

- Input and track grades for multiple courses.
- Calculate subject-wise averages.
- Display an overall GPA at the bottom of the grade list.
- Promts in the program will guide the user.

---

### Requirements

- **Python 3.11+** (It may also work with earlier Python 3 versions, but this is untested.)

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Alismero/GradeCalculator.git
   ```
2. Navigate to the project folder:
   ```bash
   cd GradeCalculator/Program
   ```
3. Run the program:
   ```bash
   python3 GradeCalculator.py
   ```

---

### Little Warning !

I created a binary file called `Data.dat`, which contains an empty dictionary (`{}`). This file is necessary for the program to run properly. If you encounter a "File not found" error, please copy the path of the Data.dat file and paste it into the following sections:

- File opening part (At the begginning of the program)
```python
    with open("PATH_TO_FILE", "rb") as datafile:
```
- Save function part (At the end of the program)
```python
    with open("PATH_TO_FILE", "wb") as datafile:
```

If you do not encounter any errors, just let the program run as it is. :)

---

### Usage

Simply run the program, and it will guide you through the process of entering grades and viewing calculated averages. No additional configuration is needed.

---

### Feedback

If you have suggestions or find any issues, feel free to open an issue in this repository: [Open an Issue](https://github.com/Alismero/GradeCalculator/issues).

---

### License

This project does not currently have a license. If you wish to use or modify the code, you are free to do so.

---

### About the Developer

Developed by [Ali Kazancı](https://github.com/Alismero). Feel free to check out my GitHub profile for more projects (More will come soon...)!

---

### Notes
I used hard formatting in some parts of my code, and there might be more efficient ways to do it. You may give me feedback.

I use Ankara University's grade ranges for calculating GPA, as mentioned in `GradeWeights.png`. If your grade ranges are different, you can modify them in the GeneralAverageV2 function. (The reason there are two GeneralAverage functions is that I initially coded GeneralAverageV1 based on an arithmetic average system. However, after learning Ankara University's grading system, I updated it and created GeneralAverageV2.)

You can view a part of my development process in the `GC.excalidraw` file. You can open it at [excalidraw](https://excalidraw.com), or you can download the Excalidraw extension for VS Code to open it directly.

If you encounter any issues or have suggestions for improvement, please open an issue in the repository or contact me directly through GitHub.

