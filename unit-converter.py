import os
import re


class TerminalUnitConverter:
    def __init__(self):
        # Conversion dictionaries
        self.conversions = {
            "Length": {
                "Nanometer": 1e-9,
                "Micrometer": 1e-6,
                "Millimeter": 1e-3,
                "Centimeter": 1e-2,
                "Meter": 1,
                "Kilometer": 1e3,
                "Inch": 0.0254,
                "Foot": 0.3048,
                "Yard": 0.9144,
                "Mile": 1609.34,
                "Nautical mile": 1852
            },
            "Mass": {
                "Microgram": 1e-9,
                "Milligram": 1e-6,
                "Gram": 1e-3,
                "Kilogram": 1,
                "Metric ton": 1000,
                "Ounce": 0.0283495,
                "Pound": 0.453592,
                "Stone": 6.35029,
                "US ton": 907.185,
                "Imperial ton": 1016.05
            },
            "Volume": {
                "Milliliter": 1e-6,
                "Cubic centimeter": 1e-6,
                "Liter": 0.001,
                "Cubic meter": 1,
                "Gallon (US)": 0.00378541,
                "Quart (US)": 0.000946353,
                "Pint (US)": 0.000473176,
                "Cup (US)": 0.000236588,
                "Fluid ounce (US)": 2.9574e-5,
                "Gallon (UK)": 0.00454609,
                "Quart (UK)": 0.00113652,
                "Pint (UK)": 0.000568261,
                "Cup (UK)": 0.000284131,
                "Fluid ounce (UK)": 2.84131e-5
            },
            "Temperature": {
                "Celsius": "Celsius",
                "Fahrenheit": "Fahrenheit",
                "Kelvin": "Kelvin"
            },
            "Area": {
                "Square millimeter": 1e-6,
                "Square centimeter": 1e-4,
                "Square meter": 1,
                "Square kilometer": 1e6,
                "Hectare": 10000,
                "Square inch": 0.00064516,
                "Square foot": 0.092903,
                "Square yard": 0.836127,
                "Acre": 4046.86,
                "Square mile": 2.59e6
            },
            "Time": {
                "Nanosecond": 1e-9,
                "Microsecond": 1e-6,
                "Millisecond": 1e-3,
                "Second": 1,
                "Minute": 60,
                "Hour": 3600,
                "Day": 86400,
                "Week": 604800,
                "Month": 2.628e6,
                "Year": 3.154e7,
                "Decade": 3.154e8,
                "Century": 3.154e9
            },
            "Speed": {
                "Meter per second": 1,
                "Kilometer per hour": 0.277778,
                "Mile per hour": 0.44704,
                "Knot": 0.514444,
                "Foot per second": 0.3048
            },
            "Data": {
                "Bit": 1,
                "Byte": 8,
                "Kilobit": 1e3,
                "Kilobyte": 8e3,
                "Megabit": 1e6,
                "Megabyte": 8e6,
                "Gigabit": 1e9,
                "Gigabyte": 8e9,
                "Terabit": 1e12,
                "Terabyte": 8e12,
                "Petabit": 1e15,
                "Petabyte": 8e15
            }
        }
        
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Display the program header."""
        print("=" * 60)
        print("GOOGLE-STYLE UNIT CONVERTER".center(60))
        print("=" * 60)
        print()
        
    def print_menu(self):
        """Print the main menu of categories."""
        self.print_header()
        print("Categories:")
        for idx, category in enumerate(self.conversions.keys(), 1):
            print(f"{idx}. {category}")
        print("0. Exit")
        print()
    
    def get_units(self, category):
        """Get list of units for a category."""
        return list(self.conversions[category].keys())
    
    def print_units(self, units):
        """Print the list of available units."""
        for idx, unit in enumerate(units, 1):
            print(f"{idx}. {unit}")
    
    def validate_input(self, value):
        """Validate if the input is a valid number."""
        return bool(re.match(r'^-?\d*\.?\d*$', value) and value)
    
    def convert(self, category, from_unit, to_unit, value):
        """Perform the unit conversion."""
        try:
            if category == "Temperature":
                result = self.convert_temperature(float(value), from_unit, to_unit)
            else:
                from_factor = self.conversions[category][from_unit]
                to_factor = self.conversions[category][to_unit]
                result = float(value) * from_factor / to_factor
                
            # Format result based on magnitude
            if abs(result) < 0.001 or abs(result) >= 10000:
                formatted_result = f"{result:.6e}"
            else:
                formatted_result = f"{result:.6f}".rstrip('0').rstrip('.')
                
            return f"{value} {from_unit} = {formatted_result} {to_unit}"
            
        except ValueError:
            return "Error: Please enter a valid number"
        except Exception as e:
            return f"Error: {str(e)}"
            
    def convert_temperature(self, value, from_unit, to_unit):
        """Convert temperature between different units."""
        # Convert from source temperature to Kelvin first
        if from_unit == "Celsius":
            kelvin = value + 273.15
        elif from_unit == "Fahrenheit":
            kelvin = (value - 32) * 5/9 + 273.15
        else:  # Kelvin
            kelvin = value
            
        # Convert from Kelvin to target temperature
        if to_unit == "Celsius":
            return kelvin - 273.15
        elif to_unit == "Fahrenheit":
            return (kelvin - 273.15) * 9/5 + 32
        else:  # Kelvin
            return kelvin
    
    def run(self):
        """Main program loop."""
        while True:
            self.print_menu()
            try:
                category_choice = input("Select a category (0-8): ")
                
                if category_choice == '0':
                    print("Thank you for using the Unit Converter. Goodbye!")
                    break
                    
                if not category_choice.isdigit() or int(category_choice) < 1 or int(category_choice) > len(self.conversions):
                    raise ValueError("Invalid category selection.")
                    
                # Get selected category
                categories = list(self.conversions.keys())
                selected_category = categories[int(category_choice) - 1]
                units = self.get_units(selected_category)
                
                # Display the units for the selected category
                self.clear_screen()
                self.print_header()
                print(f"Category: {selected_category}")
                print("\nAvailable units:")
                self.print_units(units)
                print()
                
                # Get FROM unit
                from_choice = input("Select FROM unit (number): ")
                if not from_choice.isdigit() or int(from_choice) < 1 or int(from_choice) > len(units):
                    raise ValueError("Invalid unit selection.")
                from_unit = units[int(from_choice) - 1]
                
                # Get TO unit
                to_choice = input("Select TO unit (number): ")
                if not to_choice.isdigit() or int(to_choice) < 1 or int(to_choice) > len(units):
                    raise ValueError("Invalid unit selection.")
                to_unit = units[int(to_choice) - 1]
                
                # Get value to convert
                value = input(f"Enter value to convert from {from_unit}: ")
                if not self.validate_input(value):
                    raise ValueError("Invalid number.")
                
                # Perform conversion
                result = self.convert(selected_category, from_unit, to_unit, value)
                
                # Display result
                self.clear_screen()
                self.print_header()
                print("RESULT:")
                print(f"{result}")
                print("\nPress Enter to continue...")
                input()
                
            except ValueError as e:
                print(f"Error: {str(e)}")
                print("\nPress Enter to continue...")
                input()
                self.clear_screen()
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
                print("\nPress Enter to continue...")
                input()
                self.clear_screen()


if __name__ == "__main__":
    converter = TerminalUnitConverter()
    converter.run()