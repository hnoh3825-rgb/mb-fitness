import streamlit as st
import pandas as pd
import time

# إعدادات الصفحة
st.set_page_config(
    page_title="CROSSFIT & FITNESS", 
    page_icon="🏋️‍♂️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==================== CSS التجميل الشامل للتبويبات والواجهة ====================
bg_img_url = "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=1200&auto=format&fit=crop"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Tajawal:wght@400;700;900&display=swap');

    /* خلفية التطبيق الداكنة والاحترافية */
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.93)), url("{bg_img_url}") no-repeat center center fixed;
        background-size: cover !important;
        font-family: 'Tajawal', sans-serif;
    }}
    
    /* حاوية المحتوى الرئيسية */
    .main .block-container {{
        background-color: rgba(18, 18, 18, 0.85) !important;
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 30px 22px;
        margin-top: 10px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.9);
        color: #ffffff;
    }}

    /* العنوان الرئيسي بصيغة مودرن */
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
        margin-top: 5px;
        margin-bottom: 6px;
    }}

    /* الوصف الفرعي */
    .hero-subtitle {{
        text-align: center;
        font-family: 'Tajawal', sans-serif;
        font-size: 14px;
        color: #A0A0A0;
        margin-bottom: 20px;
        font-weight: 500;
    }}

    /* خط الفاصل */
    .custom-divider {{
        height: 1px;
        background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(212,175,55,0.4) 50%, rgba(255,255,255,0) 100%);
        margin: 15px 0 25px 0;
    }}

    /* ==================== إعادة تصميم الأزرار العلوية بالكامل (التمارين، الوزن، السعرات، الماء) ==================== */
    div[data-testid="stTabs"] [data-baseweb="tab-list"] {{
        display: grid !important;
        grid-template-columns: repeat(4, 1fr) !important;
        gap: 12px !important;
        background: transparent !important;
        padding: 5px 0 !important;
        border: none !important;
    }}

    div[data-testid="stTabs"] [data-baseweb="tab-list"] button {{
        background: linear-gradient(145deg, rgba(30, 30, 35, 0.9), rgba(15, 15, 20, 0.95)) !important;
        border: 1px solid rgba(212, 175, 55, 0.25) !important;
        border-radius: 16px !important;
        padding: 14px 8px !important;
        color: #D0D0D0 !important;
        font-family: 'Tajawal', sans-serif !important;
        font-weight: 800 !important;
        font-size: 15px !important;
        text-align: center !important;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.5) !important;
        transition: all 0.3s ease-in-out !important;
        height: auto !important;
    }}

    /* عند التمرير بالماوس أو تحديد التبويب (Hover & Active) */
    div[data-testid="stTabs"] [data-baseweb="tab-list"] button:hover {{
        border-color: #D4AF37 !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(212, 175, 55, 0.2) !important;
    }}

    div[data-testid="stTabs"] [data-baseweb="tab-list"] button[aria-selected="true"] {{
        background: linear-gradient(135deg, #D4AF37 0%, #AA820A 100%) !important;
        color: #000000 !important;
        font-weight: 900 !important;
        border: 1px solid #FFE885 !important;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.6) !important;
        transform: translateY(-2px) !important;
    }}

    /* إخفاء الخط السفلي المزعج الافتراضي في streamlit */
    div[data-testid="stTabs"] [data-baseweb="tab-highlight-title"] {{
        display: none !important;
    }}

    /* تصميم بطاقة التمرين */
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

    /* القائمة الجانبية (Sidebar) */
    [data-testid="stSidebar"] {{
        background-color: rgba(12, 12, 12, 0.96) !important;
        backdrop-filter: blur(20px);
        border-left: 1px solid rgba(212, 175, 55, 0.3);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ==================== القائمة الجانبية (Side Panel) ====================
with st.sidebar:
    st.markdown("<h2 style='color: #D4AF37; text-align: center;'>⚙️ أدوات القوة والتحكم</h2>", unsafe_allow_html=True)
    st.caption("مركز الخيارات المتقدمة والأدوات المساعدة")
    st.markdown("---")
    
    # 1. هدف التدريب
    st.subheader("🎯 تحديد الهدف")
    user_goal = st.radio("حدد هدفك الحالي:", ["🔥 تنشيف وحرق دهون", "💪 بناء ضخامة وقوة", "⚡ زيادة لياقة وتحمل"], index=0)
    
    st.markdown("---")
    
    # 2. حاسبة الماكروز
    st.subheader("🍽️ توزيع الماكروز اليومي")
    target_cals = st.number_input("السعرات المستهدفة:", value=2000, step=100)
    prot = int((target_cals * 0.3) / 4)
    carbs = int((target_cals * 0.4) / 4)
    fats = int((target_cals * 0.3) / 9)
    st.caption(f"🥩 بروتين: **{prot}g** | 🍞 كربوهيدرات: **{carbs}g** | 🥑 دهون: **{fats}g**")
    
    st.markdown("---")
    
    # 3. قائمة التحدي اليومي
    st.subheader("📋 قائمة الالتزام اليومي")
    st.checkbox("أكملت تمرين الكروس فيت")
    st.checkbox("شربت 3 لتر ماء")
    st.checkbox("حققت هدف البروتين")
    st.checkbox("نوم كافٍ (7-8 ساعات)")
    
    st.markdown("---")
    
    # 4. مؤقت التاباتا
    st.subheader("⏱️ مؤقت التاباتا (Tabata)")
    if st.button("بدء مؤقت التاباتا السريع 🚀"):
        with st.empty():
            st.warning("🔥 **WORK! (تمرين 20 ثانية)**")
            time.sleep(2)
            st.success("💧 **REST! (راحة 10 ثواني)**")
            time.sleep(1)
            st.balloons()

    st.markdown("---")
    
    # 5. دفتر الملاحظات
    st.subheader("📝 ملاحظاتك الخاصة")
    st.text_area("سجل إنجازاتك اليوم:", placeholder="اكتب هنا ملاحظاتك...")

# ==================== الهيدر والعنوان الرئيسي ====================
st.markdown('<div class="hero-title">CROSSFIT & FITNESS</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">دليلك اليومي لبناء القوة، اللياقة، والالتزام</div>', unsafe_allow_html=True)
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# ==================== الأزرار العلوية بالأشكال والتنسيقات الفخمة الجديدة ====================
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

    # مؤقت راحة الجولات
    st.subheader("⏱️ مؤقت راحة الجولات")
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
