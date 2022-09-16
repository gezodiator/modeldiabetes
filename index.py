import streamlit as st

n_bar = st.sidebar.radio("Navigation",["Home", "Hasil", "Visualisasi"])

#home section

#home section
if n_bar == "Home":
    st.markdown("<h1 style='text-align: center;'>Prediksi Model Machine Learning Diabetes Menggunakan Metode Regression Linear</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image("gambar diabet.jpg")

    with col3:
        st.write(' ')

    st.markdown("<h2 style='text-align: center;'>Kevin Kristio </h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>13118639 </h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Universitas Gunadarma </h2>", unsafe_allow_html=True)

    #Result
if n_bar == "Hasil":
    st.title("Hasil")
    col1, col2 = st.columns(2)
    col1.metric("R2 Score", "85.54%")
    col2.metric("RMSE", "14.46%")
    
    #Visualization
if n_bar == "Visualisasi":
    st.title("Visualisasi")
    st.image("linear regression.png")