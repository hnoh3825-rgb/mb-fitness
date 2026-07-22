import streamlit as st
import pandas as pd
import time

# إعدادات الصفحة
st.set_page_config(
    page_title="CROSSFIT & FITNESS PRO", 
    page_icon="🏋️‍♂️", 
    layout="centered",
    initial_sidebar_state="expanded"
)

# ==================== CSS التجميل الشامل ====================
bg_img_url = "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=1200&auto=format&fit=crop"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Tajawal:wght@400;700;900&display=swap');

    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.88), rgba(0, 0, 0, 0.95)), url("{bg_img_url}") no-repeat center center fixed;
        background-size: cover !important;
        font-family: 'Tajawal', sans-serif;
    }}
    
    .main .block-container {{
        background-color: rgba(16, 16, 20, 0.88) !important;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 30px 20px;
        margin-top: 10px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.95);
        color: #ffffff;
    }}

    .hero-title {{
        text-align: center;
        font-family: 'Montserrat', sans-serif;
        font-size: 28px;
        font-weight: 900;
        letter-spacing: 2px;
        white-space: nowrap;
        background: linear-gradient(135deg, #FFFFFF 0%, #D4AF37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 2px;
        margin-bottom: 4px;
    }}

    .hero-subtitle {{
        text-align: center;
        font-family: 'Tajawal', sans-serif;
        font-size: 14px;
        color: #A0A0A0;
        margin-bottom: 20px;
        font-weight: 500;
    }}

    .custom-divider {{
        height: 1px;
        background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(212,175,55,0.4) 50%, rgba(255,255,255,0) 100%);
        margin: 15px 0 25px 0;
    }}

    /* أزرار التنقل العرضية الأفقية بجانب بعضها تماماً */
    [data-testid="stHorizontalBlock"] {{
        display: flex !important;
        flex-direction: row !important;
        gap: 8px !important;
        align-items: center !important;
        justify-content: space-between !important;
    }}

    [data-testid="stHorizontalBlock"] > div {{
        flex: 1 !important;
        min-width: 0 !important;
    }}

    .stButton > button {{
        width: 100% !important;
        background: linear-gradient(145deg, rgba(30, 30, 38, 0.9), rgba(18, 18, 24, 0.95)) !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 12px !important;
        padding: 10px 4px !important;
        color: #E0E0E0 !important;
        font-family: 'Tajawal', sans-serif !important;
        font-weight: 800 !important;
        font-size: 13px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5) !important;
        transition: all 0.3s ease-in-out !important;
        white-space: nowrap !important;
    }}

    .stButton > button:hover {{
        border-color: #D4AF37 !important;
        color: #FFFFFF !important;
        background: linear-gradient(135deg, rgba(212, 175, 55, 0.25) 0%, rgba(30, 30, 38, 0.95) 100%) !important;
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.35) !important;
        transform: translateY(-2px) !important;
    }}

    [data-testid="stSidebar"] {{
        background-color: rgba(12, 12, 16, 0.97) !important;
        backdrop-filter: blur(25px);
        border-left: 2px solid rgba(212, 175, 55, 0.4) !important;
    }}

    .exercise-card {{
        background: linear-gradient(145deg, rgba(30, 30, 30, 0.7), rgba(20, 20, 20, 0.8));
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-right: 4px solid #D4AF37;
        border-radius: 16px;
        padding: 18px;
        margin-top: 15px;
        margin-bottom: 12px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    }}

    .exercise-title {{
        font-size: 19px;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 10px;
    }}

    .badge-container {{
        display: flex;
        gap: 10px;
        margin-bottom: 12px;
        flex-wrap: wrap;
    }}

    .badge-item {{
        background: rgba(212, 175, 55, 0.12);
        color: #E2C055;
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 4px 12px;
        border-radius: 8px;
        font-size: 13px;
        font-weight: 700;
    }}

    .exercise-desc {{
        font-size: 14px;
        color: #C0C0C0;
        line-height: 1.6;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ==================== القائمة الجانبية (Sidebar من اليمين) ====================
with st.sidebar:
    st.markdown("<h2 style='color: #D4AF37; text-align: center; margin-bottom: 0;'>⚙️ لوحة التحكم PRO</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align:center; color:#A0A0A0;'>الإضافات والأدوات المتقدمة</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 🎯 نمط وهدف التدريب")
    user_goal = st.radio("حدد هدفك:", ["🔥 حرق دهون وتنشيف", "💪 بناء ضخامة وقوة", "⚡ زيادة لياقة وتحمل"], index=0)
    
    st.markdown("---")
    
    st.markdown("### ⏱️ غرفة المؤقتات المتقدمة")
    timer_type = st.selectbox("اختر نوع المؤقت:", ["Tabata (20ث تمرين / 10ث راحة)", "EMOM (دقيقة لكل جولة)", "AMRAP (أقصى جولات ممتدة)"])
    if st.button("تشغيل المؤقت 🚀", key="side_timer"):
        with st.empty():
            st.warning(f"⚡ بدء مؤقت: {timer_type}")
            time.sleep(2)
            st.success("🔥 انطلق بقوة! GO!")
            st.balloons()

    st.markdown("---")

    st.markdown("### 📋 سجل عادات الالتزام اليومية")
    st.checkbox("✔️ تمرين الكروس فيت اليومي")
    st.checkbox("✔️ شرب 3 لتر ماء كاملة")
    st.checkbox("✔️ الزام حصة البروتين")
    st.checkbox("✔️ النوم المبكر (7-8 ساعات)")

# ==================== العنوان الرئيسي ====================
st.markdown('<div class="hero-title">CROSSFIT & FITNESS PRO</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">منصة اللياقة المتكاملة - أداء، تغذية، ومتابعة متطورة</div>', unsafe_allow_html=True)
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# ==================== حالة التنقل بين الأقسام (أفقي بالكامل) ====================
if "active_page" not in st.session_state:
    st.session_state.active_page = "workouts"

# 4 خيارات أفقية متجاورة تماماً
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🔥 التمارين", key="btn_workouts"):
        st.session_state.active_page = "workouts"
        st.rerun()

with col2:
    if st.button("⚖️ الوزن والـ PR", key="btn_weight"):
        st.session_state.active_page = "weight"
        st.rerun()

with col3:
    if st.button("📊 الماكروز", key="btn_calories"):
        st.session_state.active_page = "calories"
        st.rerun()

with col4:
    if st.button("💧 الترطيب", key="btn_water"):
        st.session_state.active_page = "water"
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# ==================== 1. قسم التمارين مع إضافات الصعوبة والمستويات ====================
if st.session_state.active_page == "workouts":
    st.header("🏃‍♂️ جداول الكروس فيت والمستويات المتقدمة")
    
    # فلتر مستوى الصعوبة الجديد
    diff_level = st.selectbox("فلترة حسب المستوى التدريبي:", ["الكل", "مبتدئ (Beginner)", "متوسط (Intermediate)", "محترف (Advanced)"])
    
    crossfit_data = [
        {
            "title": "تمرين البيربيز الشامل",
            "english_name": "Burpees",
            "category": "حرق وقوة",
            "level": "متوسط (Intermediate)",
            "sets": "3 جلسات",
            "reps": "12 تكرار",
            "desc": "تمرين كروس فيت متكامل يشارك فيه كامل الجسم، يرفع معدل ضربات القلب ويضاعف حرق الدهون.",
            "url": "https://www.youtube.com/watch?v=dZgVxmf6jkA"
        },
        {
            "title": "تمرين سكوات القفز التفجيري",
            "english_name": "Jump Squats",
            "category": "جزء سفلي",
            "level": "محترف (Advanced)",
            "sets": "4 جلسات",
            "reps": "15 تكرار",
            "desc": "تمرين تفجيري قوي يستهدف عضلات الفخذين والمقعدة لزيادة القوة والسرعة.",
            "url": "https://www.youtube.com/watch?v=72BSZupb-1I"
        },
        {
            "title": "تمرين الضغط الكلاسيكي",
            "english_name": "Push-ups",
            "category": "جزء علوي",
            "level": "مبتدئ (Beginner)",
            "sets": "4 جلسات",
            "reps": "15 تكرار",
            "desc": "التمرين الأساسي لتقوية عضلات الصدر، الأكتاف الأمامية، والترايسبس.",
            "url": "https://www.youtube.com/watch?v=IODxDxX7oi4"
        }
    ]

    for ex in crossfit_data:
        if diff_level == "الكل" or diff_level in ex["level"]:
            card_html = f"""
            <div class="exercise-card">
                <div class="exercise-title">{ex['title']} ({ex['english_name']})</div>
                <div class="badge-container">
                    <span class="badge-item">🎯 المستوى: {ex['level']}</span>
                    <span class="badge-item">🔁 {ex['sets']}</span>
                    <span class="badge-item">⚡ {ex['reps']}</span>
                </div>
                <div class="exercise-desc">📌 {ex['desc']}</div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            st.video(ex["url"])
            st.markdown("<br>", unsafe_allow_html=True)

# ==================== 2. قسم سجل الوزن والـ PRs (الإنجاز الشخصي) ====================
elif st.session_state.active_page == "weight":
    st.header("⚖️ متابعة الوزن القياسي وتسجيل الأرقام الشخصية (PR)")
    
    if "weight_data" not in st.session_state:
        st.session_state.weight_data = []

    c1, c2 = st.columns(2)
    with c1:
        new_weight = st.number_input("أدخل وزن الجسم الحالي (كجم):", min_value=30.0, max_value=200.0, value=75.0, step=0.1)
    with c2:
        pr_lift = st.number_input("أقصى وزن رفعته في الديدليفت / السكوات (كجم):", min_value=0.0, max_value=300.0, value=100.0, step=2.5)

    if st.button("حفظ السجل الجديد 💾", key="save_w"):
        today = time.strftime("%Y-%m-%d")
        st.session_state.weight_data.append({"التاريخ": today, "الوزن (كجم)": new_weight, "رقم قياسي PR": pr_lift})
        st.success("تم تحديث السجل الشخصي بنجاح!")

    if st.session_state.weight_data:
        df = pd.DataFrame(st.session_state.weight_data)
        st.dataframe(df, use_container_width=True)
        st.line_chart(df.set_index("التاريخ")[["الوزن (كجم)"]])

# ==================== 3. قسم السعرات والماكروز الشاملة ====================
elif st.session_state.active_page == "calories":
    st.header("📊 حاسبة السعرات والماكروز المتقدمة")
    
    c_h, c_w, c_a = st.columns(3)
    with c_h:
        height = st.number_input("الطول (سم):", value=170)
    with c_w:
        weight_c = st.number_input("الوزن (كجم):", value=70)
    with c_a:
        age = st.number_input("العمر:", value=25)
        
    gender = st.radio("النوع:", ["ذكر", "أنثى"], horizontal=True)

    if st.button("حساب تفصيلي دقيق 🧮", key="calc_c"):
        if gender == "ذكر":
            bmr = 10 * weight_c + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight_c + 6.25 * height - 5 * age - 161

        tdee = int(bmr * 1.55) # نشاط متوسط
        prot = int((tdee * 0.3) / 4)
        carbs = int((tdee * 0.4) / 4)
        fats = int((tdee * 0.3) / 9)

        st.metric("احتياج السعرات للمحافظة على الوزن", f"{tdee} سعرة حرارية")
        st.info(f"🥩 البروتين المقترح: **{prot}g** | 🍞 الكربوهيدرات: **{carbs}g** | 🥑 الدهون الصحية: **{fats}g**")
        st.success(f"📉 سعرات التنشيف وخسارة الدهون: **{tdee - 400}** سعرة | 📈 سعرات الضخامة: **{tdee + 350}** سعرة")

# ==================== 4. قسم الترطيب والعادات ====================
elif st.session_state.active_page == "water":
    st.header("💧 متابعة الترطيب والهدف اليومي للماء")
    
    if "water_cups" not in st.session_state:
        st.session_state.water_cups = 0

    st.subheader(f"المستهلك حتى الآن: {st.session_state.water_cups} من أصل 12 كاس مستهدف 🥤")
    st.progress(min(st.session_state.water_cups / 12.0, 1.0))
    
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        if st.button("إضافة كوب ماء ➕", key="add_w"):
            st.session_state.water_cups += 1
            st.rerun()
    with col2:
        if st.button("إعادة ضبط 🔄", key="rst_w"):
            st.session_state.water_cups = 0
            st.rerun()
