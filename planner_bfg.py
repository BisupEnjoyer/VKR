import streamlit as st
import pandas as pd

# Заголовок приложения
st.title('Расчет оперативного плана производства')

# Загрузка файла с данными о заказах
uploaded_file = st.file_uploader("Загрузите файл с данными о заказах (CSV формат)", type=["csv"])

# Расчет оперативного плана производства
if uploaded_file is not None:
    st.subheader('Данные о заказах:')
    
    # Чтение данных из загруженного файла
    orders_df = pd.read_csv(uploaded_file)
    
    # Расчет потребности в материалах и мощностях (здесь можно добавить свои расчеты)
    # Пример:
    materials_needed = orders_df.groupby('Название продукта')['Количество'].sum()
    capacity_needed = orders_df.shape[0]  # Пример простого расчета мощностей
    
    # Вывод результатов
    st.write('Потребность в материалах:')
    st.write(materials_needed)
    st.write('Потребность в мощностях:', capacity_needed)

# Пример использования:
# ID заказа, Название продукта, Количество
# 1, Продукт А, 100
# 2, Продукт В, 150
# 3, Продукт А, 200
