# n-Least Significant Bit(s) Steganography

[![GitHub Last Commit](https://img.shields.io/github/last-commit/mtabidze/nLSBs-Steganography.svg?branch=main)](https://github.com/mtabidze/nLSBs-Steganography/commits/main)
[![Testing Workflow Status](https://github.com/mtabidze/nLSBs-Steganography/actions/workflows/testing-flow.yml/badge.svg?branch=main)](https://github.com/mtabidze/llm-co-writer/actions/workflows/testing-flow.yml)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/mtabidze/nLSBs-Steganography.svg)](https://github.com/mtabidze/nLSBs-Steganography/pulls)
[![GitHub Release](https://img.shields.io/github/release/mtabidze/nLSBs-Steganography.svg)](https://github.com/mtabidze/nLSBs-Steganography/releases)

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=flat&logo=macos&logoColor=F0F0F0)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=flat&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Atom](https://img.shields.io/badge/Atom-%2366595C.svg?style=flat&logo=atom&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=flat&logo=github&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=flat&logo=githubactions&logoColor=white)
![Dependabot](https://img.shields.io/badge/dependabot-025E8C?style=flat&logo=dependabot&logoColor=white)

---

## Introduction

n-Least Significant Bit(s) Steganography is a versatile Python library designed for seamless message insertion and extraction within images using the n-Least Significant Bits technique. This library empowers users to embed confidential information into images while maintaining visual integrity, and subsequently retrieve hidden messages with ease. 

---

## Example
### Message
The message to be inserted into the image: 

>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### Images
The input image and resulting image with the message inserted.
![The input and resulting images](tools/SampleImages.png?raw=true)

---

## Performance Measurement and Optimization

| Function   | Repetitions | Baseline | Optimization 1 | Optimization 2 | Optimization 3 | Optimization 4 | Optimization 5 |
|------------|-------------|----------|----------------|----------------|----------------|----------------|----------------|
| insertion  | 1000        | 2.61     | 1.99           | 1.68           | 1.29           | 1.78           | 4.86           |
| extraction | 1000        | 1.23     | 0.96           | 0.79           | 0.79           | 0.82           | 2.91           |

![The optimization plot](tools/optimization/OptimizationPlot.png?raw=true)

- Optimization 1: Replace string manipulations with bitwise operations.
- Optimization 2: Utilize the NumPy library. 
- _best_ Optimization 3: Implement stable pixel updating. 
- Optimization 4: Employ the C extension module. 
- Optimization 5: Leverage PyPy, an alternative implementation of Python

Please read [OPTIMIZATION.md](OPTIMIZATION.md) for more details.

---

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process.