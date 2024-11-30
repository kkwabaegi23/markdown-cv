import os
import subprocess

# Set execution policy (not needed in Python)
# In PowerShell this is used to bypass script signing requirement, but in Python, it's usually not an issue.

# Get all markdown files in the current directory
markdown_files = [f for f in os.listdir('.') if f.endswith('.md') and f.startswith('cv')]

# Loop through each markdown file
for file in markdown_files:
    # Grab the filename
    filename = file

    # Output the filename (you can perform any operations you want here)
    print(f"Processing file: {filename}")

    # Extract the pure base name (without extension)
    filename_pure, _ = os.path.splitext(filename)
    filename_tex = f"{filename_pure}.tex"

    # Determine language based on the filename
    if filename.startswith('cv_en'):
        language = "english"
    else:
        language = "german"
    
    # Convert markdown to DOCX using pandoc
    subprocess.run(['pandoc', '-s', filename, '-o', f"./output/{filename_pure}.docx"], check=True)
    
    # Convert markdown to LaTeX using the md_to_tex.py script
    subprocess.run(['python', 'md_to_tex.py', filename, language], check=True)
    
    # Run pdflatex to generate the PDF
    subprocess.run(['pdflatex', '-output-directory', 'output', filename_tex], check=True)

# Cleanup: remove auxiliary files (.aux, .log, .out) in the output directory
for file in os.listdir('./output'):
    if file.endswith(('.aux', '.log', '.out')):
        file_path = os.path.join('./output', file)
        os.remove(file_path)
        print(f"Removed {file_path}")
