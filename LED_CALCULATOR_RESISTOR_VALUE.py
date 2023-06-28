# Header with LED voltage ranges
print("Dacian Florin Dedu | TikTok - @dacianflorindedu")
print("LEDs (Light Emitting Diodes)")
print("Voltage ranges and forward current")
print("Values are approximate and can vary depending on the specific LED model.")
print("   Red LED: 10-30 mA | 1.8-2.2 volts")
print("Yellow LED: 10-30 mA | 2.0-2.2 volts")
print(" Green LED: 10-30 mA | 2.0-3.2 volts")
print("  Blue LED: 20-30 mA | 3.0-3.6 volts")
print(" White LED: 20-30 mA | 3.0-3.6 volts")
print()
print("Calculate resistor value")
def calculate_resistor_value(power_source_voltage, led_voltage, led_current):
    # Calculate the voltage across the resistor
    voltage_across_resistor = power_source_voltage - led_voltage

    # Convert LED current from milliamperes to amperes
    led_current = led_current / 1000.0

    # Calculate the resistor value
    resistor_value = voltage_across_resistor / led_current

    return resistor_value

# Get user inputs
power_source_voltage = float(input("Enter power source voltage: "))
led_voltage = float(input("Enter LED voltage: "))
led_current = float(input("Enter LED current (in milliamperes): "))

# Calculate the resistor value
resistor_value = calculate_resistor_value(power_source_voltage, led_voltage, led_current)

# Print the result
print(f"R=({power_source_voltage} volt - {led_voltage} volt) / {led_current} milliampere = {resistor_value:.1f} ohms")

# Print the final result
print("Given a power source voltage of {}V, an LED voltage of {}V, and an LED current of {} milliamperes, the appropriate resistor value to limit the current is indeed {:.2f} ohms.".format(power_source_voltage, led_voltage, led_current, resistor_value))
