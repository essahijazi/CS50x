# CS50x Solutions and Local Environment Setup

Setting Up Local Environment for CS50

This guide will help you set up a local development environment for CS50, including configuring necessary tools and libraries.

Prerequisites:

Before you begin, ensure you have the following installed:
- Operating System: macOS (for this guide), or Linux/Windows with adjustments as needed.
- Command Line Tools: Terminal (macOS), or Git Bash (Windows).

Step-by-Step Setup Guide:

1. Install CS50 Library

   First, install Homebrew:
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   Then, use Homebrew to install the CS50 library:
   ```sh
   brew install cs50
   ```

2. Configure Compiler

   Ensure that `clang`, the C language compiler, is installed:
   ```sh
   xcode-select --install
   ```

3. Setup Shell Configuration (for Zsh users)

   If you are using Zsh, you have two options to set up the environment variables.

   Option A: Setup `.zshrc`

   Edit your `.zshrc` file to include the CS50 library path:
   ```sh
   nano ~/.zshrc
   ```
   Add the following line at the end of the file:
   ```sh
   export DYLD_LIBRARY_PATH=/usr/local/lib
   ```
   Save and exit the editor (CTRL + X, then Y, and Enter).

   Source the `.zshrc` file to apply the changes:
   ```sh
   source ~/.zshrc
   ```

   Option B: Setup `.zprofile` (if using Zsh and `.zprofile` exists)

   Edit your `.zprofile` file to include the CS50 library path:
   ```sh
   nano ~/.zprofile
   ```
   Add the following line at the end of the file:
   ```sh
   export DYLD_LIBRARY_PATH=/usr/local/lib
   ```
   Save and exit the editor (CTRL + X, then Y, and Enter).

   Source the `.zprofile` file to apply the changes:
   ```sh
   source ~/.zprofile
   ```

4. Verify the Environment Variable

   Check that the `DYLD_LIBRARY_PATH` environment variable is set correctly:
   ```sh
   echo $DYLD_LIBRARY_PATH
   ```
   You should see output similar to this:
   ```sh
   /usr/local/lib
   ```

5. Clone CS50 Solutions

   Clone the CS50 solutions repository:
   ```sh
   git clone git@github.com:essahijazi/CS50x.git
   ```

6. Compile and Run CS50 Programs

   Navigate to your program directory and use `make` to compile your programs. For example, to compile a program named `caesar`:
   ```sh
   cd path/to/your/program
   make caesar
   ```
   Replace `caesar` with the actual name of your program.

   Run your compiled program:
   ```sh
   ./caesar
   ```

Additional Resources:

- CS50 Documentation: https://cs50.harvard.edu/
- CS50 GitHub Repository: https://github.com/cs50
