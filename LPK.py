# Library
import streamlit as st

# Write
st.title('Software Perkalian')
st.subheader('Ini adalah aplikasi untuk mengalikan bilangan bulat')

# Input bilangan pertama
number1 = st.number_input('masukan bilangan pertama')
st.write(f'bilangan pertama adalah {number1}')

# Input bilangan kedua
number2 = st.number_input('masukan bilangan kedua')
st.write(f'bilangan pertama adalah {number2}')

# Hasil kali
hasil = number1*number2

if st.button('Hitung'):
    st.write(f'Hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('silahkan pencet tombol hitung!')