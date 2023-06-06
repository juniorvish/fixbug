# fixbug

A CLI app that helps you find solutions to unhandled exceptions in your code by using the OpenAI API.

## Installation

1. Clone the repository:

```
git clone https://github.com/juniorvish/fixbug.git
```

2. Change to the `fixbug` directory:

```
cd fixbug
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Make the `fixbug.py` script executable:

```
chmod +x fixbug.py
```

5. Add the `fixbug` directory to your PATH:

### Ubuntu

Edit your `.bashrc` or `.zshrc` file and add the following line:

```
export PATH=$PATH:/path/to/fixbug
```

Replace `/path/to/fixbug` with the actual path to the `fixbug` directory.

### Windows

1. Open the Start menu, right-click on "Computer" and select "Properties".
2. Click on "Advanced system settings" and then the "Environment Variables" button.
3. In the "System variables" section, find the "Path" variable, select it, and click "Edit".
4. Add the path to the `fixbug` directory at the end of the "Variable value" field, separated by a semicolon (`;`).

## Usage

Run your code with the `fixbug` command followed by your usual command:

```
fixbug python main.py
```

or

```
fixbug npm start
```

When an unhandled exception occurs, the app will print the error and suggest possible ways to solve it using the OpenAI API.