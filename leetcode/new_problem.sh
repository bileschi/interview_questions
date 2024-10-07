#!/bin/bash
#
# Creates the directories for a leetcode problem, following the template
# for python and rust
#
# Usage: new_problem.sh <problem_number>
# Example: new_problem.sh 1

# Set strict mode
set -euo pipefail
IFS=$'\n\t'

if [ "$#" -ne 1 ]; then
    echo "Usage: new_problem.sh <problem_number>"
    echo "Example: new_problem.sh 1"
    exit 1
fi

# Parse command line arguments
verbose=false

format_digit() {
    local digit=$1
    if [[ ! -z "${digit//[0-9]/}" ]]; then
        echo "Invalid digit"
        exit 1
    fi
    if [ ${#digit} -eq 1 ]; then
        echo "000$digit"
    elif [ ${#digit} -eq 2 ]; then
        echo "00$digit"
    elif [ ${#digit} -eq 3 ]; then
        echo "0$digit"
    elif [ ${#digit} -eq 4 ]; then
        echo "$digit"
    else 
        echo "Invalid digit"
        exit 1
    fi
}

# Main function
main() {
    # Your script logic here
    if $verbose; then
        echo "Processing file: $file"
    fi

    # Check the input and convert to a four character digit.
    local digit=$(format_digit "$1")
    echo "$digit"

    # # Create the directories
    mkdir -p "problemsets/$digit"

    # Copy the python template
    cp -R template/py "problemsets/$digit/py/"
    # Replace the string $$DIGIT_GOES_HERE$$ with the problem number
    sed -i '' "s/\$\$DIGIT_GOES_HERE\$\$/$1/g" "problemsets/$digit/py/main.py"
    sed -i '' "s/\$\$DIGIT_GOES_HERE\$\$/$1/g" "problemsets/$digit/py/test_main.py"

    # Create the rust version
    mkdir -p "problemsets/$digit/rust"
    cargo new "problemsets/$digit/rust/solution"
    
    # Print the commands to run the tests
    echo ""
    echo "Python:"
    echo "   python3 problemsets/$digit/py/test_main.py"
    echo "Rust:"
    echo "   cargo run --manifest-path problemsets/$digit/rust/solution/Cargo.toml"

}

# Run the main function
main "$@"
