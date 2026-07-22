import streamlit as st
import pandas as pd
import time

# إعدادات الصفحة
st.set_page_config(page_title="تطبيق MB للتمارين", page_icon="⚡", layout="centered")

# عنوان التطبيق
st.title("⚡ MB CROSSFIT & FITNESS")
st.write("تمارين لياقة وحرق للجسم كامل (CrossFit) - نسخة الجوال المضمونة")

# إنشاء التبويبات
tab_workouts, tab_weight, tab_calories, tab_water = st.tabs([
    "🔥 تمارين الكروس فيت", 
    "⚖️ سجل الوزن", 
    "📊 السعرات", 
    "💧 شرب الماء"
])

# ==================== 1. تبويب تمارين الكروس فيت ====================
with tab_workouts:
    st.header("🏃‍♂️ جداول الكروس فيت المعتمدة")
    
    # روابط GIF مباشرة ومستقرة جداً لضمان العمل على الجوال
    crossfit_data = {
        "تمارين حرق وقوة (Bodyweight 🔥)": [
            {
                "name": "1. بيربيز (Burpees) - 3 جلسات × 12 تكرار",
                "desc": "تمرين شامل يرفع اللياقة فوراً.",
                "gif_url": "https://i.imgur.com/vHq8S7l.gif"
            },
            {
                "name": "2. نط الحبل (Jumping Jacks) - 3 جلسات × 45 ثانية",
                "desc": "ممتاز لتحمية وضخ الدم للجسم.",
                "gif_url": "https://i.imgur.com/D4A9T99.gif"
            },
            {
                "name": "3. تسلق الجبل (Mountain Climbers) - 3×20 تكرار",
                "desc": "يقوي البطن، الأكتاف، والأرجل.",
                "gif_url": "https://i.imgur.com/kS9Z0Xb.gif"
            }
        ],
        "تمارين الجزء السفلي والكتلة (Legs & Core 🦵)": [
            {
                "name": "1. سكوات (Bodyweight Squat) - 4 جلسات × 15",
                "desc": "الأساسي لقوة الأرجل والتحمل.",
                "gif_url": "https://i.imgur.com/YIu0v7x.gif"
            },
            {
                "name": "2. سكوات قفز (Jump Squats) - 3 جلسات × 12",
                "desc": "تمرين تفجيري للأرجل ورفع الحرق.",
                "gif_url": "https://i.imgur.com/A6E75xV.gif"
            }
        ],
        "تمارين الجزء العلوي والتحمل (Upper Body 🦾)": [
            {
                "name": "1. بوش أب (Push-ups) - 4 جلسات × 15 تكرار",
                "desc": "الأساسي للصدر، الأكتاف، والترايسبس.",
                "gif_url": "https://i.imgur.com/2Y44bFp.gif"
            },
            {
                "name": "2. بلانك (Plank) - 3 جلسات × 45 ثانية ثبات",
                "desc": "تمرين ثبات قوي جداً للبطن والجذع.",
                "gif_url": "https://i.imgur.com/Ue5Vp9r.gif"
            }
        ]
    }

    category = st.selectbox("اختر نوع الجلسة:", list(crossfit_data.keys()))
    st.markdown("---")
    
    for ex in crossfit_data[category]:
        st.subheader(ex["name"])
        st.caption(ex["desc"])
        
        # الطريقة البرمجية المضمونة لعرض الـ GIF على الجوال:
        # نقوم بعرض الصورة مباشرة باستخدام رابطها مع خاصية العرض الكامل
        st.image(ex["gif_url"], use_container_width=True)
        st.markdown("---")

    # مؤقت راحة الجولات
    st.subheader("⏱️ مؤقت جولات الكروس فيت")
    seconds = st.number_input("وقت الراحة بين الجولات (ثانية):", min_value=10, max_value=120, value=45, step=5)
    if st.button("تفعيل مؤقت الجولة 🔔"):
        with st.empty():
            for i in range(seconds, 0, -1):
                st.write(f"⏳ المتبقي للجولة القادمة: **{i}** ثانية")
                time.sleep(1)
            st.success("🔥 انطلقت الجولة التالية! GO!")

# ==================== 2. تبويب سجل الوزن ====================
with tab_weight:
    st.header("⚖️ متابعة الوزن اليومي")
    
    if "weight_data" not in st.session_state:
        st.session_state.weight_data = []

    new_weight = st.number_input("أدخل وزنك اليوم (كجم):", min_value=30.0, max_value=200.0, value=75.0, step=0.1)
    if st.button("حفظ الوزن 💾"):
        today = time.strftime("%Y-%m-%d")
        # حفظ تاريخ اليوم مع الوزن
        st.session_state.weight_data.append({"التاريخ": today, "الوزن (كجم)": new_weight})
        st.success(f"تم حفظ الوزن ({new_weight} كجم) بتاريخ اليوم.")

    if st.session_state.weight_data:
        # عرض البيانات في جدول ورسم بياني
        df = pd.DataFrame(st.session_state.weight_data)
        st.dataframe(df)
        st.line_chart(df.set_index("التاريخ"))

# ==================== 3. تبويب السعرات ====================
with tab_calories:
    st.header("🔥 حاسبة احتياج الطاقة للكروس فيت")
    
    height = st.number_input("الطول (سم):", value=170)
    weight_c = st.number_input("الوزن (كجم):", value=70)
    age = st.number_input("العمر:", value=25)
    gender = st.radio("النوع:", ["ذكر", "أنثى"])

    if st.button("حساب الاحتياج اليومي 🧮"):
        # معادلة ميفلين سانت جوير لحساب الـ BMR
        if gender == "ذكر":
            bmr = 10 * weight_c + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight_c + 6.25 * height - 5 * age - 161

        # للكروس فيت نعتمد معامل نشاط عالي جداً (1.6)
        tdee = int(bmr * 1.6)

        st.metric("احتياجك اليومي للمحافظة على الوزن", f"{tdee} سعرة")
        st.write(f"📉 للتنشيف ونزول الوزن: **{tdee - 400}** سعرة")

# ==================== 4. تبويب الماء ====================
with tab_water:
    st.header("💧 متابعة استهلاك الماء")
    
    if "water_cups" not in st.session_state:
        st.session_state.water_cups = 0

    st.subheader(f"شربت اليوم: {st.session_state.water_cups} كاسات 🥤")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("إضافة كاس ماء ➕"):
            st.session_state.water_cups += 1
            st.rerun()
    with col2:
        if st.button("تصفير 🔄"):
            st.session_state.water_cups = 0
            st.rerun()
