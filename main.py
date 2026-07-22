import streamlit as st
import pandas as pd
import time

# إعدادات الصفحة
st.set_page_config(page_title="تطبيق MB للتمارين", page_icon="⚡", layout="centered")

# ==================== خلفية دكنة وفخمة بتصميم NO EXCUSES عبر CSS ====================
st.markdown(
    """
    <style>
    /* خلفية متدرجة سوداء رياضية فخمة جداً متوافقة مع جميع الأجهزة */
    .stApp {
        background: linear-gradient(135deg, #0b0c10 0%, #1f2833 50%, #000000 100%);
        background-attachment: fixed;
    }
    
    /* تصميم حاوية المحتوى الرئيسي */
    .main .block-container {
        background-color: rgba(15, 15, 15, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 18px;
        padding: 25px;
        margin-top: 15px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
        color: white;
    }

    /* شعار تحفيزي في أعلى التطبيق */
    .motivation-banner {
        text-align: center;
        font-family: 'Impact', sans-serif;
        font-size: 28px;
        letter-spacing: 4px;
        color: #e5e5e5;
        border-bottom: 2px solid #66fcf1;
        padding-bottom: 10px;
        margin-bottom: 20px;
        text-transform: uppercase;
    }

    /* تحسين شكل التبويبات */
    .stTabs [data-baseweb="tab-list"] button {
        color: white !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# هيدر تحفيزي للتطبيق
st.markdown('<div class="motivation-banner">NO EXCUSES ⚡</div>', unsafe_allow_html=True)

st.title("⚡ MB CROSSFIT & FITNESS")
st.write("تمارين كروس فيت وفيديوهات توضيحية مباشرة تحت كل تمرين")

# إنشاء التبويبات
tab_workouts, tab_weight, tab_calories, tab_water = st.tabs([
    "🔥 تمارين الكروس فيت", 
    "⚖️ سجل الوزن", 
    "📊 السعرات", 
    "💧 شرب الماء"
])

# ==================== 1. تبويب تمارين الكروس فيت ====================
with tab_workouts:
    st.header("🏃‍♂️ جداول الكروس فيت (جسم كامل)")
    
    crossfit_data = {
        "تمارين حرق وقوة (Bodyweight 🔥)": [
            {
                "name": "1. بيربيز (Burpees) - 3 جلسات × 12 تكرار",
                "desc": "تمرين كروس فيت شامل يرفع اللياقة ويحرق الدهون بسرعة.",
                "url": "https://www.youtube.com/watch?v=dZgVxmf6jkA"
            },
            {
                "name": "2. نط الحبل / القفز (Jumping Jacks) - 3 جلسات × 45 ثانية",
                "desc": "ممتاز لرفع ضغط الدم وضخ الأكسجين للجسم.",
                "url": "https://www.youtube.com/watch?v=c4DAnQ6DtF8"
            },
            {
                "name": "3. تسلق الجبل (Mountain Climbers) - 3 جلسات × 20 لكل رجل",
                "desc": "يقوي عضلات البطن، الأكتاف، والأرجل.",
                "url": "https://www.youtube.com/watch?v=nmwgirgXLYM"
            }
        ],
        "تمارين الجزء السفلي والكتلة (Legs & Core 🦵)": [
            {
                "name": "1. سكوات قفز (Jump Squats) - 4 جلسات × 15 تكرار",
                "desc": "تمرين تفجيري للأرجل لزيادة اللياقة والقوة.",
                "url": "https://www.youtube.com/watch?v=A-cFYWvaB1Q"
            },
            {
                "name": "2. الطعن (Lunges) - 3 جلسات × 12 تكرار لكل رجل",
                "desc": "لتقوية عضلات الفخذين والاتزان.",
                "url": "https://www.youtube.com/watch?v=QOVaHwm-Q6U"
            }
        ],
        "تمارين الجزء العلوي والتحمل (Upper Body 🦾)": [
            {
                "name": "1. بوش أب (Push-ups) - 4 جلسات × 15 تكرار",
                "desc": "الأساسي للصدر، الأكتاف، والترايسبس.",
                "url": "https://www.youtube.com/watch?v=IODxDxX7oi4"
            },
            {
                "name": "2. بلانك ثبات (Plank Hold) - 3 جلسات × 45 ثانية",
                "desc": "تمرين ثبات قوي جداً لشد البطن والجذع بالكامل.",
                "url": "https://www.youtube.com/watch?v=pSHjTRCQxIw"
            }
        ]
    }

    category = st.selectbox("اختر نوع الجلسة:", list(crossfit_data.keys()))
    st.markdown("---")
    
    for ex in crossfit_data[category]:
        st.subheader(ex["name"])
        st.caption(ex["desc"])
        st.video(ex["url"])
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
        st.session_state.weight_data.append({"التاريخ": today, "الوزن (كجم)": new_weight})
        st.success(f"تم حفظ الوزن ({new_weight} كجم).")

    if st.session_state.weight_data:
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
        if gender == "ذكر":
            bmr = 10 * weight_c + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight_c + 6.25 * height - 5 * age - 161

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
