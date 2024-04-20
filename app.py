import streamlit as st
import pandas as pd

st.title('BMI計算')
st.text('身長・体重を入力してください')

with st.form(key='bmi_form'):
    col1, col2 = st.columns(2)
    with col1:
        height_input = st.text_input('身長 (cm)')
    with col2:
        weight_input = st.text_input('体重 (kg)')

    submitted = st.form_submit_button('計算')

    if submitted:
        try:
            height = float(height_input) #convert the text to float number
            weight = float(weight_input) #convert the text to float number
            if height <= 0 or weight <= 0:
                st.error("身長と体重は0より大きい値である必要があります。")
            else:
                bmi = weight / ((height/100) * (height/100))
                ideal_weight = (height/100) * (height/100) * 22
                st.text(f'あなたのBMIは{bmi:.2f}です。')
                st.text(f'適正体重{ideal_weight:.2f}kg')
                if(bmi < 18.5):
                    st.text(f'低体重 (やせ)')
                elif(bmi >= 18.5 and bmi < 25):
                    st.text(f'普通体重')
                elif(bmi >= 25 and bmi < 30):
                    st.text(f'肥満 (1度)')
                elif(bmi >= 30 and bmi < 35):
                    st.text(f'肥満 (2度)')
                elif(bmi >= 35 and bmi < 40):
                    st.text(f'肥満 (3度)')
                elif(bmi >= 40):
                    st.text(f'肥満 (4度)')
        except ValueError:
            st.error("身長と体重は数値で入力してください。")

st.write('')
st.subheader("BMI計算式")
st.text("BMI = 体重 ÷ (身長×身長)")

st.write('')
st.subheader("適正体重計算式")
st.text("適正体重(kg) = 身長 × 身長 × 22")

st.write('')
st.subheader('肥満判定')
data = {
    'BMI' : ['18.5未満', '18.5～25未満', '25～30未満', '30～35未満', '35～40未満', '40以上'],
    '肥満の判定' : ['低体重', '普通体重', '肥満1度', '肥満2度', '肥満3度', '肥満4度']
    }
df = pd.DataFrame(data)
st.table(df)

