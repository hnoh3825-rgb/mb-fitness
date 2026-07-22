import streamlit as st
import pandas as pd
import time

# إعدادات الصفحة
st.set_page_config(page_title="CROSSFIT & FITNESS", page_icon="🏋️‍♂️", layout="centered")

# ==================== خلفية داكنة فخمة وتنسيق الخطوط والعناوين ====================
bg_img_url = "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=1200&auto=format&fit=crop"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Tajawal:wght@400;700;900&display=swap');

    /* خلفية التطبيق */
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.78), rgba(0, 0, 0, 0.88)), url("{bg_img_url}") no-repeat center center fixed;
        background-size: cover !important;
        font-family: 'Tajawal', sans-serif;
    }}
    
    /* حاوية المحتوى الرئيسية */
    .main .block-container {{
        background-color: rgba(15, 15, 15, 0.75) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px 25px;
        margin-top: 20px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.8);
        color: #ffffff;
    }}

    /* العنوان الرئيسي - سطر واحد متناسق بدون كسور */
    .hero-title {{
        text-align: center;
        font-family: 'Montserrat', sans-serif;
        font-size: 28px;
        font-weight: 900;
        letter-spacing: 2px;
        white-space: nowrap; /* إجبار النص على سطر واحد */
        background: linear-gradient(135deg, #FFFFFF 0%, #D4AF37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 10px;
        margin-bottom: 10px;
    }}

    /* الوصف الفرعي الجديد */
    .hero-subtitle {{
        text-align: center;
        font-family: 'Tajawal', sans-serif;
        font-size: 16px;
        color: #CCCCCC;
        margin-bottom: 25px;
        font-weight: 500;
    }}

    /* خط الفاصل الأنيق */
    .custom-divider {{
        height: 1px;
        background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(212,175,55,0.5) 50%, rgba(255,255,255,0) 100%);
        margin: 20px 0 30px 0;
    }}

    /* تحسين ألوان التبويبات */
    .stTabs [data-baseweb="tab-list"] button {{
        color: #CCCCCC !important;
        font-family: 'Tajawal', sans-serif;
        font-weight: 700;
        font-size: 16px;
    }}
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
        color: #D4AF37 !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ==================== الواجهة العلوية المعدلة ====================
st.markdown('<div class="hero-title">CROSSFIT & FITNESS</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">دليلك اليومي لبناء القوة، اللياقة، والالتزام</div>', unsafe_allow_html=True)
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# إنشاء التبويبات
tab_workouts, tab_weight, tab_calories, tab_water = st.tabs([
    "🔥 التمارين", 
    "⚖️ الوزن", 
    "📊 السعرات", 
    "💧 الماء"
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
                "url": "https://www.youtube.com/watch?v=72BSZupb-1I"
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
