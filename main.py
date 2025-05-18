import streamlit as st

# Conversion data
conversions = {
    "length": {"meter": 1, "kilometer": 0.001, "mile": 0.000621371, "yard": 1.09361},
    "weight": {"gram": 1, "kilogram": 0.001, "pound": 0.00220462, "ounce": 0.035274},
    "temperature": lambda v, f, t: v * 1.8 + 32 if f == "celsius" and t == "fahrenheit" else (v - 32) / 1.8 if f == "fahrenheit" and t == "celsius" else v,
    "area": {
        "square_feet": 1, "square_yard": 1/9, "marla": 1/272.25, "kanal": 1/5445, 
        "acre": 1/43560, "murabba": 1/1089000, "hectare": 1/107639
    },
    "volume": {"liter": 1, "milliliter": 1000, "cubic_meter": 0.001, "gallon": 0.264172},
    "digital": {"bit": 1, "byte": 1/8, "kilobyte": 1/8000, "megabyte": 1/8e+6, "gigabyte": 1/8e+9}
}

# Streamlit UI
st.title("🧮 Simple Unit Converter")

category = st.selectbox("Select Category", list(conversions.keys()))
from_unit = st.selectbox("From Unit", list(conversions[category]) if category != "temperature" else ["celsius", "fahrenheit"])
to_unit = st.selectbox("To Unit", list(conversions[category]) if category != "temperature" else ["celsius", "fahrenheit"])
value = st.number_input("Enter Value", min_value=0.0, step=0.1)

# Local Conversion Function
def convert(value, from_unit, to_unit):
    if category == "temperature":
        return conversions[category](value, from_unit, to_unit)
    else:
        return value * (conversions[category][to_unit] / conversions[category][from_unit])

if st.button("Convert"):
    try:
        result = convert(value, from_unit, to_unit)
        st.success(f"Converted Value: {result:.4f} {to_unit}")
    except Exception as e:
        st.error(f"Conversion error: {e}")
