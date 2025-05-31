# f'prime: Calculus-Powered Graphing App
![image](https://github.com/user-attachments/assets/7511ab89-9018-4e23-beae-a4cc6bf85683)

A Python-based calculator application with a graphical user interface built using tkinter. This application allows users to input mathematical functions and perform numerical integration.

## Project Structure

```
fprime/
├── assets/
│   ├── fonts/
│   │   └── Poppins-Medium.ttf
│   └── frame0/
│       └── (image assets)
├── build/
│   └── requirements.txt
├── gui.py
├── integration.py
└── README.md
```

## Features

- Input mathematical functions using Python syntax (e.g., `x**3-3*x`)
- Calculate numerical integrals using scipy.integrate.quad()
- Display integration results
- Modern and user-friendly interface

## Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- pyglet>=1.5.0
- sympy>=1.8
- scipy>=1.7.0
- numpy>=1.20.0

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/punyeeta/fprime.git
   cd fprime
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Make sure the Poppins-Medium.ttf font is in the `assets/fonts/` directory.

## Running the Application

Run the application with:
```
python gui.py
```

## Usage

1. Enter a mathematical function in the input field using Python syntax (e.g., `x**3-3*x`)
2. Enter the lower and upper limits for integration
3. Click the "Calculate" button to compute the integral
4. The result will be displayed in the "Result for numerical integration" field

## Notes

- The application uses the Poppins Medium font. If the font is not found, it will display a warning message.
- All assets are loaded from relative paths, making the application portable across different operating systems.
- The integration is performed using scipy.integrate.quad(), which provides a numerical approximation of the integral.

## Contributors

| Avatar | Name | GitHub |
|--------|------|--------|
| <img src="https://avatars.githubusercontent.com/u/199071096?v=4" width="60"/> | Heart Chiong | [@Aarchie14](https://github.com/Aarchie14) |
| <img src="https://avatars.githubusercontent.com/u/150583091?v=4" width="60"/> | Mark Vincent Limpahan | [@markvncent](https://github.com/markvncent) |
| <img src="https://avatars.githubusercontent.com/u/144111787?v=4" width="60"/> | Rhenel Jhon Sajol | [@Tetsuuya](https://github.com/Tetsuuya) |
| <img src="https://avatars.githubusercontent.com/u/163762221?v=4" width="60"/> | Charles Sorongon | [@charlesgiovanne](https://github.com/charlesgiovanne) |


## License

MIT License 
