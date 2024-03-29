#!/bin/bash

# Function to check if a Python package is installed
is_package_installed() {
    python -c "import $1" >/dev/null 2>&1
}

# List of required Python packages
packages="uvicorn fastapi numpy scikit-learn bs4 requests imgkit"

# Navigate to the directory containing your Python code
cd Backend

# Loop through the list of packages and install if not already installed
for package in $packages; do
    if ! is_package_installed "$package"; then
        echo "Installing $package..."
        pip install "$package"
    else
        echo "$package is already installed."
    fi
done

