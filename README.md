# Task Eight - Working with VSCodium, HTML, and Python Scripts

## Overview

In this task, we installed VSCodium on Kali Linux to edit HTML and Python files from Task Three. The goal is to improve the HTML file using Emmet in VSCodium, add a shebang (`#!/usr/bin/env python3`) to the Python script, and execute the Python script without using the `python` command.


## Steps

### 1. Install VSCodium on Kali Linux

VSCodium is a free, open-source version of Microsoft's Visual Studio Code. It can be installed on Kali Linux as follows:

#### Installation Steps:
##### 1. Add the VSCodium GPG Key and Repository:
     ```wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg \
    | gpg --dearmor \
    | sudo dd of=/usr/share/keyrings/vscodium-archive-keyring.gpg```
##### 2. Add the repository:
    ```echo 'deb [ signed-by=/usr/share/keyrings/vscodium-archive-keyring.gpg ] https://download.vscodium.com/debs vscodium main' \
    | sudo tee /etc/apt/sources.list.d/vscodium.list```

##### 3. Update the Package List:
     sudo apt update
##### 4. Install VSCodium:
     sudo apt install codium

### 2. Open the HTML File from Task Three in VSCodium

Once VSCodium is installed, you can open your HTML file from Task Three. Upon opening the file, you should notice that VSCodium highlights the HTML syntax.

#### Steps:
##### 1. Launch VSCodium:
      codium
##### 2. Open your HTML file:

- Navigate to `File > Open` and select the HTML file from Task Three.
- Syntax highlighting will be automatically applied.
##### Improving the HTML using Emmet:
Emmet allows you to write concise HTML code that expands into full markup. For example, you can type:  
`ul>li*3`  
And after pressing Tab, it expands into:
```
<ul>
    <li></li>
    <li></li>
    <li></li>
</ul>
```

### 3. Open the Python Script from Task Three in VSCodium
You will also open the Python script from Task Three in VSCodium to edit and enhance the script.
#### Steps:
##### 1. Open your Python script in VSCodium:
- Navigate to `File > Open` and select the Python script.
- Observe the syntax highlighting.
#### Adding the Shebang:
Add the following line at the very top of the Python script:
`#!/usr/bin/env python3`  

This shebang allows the script to be executed directly by telling the system to use Python 3 as the interpreter.

### 4. Execute the Python Script without Using the Python Command
#### Steps:
##### 1. Make the script executable:
`chmod +x script.py`
##### 2. Run the script directly without the python command:
`./script.py`  
The shebang (`#!/usr/bin/env python3`) enables the script to be executed directly without needing to invoke the `python` command explicitly.
### 5. Upload the Changed Files to the taskeight Repo
Once both files (HTML and Python) are updated and tested, upload them to your taskeight GitHub repository.
