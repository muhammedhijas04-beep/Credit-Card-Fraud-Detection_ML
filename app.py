import streamlit as st
import numpy as np
import joblib
import pandas as pd


# Load model and scaler
#==========================

model = joblib.load("fraud_model.pkl") # Pre-trained Random Forest model
scaler = joblib.load("scaler.pkl")     # Pre-fitted StandardScaler



# Page config  
#==========================


st.set_page_config(
    page_title="Fraud Detection System", # → Browser tab name
    page_icon="🏦", # → Browser tab icon
    layout="wide"  # → Use wide mode for more space
)


# Sidebar 
#===========================

st.sidebar.title("🏦 Fraud Detection System")
st.sidebar.markdown("### Transaction Risk Analyzer")
st.sidebar.info("This system detects fraudulent credit card transactions using a trained ML model.")

st.sidebar.markdown("---")
st.sidebar.write("Model: Random Forest")
st.sidebar.write("Dataset: Credit Card Fraud (ULB)")

st.sidebar.markdown("---")
page = st.sidebar.radio(        # Page selection
    "select mode",
    ["CSV fraud scanner","Manual fraud scanner"])


# page 1: CSV fraud scanner
#================================

if page == "CSV fraud scanner": # If user selects CSV mode, this page opens.

    # Page content for CSV fraud scanner
    st.title("📁 CSV Fraud Scanner")
    st.markdown("Upload a CSV file with transaction details to analyze fraud risk.")

    
    uploaded_file = st.file_uploader("Choose transaction CSV file", type=["csv"]) # Creates a file upload button.

    if uploaded_file is not None: # If a file is uploaded, it will read csv to pd.DataFrame
        data = pd.read_csv(uploaded_file)

        # Remove Class column if present
        if "Class" in data.columns: 
            data = data.drop(columns=["Class"])

        st.subheader("Uploaded Data")
        st.dataframe(data.head(), use_container_width=True) # Display first few rows of uploaded data

        st.info("CSV must contain columns: Time, V1 to V28, Amount") # Inform user about required columns

        if st.button("🚨 Scan Transactions for Fraud"): 

            # Ensure correct column order
            expected_cols = ["Time"] + [f"V{i}" for i in range(1,29)] + ["Amount"] # This ensures correct column order:
            X = data[expected_cols] # Model requires exact same order as training.

            X_scaled = scaler.transform(X) #Scales the input using trained scaler.

            prediction = model.predict(X_scaled) 
            probabilities = model.predict_proba(X_scaled)[:, 1]

            data["Fraud Probability (%)"] = probabilities * 100
            data["Prediction"] = np.where(prediction == 1, "Fraud", "Legitimate") # Add prediction results to DataFrame

            st.subheader("📃 Scan Results")
            st.dataframe(data, use_container_width=True) # Display results

            csv = data.to_csv(index=False).encode("utf-8") # Convert DataFrame to CSV for download
            st.download_button(
                "📥 Download Results",
                csv,
                "fraud_scan_results.csv",  
                "text/csv"
            ) # Download button for results


# page 2: Manual fraud scanner
#================================

elif page == "Manual fraud scanner":
    st.title("📝 Manual Fraud Scanner")
    st.markdown("Input transaction details manually to analyze fraud risk.")

    st.divider()

# input section 

    st.subheader("💳 Transaction Input Details")

    input=[] # To collect user inputs from columns

    col1, col2, col3 = st.columns(3) # Three columns for better layout

    with col1:
        st.markdown("time & Amount") # Time and Amount inputs
        time = st.number_input("transcation time ⏱️(seconds)",min_value = 0, max_value = 200000)
        amount = st.number_input("transcation amount 💰",min_value = 0.0, max_value = 50000.0)

    input.append(time) # add time to inputs list
    input.append(amount) # add amount to inputs list

    with col2:
        st.markdown("transcation features (V1 - V15)")

        for i in range(1,15): # Loop through V1 to V14
            value = st.number_input(f"v{i}")
            input.append(value) # add value to inputs list

    with col3:
        st.markdown("transcation features (V16 - V29)")

        for i in range(15,29):
            value = st.number_input(f"v{i}")
            input.append(value) # add value to inputs list


    st.divider()

#==============================================================
# Prediction Section 
#==============================================================


    st.subheader("🔍 Fraud Prediction")

    if st.button("🚨 Predict Fraud Risk"):

    # Convert input list to numpy array
       input_array = np.array(input).reshape(1, -1)

    # Scale input
       input_scaled = scaler.transform(input_array)

    # Predict
       prediction = model.predict(input_scaled)[0]
       confidence = model.predict_proba(input_scaled)[0][1]

       st.divider()

    # Result Panel
       st.subheader("📊 Prediction Result")

       if prediction == 1: 
          st.error("🚨 Fraudulent Transaction Detected!")
       else:
          st.success("✅ Transaction is Legitimate")

       col_r1, col_r2 = st.columns(2) 

       with col_r1:
          st.metric("Fraud Probability", f"{confidence*100:.2f}%") 

       with col_r2:
           if confidence > 0.7:
                st.error("🚨 High Risk Fraud Transaction") 
           elif confidence > 0.4:
                st.warning("⚠️ Medium Risk Fraud Transaction")  
           else:
                st.success("✅ Low Risk Transaction")


    
