# Compuler
Compile your Python Projects Into Exe Application for Windows

CounTrol - Python to EXE Converter
CounTrol is a Python-to-EXE converter with a simple, intuitive graphical interface. It allows you to easily convert Python scripts to standalone executables using PyInstaller. With features like drag-and-drop support, customizable PyInstaller options, and multi-file packaging, CounTrol is a powerful tool for developers looking to distribute their Python applications as executables.

Features
1. Progress Bar for Conversion
A progress bar provides visual feedback during the conversion process. It starts when the conversion begins and stops when the process is complete, giving users a clear indication of the progress.

2. Output Log Window
CounTrol includes a log window that displays detailed logs of the PyInstaller conversion process. This is particularly useful for debugging and troubleshooting in case any errors occur during the conversion.

3. Drag-and-Drop Support
With drag-and-drop functionality, users can easily select Python scripts (.py) and icon files (.ico) by simply dragging them into the app. This makes file selection quick and intuitive.

4. Customizable PyInstaller Options
Users have the flexibility to customize PyInstaller’s behavior by specifying:

UPX Compression: Reduce the size of the generated executable using UPX compression.
Hidden Imports: Add hidden imports if needed for your script.
Additional Files: Bundle extra files or directories with your executable using the --add-data option.
5. Virtual Environment Detection
The tool checks if the user is working in a virtual environment and displays a warning if they are not. This helps users ensure that the correct environment is being used during the conversion process.

6. Versioning and "About" Section
CounTrol provides version information both for the tool itself and the PyInstaller version being used. This information is available through an "About" menu, making it easy to track versions.

7. Error Handling and Validation
Input validation ensures that users select valid Python scripts and icon files. If an invalid file is selected, CounTrol displays an error message to prevent incorrect conversions.

8. Multi-file or Directory Packaging
Users can include additional files or directories in their executable package by specifying them in the interface. This feature is powered by PyInstaller’s --add-data option.

9. Command-line Interface (CLI) Support
While CounTrol is designed primarily as a graphical tool, it also supports running conversions directly from the command line using argparse. This allows for quick, non-GUI batch conversions.

How to Use
Requirements
Make sure you have the following Python packages installed:

tkinterdnd2: for drag-and-drop functionality.
Pillow: for handling icons and image files.
PyInstaller: for converting Python scripts into executables.
Install these dependencies using pip:

pip install tkinterdnd2 Pillow PyInstaller
Running the Tool
Download or clone the repository.

Run the Python script:

python counTrol.py
Select your Python script (.py) and (optionally) an icon (.ico).

Customize PyInstaller options such as UPX compression, hidden imports, or additional files.

Click "Convert to EXE" to generate the executable.

Command-line Mode
CounTrol also supports command-line usage. You can convert a Python script to an executable directly from the terminal using:

python counTrol.py --script your_script.py --icon your_icon.ico --app_name "YourAppName"
Screenshots
Main Interface

Output Log

Contributing
Feel free to fork the project and submit pull requests. Any contributions, improvements, or feedback are greatly appreciated!

License
This project is licensed under the MIT License.

