import streamlit as st

# Function to calculate Ohm's Law
def calculate_ohms_law(voltage, current, resistance):
    if voltage == '':
        voltage = current * resistance
        return voltage, "Voltage (V)"
    elif current == '':
        current = voltage / resistance
        return current, "Current (I)"
    elif resistance == '':
        resistance = voltage / current
        return resistance, "Resistance (R)"
    else:
        return None, "Please leave one field empty to calculate the unknown value."

# Streamlit App
def main():
    st.title("Ohm's Law Calculator")
    
    st.write("This app calculates the unknown parameter in Ohm's Law (V = I * R).")
    
    voltage = st.text_input("Enter Voltage (V) in Volts:", value='')
    current = st.text_input("Enter Current (I) in Amperes:", value='')
    resistance = st.text_input("Enter Resistance (R) in Ohms:", value='')
    
    if st.button("Calculate"):
        result, param = calculate_ohms_llaw(voltage, current, resistance)
        if result:
            st.write(f"{param}: {result:.2f}")
        else:
            st.write("Please provide valid inputs.")

if __name__ == "__main__":
    main()
