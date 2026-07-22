import streamlit as st
import pandas as pd
import time

# إعدادات الصفحة وتغيير الأيقونة اللي تطلع برة في المتصفح (غيرناها هنا إلى ذراع قوية أو تقدر تحط أي إيموجي)
st.set_page_config(
    page_title="CROSSFIT & FITNESS", 
    page_icon="🦾", 
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

    [data-testid="stHorizontalBlock"] {{
        display: flex !important;
        flex-direction: row !important;
        gap: 6px !important;
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
        padding: 10px 2px !important;
        color: #E0E0E0 !important;
        font-family: 'Tajawal', sans-serif !important;
        font-weight: 800 !important;
        font-size: 12px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5) !important;
        transition: all 0.3s ease-in-out !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
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

# ==================== القائمة الجانبية (Sidebar) ====================
with st.sidebar:
    st.markdown("<h2 style='color: #D4AF37; text-align: center; margin-bottom: 0;'>⚙️ لوحة التحكم PRO</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align:center; color:#A0A0A0;'>الإضافات والأدوات المتقدمة</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 🎯 تحديد الهدف")
    user_goal = st.radio("هدف التدريب:", ["🔥 حرق دهون وتنشيف", "💪 بناء ضخامة وقوة", "⚡ زيادة لياقة وتحمل"], index=0)
    
    st.markdown("---")
    
    st.markdown("### ⏱️ غرفة المؤقتات المتقدمة")
    timer_mode = st.selectbox("اختر نوع المؤقت:", ["Tabata (20ث/10ث)", "EMOM (دقيقة لكل جولة)", "AMRAP (أقصى جولات)"])
    if st.button("بدء المؤقت المختار 🚀", key="side_timer_pro"):
        with st.empty():
            st.warning(f"⚡ تشغيل: {timer_mode}")
            time.sleep(2)
            st.success("🔥 انطلق بقوة! GO!")
            st.balloons()

    st.markdown("---")

    st.markdown("### 🍽️ حاسبة الماكروز الشاملة")
    target_cals = st.number_input("السعرات اليومية:", value=2000, step=100)
    prot = int((target_cals * 0.3) / 4)
    carbs = int((target_cals * 0.4) / 4)
    fats = int((target_cals * 0.3) / 9)
    st.info(f"🥩 بروتين: **{prot}g**\n\n🍞 كربوهيدرات: **{carbs}g**\n\n🥑 دهون: **{fats}g**")

    st.markdown("---")

    st.markdown("### 📋 قائمة الانضباط والعادات")
    st.checkbox("تمرين الكروس فيت اليومي")
    st.checkbox("شرب 3 لتر ماء")
    st.checkbox("أخذ كفايتك من النوم")
    st.checkbox("الالتزام بالوجبات الصحية")

# ==================== العنوان الرئيسي ====================
st.markdown('<div class="hero-title">CROSSFIT & FITNESS</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">دليلك اليومي لبناء القوة، اللياقة، والالتزام</div>', unsafe_allow_html=True)
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# ==================== حالة التنقل بين الأقسام ====================
if "active_page" not in st.session_state:
    st.session_state.active_page = "workouts"

# ==================== الأزرار العلوية المنسقة بالكامل ====================
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🔥 التمارين", key="btn_workouts"):
        st.session_state.active_page = "workouts"
        st.rerun()

with col2:
    if st.button("📊 الأرقام", key="btn_weight"):
        st.session_state.active_page = "weight"
        st.rerun()

with col3:
    if st.button("⚡ السعرات", key="btn_calories"):
        st.session_state.active_page = "calories"
        st.rerun()

with col4:
    if st.button("💧 الماء", key="btn_water"):
        st.session_state.active_page = "water"
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# ==================== 1. قسم التمارين ====================
if st.session_state.active_page == "workouts":
    st.header("🏃‍♂️ جداول الكروس فيت (جسم كامل)")
    
    crossfit_data = {
        "تمارين حرق وقوة (Bodyweight 🔥)": [
            {
                "title": "تمرين البيربيز الشامل",
                "english_name": "Burpees",
                "sets": "3 جلسات",
                "reps": "12 تكرار",
                "desc": "تمرين كروس فيت متكامل يشارك فيه كامل الجسم، يرفع معدل ضربات القلب ويضاعف حرق الدهون.",
                "url": "https://www.youtube.com/watch?v=dZgVxmf6jkA"
            },
            {
                "title": "تمرين نط الحبل والقفز",
                "english_name": "Jumping Jacks",
                "sets": "3 جلسات",
                "reps": "45 ثانية",
                "desc": "تمرين إحماء وتوافق حركي ممتاز لضخ الأكسجين وتحفيز الدورة الدموية.",
                "url": "https://www.youtube.com/watch?v=c4DAnQ6DtF8"
            },
            {
                "title": "تمرين تسلق الجبل",
                "english_name": "Mountain Climbers",
                "sets": "3 جلسات",
                "reps": "20 تكرار لكل رجل",
                "desc": "يقوي عضلات البطن والجذع والأكتاف مع رفع اللياقة البدنية والتحمل.",
                "url": "https://www.youtube.com/watch?v=nmwgirgXLYM"
            }
        ],
        "تمارين الجزء السفلي والكتلة (Legs & Core 🦵)": [
            {
                "title": "تمرين سكوات القفز التفجيري",
                "english_name": "Jump Squats",
                "sets": "4 جلسات",
                "reps": "15 تكرار",
                "desc": "تمرين تفجيري قوي يستهدف عضلات الفخذين والمقعدة لزيادة القوة والسرعة.",
                "url": "https://www.youtube.com/watch?v=72BSZupb-1I"
            },
            {
                "title": "تمرين الطعن المتبادل",
                "english_name": "Lunges",
                "sets": "3 جلسات",
                "reps": "12 تكرار لكل رجل",
                "desc": "ممتاز جداً لتقوية عضلات الأرجل وتحسين التوازن وثبات الركبتين.",
                "url": "https://www.youtube.com/watch?v=QOVaHwm-Q6U"
            }
        ],
        "تمارين الجزء العلوي والتحمل (Upper Body 🦾)": [
            {
                "title": "تمرين الضغط الكلاسيكي",
                "english_name": "Push-ups",
                "sets": "4 جلسات",
                "reps": "15 تكرار",
                "desc": "التمرين الأساسي لتقوية عضلات الصدر، الأكتاف الأمامية، والترايسبس.",
                "url": "https://www.youtube.com/watch?v=IODxDxX7oi4"
            },
            {
                "title": "تمرين البلانك للثبات",
                "english_name": "Plank Hold",
                "sets": "3 جلسات",
                "reps": "45 ثانية ثبات",
                "desc": "تمرين ثبات هائل يقوي الجذع والبطن بالكامل ويحمي أسفل الظهر من الإصابات.",
                "url": "https://www.youtube.com/watch?v=pSHjTRCQxIw"
            }
        ]
    }

    category = st.selectbox("اختر نوع الجلسة:", list(crossfit_data.keys()))
    st.markdown("---")
    
    for ex in crossfit_data[category]:
        card_html = f"""
        <div class="exercise-card">
            <div class="exercise-title">{ex['title']} ({ex['english_name']})</div>
            <div class="badge-container">
                <span class="badge-item">🔁 {ex['sets']}</span>
                <span class="badge-item">🎯 {ex['reps']}</span>
            </div>
            <div class="exercise-desc">📌 {ex['desc']}</div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        st.video(ex["url"])
        st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("⏱️ مؤقت راحة الجولات")
    seconds = st.number_input("وقت الراحة بين الجولات (ثانية):", min_value=10, max_value=120, value=45, step=5)
    if st.button("تفعيل مؤقت الجولة 🔔", key="btn_timer"):
        with st.empty():
            for i in range(seconds, 0, -1):
                st.write(f"⏳ المتبقي للجولة القادمة: **{i}** ثانية")
                time.sleep(1)
            st.success("🔥 انطلقت الجولة التالية! GO!")

# ==================== 2. قسم الأرقام والوزن الأسبوعي ====================
elif st.session_state.active_page == "weight":
    st.header("⚖️ متابعة الوزن الأسبوعي وفارق الفقدان")
    
    if "weight_data" not in st.session_state:
        st.session_state.weight_data = []

    c1, c2, c3 = st.columns(3)
    with c1:
        week_number = st.selectbox("اختر الأسبوع:", ["الأسبوع 1", "الأسبوع 2", "الأسبوع 3", "الأسبوع 4", "الأسبوع 5", "الأسبوع 6", "الأسبوع 7", "الأسبوع 8"])
    with c2:
        new_weight = st.number_input("أدخل وزنك هذا الأسبوع (كجم):", min_value=30.0, max_value=200.0, value=75.0, step=0.1)
    with c3:
        pr_lift = st.number_input("أقصى وزن رفعته (PR كجم):", min_value=0.0, max_value=300.0, value=100.0, step=2.5)

    if st.button("حفظ الوزن والسجل الأسبوعي 💾", key="save_w"):
        diff_text = "الوزن الأولي (بداية المتابعة)"
        if st.session_state.weight_data:
            last_weight = st.session_state.weight_data[-1]["الوزن الفعلي (كجم)"]
            diff = round(new_weight - last_weight, 2)
            if diff < 0:
                diff_text = f"📉 نزلت {abs(diff)} كجم عن الأسبوع الماضي"
            elif diff > 0:
                diff_text = f"📈 زدت {diff} كجم عن الأسبوع الماضي"
            else:
                diff_text = "⚖️ الوزن ثابت مقارنة بالأسبوع الماضي"

        st.session_state.weight_data.append({
            "الفترة": week_number, 
            "الوزن الفعلي (كجم)": new_weight, 
            "التغير عن السابق": diff_text,
            "الرقم القياسي PR": pr_lift
        })
        st.success("تم حفظ سجل الأسبوع بنجاح!")

    if st.session_state.weight_data:
        df = pd.DataFrame(st.session_state.weight_data)
        
        if len(df) > 1:
            first_w = df.iloc[0]["الوزن الفعلي (كجم)"]
            current_w = df.iloc[-1]["الوزن الفعلي (كجم)"]
            total_diff = round(current_w - first_w, 2)
            if total_diff < 0:
                st.metric("إجمالي الوزن المفقود منذ البداية", f"{abs(total_diff)} كجم 📉", delta_color="inverse")
            elif total_diff > 0:
                st.metric("إجمالي الوزن المكتسب منذ البداية", f"{total_diff} كجم 📈", delta_color="inverse")
            else:
                st.metric("إجمالي التغير في الوزن", "0 كجم")

        st.dataframe(df, use_container_width=True)
        st.line_chart(df.set_index("الفترة")[["الوزن الفعلي (كجم)"]])

# ==================== 3. قسم السعرات ====================
elif st.session_state.active_page == "calories":
    st.header("🔥 حاسبة احتياج الطاقة للكروس فيت")
    
    height = st.number_input("الطول (سم):", value=170)
    weight_c = st.number_input("الوزن (كجم):", value=70)
    age = st.number_input("العمر:", value=25)
    gender = st.radio("النوع:", ["ذكر", "أنثى"], horizontal=True)

    if st.button("حساب الاحتياج اليومي 🧮", key="calc_c"):
        if gender == "ذكر":
            bmr = 10 * weight_c + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight_c + 6.25 * height - 5 * age - 161

        tdee = int(bmr * 1.6)

        st.metric("احتياجك اليومي للمحافظة على الوزن", f"{tdee} سعرة")
        st.write(f"📉 للتنشيف ونزول الوزن: **{tdee - 400}** سعرة")
        st.write(f"📈 للضخامة وزيادة الكتلة: **{tdee + 350}** سعرة")

# ==================== 4. قسم الماء ====================
elif st.session_state.active_page == "water":
    st.header("💧 متابعة استهلاك الماء")
    
    if "water_cups" not in st.session_state:
        st.session_state.water_cups = 0

    st.subheader(f"شربت اليوم: {st.session_state.water_cups} كاسات 🥤")
    st.progress(min(st.session_state.water_cups / 12.0, 1.0))
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("إضافة كاس ماء ➕", key="add_w"):
            st.session_state.water_cups += 1
            st.rerun()
    with col2:
        if st.button("تصفير 🔄", key="rst_w"):
            st.session_state.water_cups = 0
            st.rerun()
