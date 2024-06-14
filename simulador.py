import streamlit as st
st.title(":rainbow[Simulador de compra]")
def multiplicacao(v1, q1):
    return v1 * q1
total_compra = 0
i = 0

while True:
    v1 = st.number_input("Adicione o valor do produto", key=f'v1_{i}')
    q1 = st.number_input("Quantidade do produto", value=0, key=f'q1_{i}')
    resultado1 = multiplicacao(v1, q1)
    total_compra += resultado1
    st.write("Valor do produto de acordo com a quantidade é: ", resultado1)
    st.write("Valor atual da compra: ", total_compra)
    fim = st.radio("Deseja continuar? ", ["Sim", "Não"], key=f'fim_{i}')
    if fim == "Não":
        break
    i += 1
st.write("O resultado final da compra é: ", total_compra)