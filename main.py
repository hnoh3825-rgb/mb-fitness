import streamlit as st
import pandas as pd
import time

# إعدادات الصفحة
st.set_page_config(page_title="تطبيق MB للتمارين", page_icon="🏋️‍♂️", layout="centered")

st.title("🏋️‍♂️ MB FITNESS")
st.write("تطبيقك الشخصي الشامل للتمارين والمتابعة اليومية")

# إنشاء Tabs (تبويبات) للتنقل داخل التطبيق
tab_workouts, tab_weight, tab_calories, tab_water = st.tabs([
    "🏋️‍♂️ التمارين", 
    "⚖️ سجل الوزن", 
    "🔥 السعرات", 
    "💧 شرب الماء"
])

# ==================== 1. تبويب التمارين ====================
with tab_workouts:
    st.header("جدول التمارين اليومي")
    
    # بيانات التمارين بروابط صور ثابتة ومباشرة شغال 100%
    workouts_data = {
        "تمارين الصدر 💪": [
            {"name": "1. بنش برس مستوي (Bench Press) - 4×10", "img": "https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=500&q=80"},
            {"name": "2. بنش برس مائل أعلى (Incline Press) - 3×12", "img": "https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?w=500&q=80"},
            {"name": "3. تجميع فراشة (Chest Fly) - 3×15", "img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&q=80"}
        ],
        "تمارين الظهر 🏋️‍♂️": [
            {"name": "1. سحب عريض علوي (Lat Pulldown) - 4×12", "img": "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?w=500&q=80"},
            {"name": "2. سحب أرضي (Seated Row) - 4×10", "img": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500&q=80"},
            {"name": "3. قطنية (Deadlift) - 3×8", "img": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500&q=80"}
        ],
        "تمارين الأرجل 🦵": [
            {"name": "1. سكوات (Squat) - 4×10", "img": "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=500&q=80"},
            {"name": "2. دفع أرجل (Leg Press) - 4×12", "img": "https://images.unsplash.com/photo-1434682881908-b43d0467b798?w=500&q=80"}
        ],
        "تمارين الذراعين 🦾": [
            {"name": "1. بايسبس بالبار (Barbell Curl) - 4×12", "img": "https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?w=500&q=80"},
            {"name": "2. ترايسبس حبل (Pushdown) - 4×12", "img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&q=80"}
        ]
    }

    category = st.selectbox("اختر العضلة:", list(workouts_data.keys()))
    st.markdown("---")
    
    for ex in workouts_data[category]:
        st.subheader(ex["name"])
        # استخدام st.image لعرض الصور المباشرة بشكل متوافق
        st.image(ex["img"], use_container_width=True)
        st.markdown("---")

    # مؤقت الراحة بين الجلسات
    st.subheader("⏱️ مؤقت الراحة بين الجلسات")
    seconds = st.number_input("اختر وقت الراحة بالثواني:", min_value=10, max_value=180, value=60, step=10)
    if st.button("تفعيل المؤقت 🔔"):
        with st.empty():
            for i in range(seconds, 0, -1):
                st.write(f"⏳ المتبقي: **{i}** ثانية")
                time.sleep(1)
            st.success("🎉 انتهى وقت الراحة! ابدأ الجلسة التالية.")

# ==================== 2. تبويب سجل الوزن ====================
with tab_weight:
    st.header("⚖️ متابعة الوزن اليومي")
    
    if "weight_data" not in st.session_state:
        st.session_state.weight_data = []

    new_weight = st.number_input("أدخل وزنك اليوم (كجم):", min_value=30.0, max_value=200.0, value=75.0, step=0.1)
    if st.button("حفظ الوزن 💾"):
        today = time.strftime("%Y-%m-%d")
        st.session_state.weight_data.append({"التاريخ": today, "الوزن (كجم)": new_weight})
        st.success("تم حفظ الوزن بنجاح!")

    if st.session_state.weight_data:
        df = pd.DataFrame(st.session_state.weight_data)
        st.dataframe(df)
        st.line_chart(df.set_index("التاريخ"))

# ==================== 3. تبويب السعرات ====================
with tab_calories:
    st.header("🔥 حاسبة الاحتياج اليومي من السعرات")
    
    height = st.number_input("الطول (سم):", value=170)
    weight_c = st.number_input("الوزن (كجم):", value=70)
    age = st.number_input("العمر:", value=25)
    gender = st.radio("النوع:", ["ذكر", "أنثى"])
    activity = st.selectbox("مستوى النشاط:", [
        "قليل النشاط (مكتبي)",
        "نشاط متوسط (3-5 أيام تمرين)",
        "نشاط عالي (6-7 أيام تمرين)"
    ])

    if st.button("احسب السعرات 🧮"):
        if gender == "ذكر":
            bmr = 10 * weight_c + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight_c + 6.25 * height - 5 * age - 161

        mult = 1.2 if "قليل" in activity else (1.55 if "متوسط" in activity else 1.725)
        tdee = int(bmr * mult)

        st.metric("احتياجك اليومي للمحافظة على الوزن", f"{tdee} سعرة")
        st.write(f"📉 للتنشيف (تنزيل الوزن): **{tdee - 500}** سعرة")
        st.write(f"📈 للتضخيم (زيادة الوزن): **{tdee + 300}** سعرة")

# ==================== 4. تبويب الماء ====================
with tab_water:
    st.header("💧 متابعة استهلاك الماء اليومي")
    
    if "water_cups" not in st.session_state:
        st.session_state.water_cups = 0

    st.subheader(f"شربت اليوم: {st.session_state.water_cups} كاسات 🥤")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("إضافة كاس ماء ➕"):
            st.session_state.water_cups += 1
            st.rerun()
    with col2:
        if st.button("تصفير العداد 🔄"):
            st.session_state.water_cups = 0
            st.rerun()
