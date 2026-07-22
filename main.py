import streamlit as st
import pandas as pd
import time

# إعدادات الصفحة
st.set_page_config(
    page_title="CROSSFIT & FITNESS - نظام شخصي", 
    page_icon="🇸🇦", 
    layout="centered",
    initial_sidebar_state="expanded"
)

# ==================== CSS التصميم الشامل (توزيع علمي ومتساوی 100% للأزرار الأربعة) ====================
bg_img_url = "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=1200&auto=format&fit=crop"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Tajawal:wght@400;700;900&display=swap');

    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
        max-width: 100% !important;
        overflow-x: hidden !important;
    }}

    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.88), rgba(0, 0, 0, 0.95)), url("{bg_img_url}") no-repeat center center fixed;
        background-size: cover !important;
        font-family: 'Tajawal', sans-serif;
        overflow-x: hidden !important;
    }}
    
    .main .block-container {{
        background-color: rgba(16, 16, 20, 0.88) !important;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 25px 15px;
        margin-top: 10px;
        max-width: 100% !important;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.95);
        color: #ffffff;
        overflow-x: hidden !important;
    }}

    .hero-title {{
        text-align: center;
        font-family: 'Montserrat', sans-serif;
        font-size: 26px;
        font-weight: 900;
        letter-spacing: 2px;
        background: linear-gradient(135deg, #FFFFFF 0%, #D4AF37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 2px;
        margin-bottom: 4px;
    }}

    .hero-subtitle {{
        text-align: center;
        font-family: 'Tajawal', sans-serif;
        font-size: 13px;
        color: #A0A0A0;
        margin-bottom: 20px;
        font-weight: 500;
    }}

    .custom-divider {{
        height: 1px;
        background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(212,175,55,0.4) 50%, rgba(255,255,255,0) 100%);
        margin: 15px 0 25px 0;
    }}

    /* ==================== التوزيع الهندسي والعلمي المتساوي للأزرار الأربعة ==================== */
    div.row-widget.stHorizontal, [data-testid="stHorizontalBlock"] {{
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        align-items: stretch !important;
        justify-content: space-between !important;
        width: 100% !important;
        gap: 12px !important; /* مسافات وفراغات علمية متساوية ودقيقة */
        margin-bottom: 15px !important;
    }}

    [data-testid="stHorizontalBlock"] > div {{
        flex: 1 1 0% !important;
        max-width: 25% !important; /* ضمان تقسيم المساحة بالتساوي 25% لكل زر هندسياً */
        min-width: 0 !important;
    }}

    /* تصميم الأزرار مع ضمان احتواء النص بالكامل داخله بوضوح */
    .stButton > button {{
        width: 100% !important;
        height: 65px !important;
        background: linear-gradient(145deg, rgba(28, 28, 36, 0.95), rgba(16, 16, 22, 0.98)) !important;
        border: 1.5px solid rgba(212, 175, 55, 0.4) !important;
        border-radius: 16px !important;
        padding: 4px 6px !important;
        color: #FFFFFF !important;
        font-family: 'Tajawal', sans-serif !important;
        font-weight: 800 !important;
        font-size: 13px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5) !important;
        transition: all 0.3s ease-in-out !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        white-space: normal !important; /* السماح بالتفاف النص الذكي لكي لا يخرج عن المربع أبدأً */
        word-break: break-word !important;
    }}

    .stButton > button:hover {{
        border-color: #D4AF37 !important;
        background: linear-gradient(135deg, rgba(212, 175, 55, 0.25) 0%, rgba(28, 28, 36, 0.98) 100%) !important;
        box-shadow: 0 6px 18px rgba(212, 175, 55, 0.4) !important;
        transform: translateY(-2px) !important;
    }}

    [data-testid="stSidebar"] {{
        background-color: rgba(12, 12, 16, 0.97) !important;
        backdrop-filter: blur(25px);
        border-left: 2px solid rgba(212, 175, 55, 0.4) !important;
    }}

    .sidebar-card {{
        background: linear-gradient(145deg, rgba(25, 25, 32, 0.85), rgba(15, 15, 20, 0.9));
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 14px;
        padding: 14px;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}

    .sidebar-card-title {{
        font-size: 14px;
        font-weight: 800;
        color: #D4AF37;
        margin-bottom: 8px;
    }}

    .exercise-card, .diet-card, .info-card {{
        background: linear-gradient(145deg, rgba(30, 30, 30, 0.7), rgba(20, 20, 20, 0.8));
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-right: 4px solid #D4AF37;
        border-radius: 16px;
        padding: 18px;
        margin-top: 15px;
        margin-bottom: 12px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    }}

    .exercise-title, .diet-title {{
        font-size: 18px;
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

    .exercise-desc, .diet-desc {{
        font-size: 14px;
        color: #C0C0C0;
        line-height: 1.6;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ==================== لوحة التحكم الذكية PRO (القائمة الجانبية) ====================
with st.sidebar:
    st.markdown("<h2 style='color: #D4AF37; text-align: center; margin-bottom: 0;'>⚙️ لوحة التحكم الذكية PRO</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align:center; color:#A0A0A0;'>الإضافات والأدوات الاحترافية المتقدمة</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("""
    <div class="sidebar-card">
        <div class="sidebar-card-title">🎯 تحديد الهدف الرياضي</div>
    """, unsafe_allow_html=True)
    user_goal = st.radio("اختر هدفك:", ["🔥 حرق الدهون والتنشيف", "💪 بناء الكتلة العضلية (ضخامة)", "⚖️ المحافظة على الوزن والثبات"], index=0, label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="sidebar-card">
        <div class="sidebar-card-title">⏱️ غرفة المؤقتات الرياضية</div>
    """, unsafe_allow_html=True)
    timer_mode = st.selectbox("اختر نوع المؤقت:", ["Tabata (20ث عمل / 10ث راحة)", "EMOM (دقيقة لكل جولة)", "AMRAP (أقصى جولات ممكنة)"], label_visibility="collapsed")
    if st.button("بدء المؤقت المختار 🚀", key="side_timer_pro"):
        with st.empty():
            st.warning(f"⚡ تشغيل: {timer_mode}")
            time.sleep(2)
            st.success("🔥 انطلق بقوة! GO!")
            st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
        <div class="sidebar-card-title">🍽️ حاسبة الماكروز السريعة</div>
    """, unsafe_allow_html=True)
    target_cals = st.number_input("السعرات اليومية:", value=2000, step=100)
    prot = int((target_cals * 0.3) / 4)
    carbs = int((target_cals * 0.45) / 4)
    fats = int((target_cals * 0.25) / 9)
    st.info(f"🥩 بروتين: **{prot}g** | 🍞 كارب: **{carbs}g** | 🥑 دهون: **{fats}g**")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
        <div class="sidebar-card-title">📋 قائمة الانضباط اليومي</div>
    """, unsafe_allow_html=True)
    st.checkbox("تمرين الكروس فيت اليومي 🦾")
    st.checkbox("شرب الاحتياج الكامل من الماء 💧")
    st.checkbox("أخذ كفايتك من النوم (7-8 ساعات) 🛌")
    st.checkbox("الالتزام بالوجبات الصحية المدروسة 🥗")
    st.markdown("</div>", unsafe_allow_html=True)

# ==================== العنوان الرئيسي ====================
st.markdown('<div class="hero-title">CROSSFIT & FITNESS 🇸🇦</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">تطبيقك الشخصي الذكي للياقة البدنية والتغذية</div>', unsafe_allow_html=True)
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# ==================== حالة التنقل بين الأقسام ====================
if "active_page" not in st.session_state:
    st.session_state.active_page = "water"

# ==================== الأزرار الأربعة (موزعة علمياً بمسافات متساوية 100%) ====================
cols = st.columns(4)

with cols[0]:
    if st.button("💧 الماء", key="btn_water"):
        st.session_state.active_page = "water"
        st.rerun()

with cols[1]:
    if st.button("⚡ السعرات", key="btn_calories"):
        st.session_state.active_page = "calories"
        st.rerun()

with cols[2]:
    if st.button("📊 قياس الجسم", key="btn_weight"):
        st.session_state.active_page = "weight"
        st.rerun()

with cols[3]:
    if st.button("🔥 التمارين", key="btn_workouts"):
        st.session_state.active_page = "workouts"
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# ==================== 1. قسم التمارين ====================
if st.session_state.active_page == "workouts":
    st.header("🏃‍♂️ جداول الكروس فيت والتحمل البدني")
    
    crossfit_data = {
        "تمارين حرق وقوة (Bodyweight 🔥)": [
            {
                "title": "تمرين البيربيز الشامل",
                "english_name": "Burpees",
                "sets": "3 جلسات",
                "reps": "12 تكرار",
                "desc": "تمرين كروس فيت متكامل يرفع معدل ضربات القلب ويضاعف حرق السعرات بكفاءة عالية.",
                "url": "https://www.youtube.com/watch?v=dZgVxmf6jkA"
            },
            {
                "title": "تمرين القفز المتوافق",
                "english_name": "Jumping Jacks",
                "sets": "3 جلسات",
                "reps": "45 ثانية",
                "desc": "إحماء ممتاز لتنشيط الدورة الدموية ورفع كفاءة الجهاز التنفسي.",
                "url": "https://www.youtube.com/watch?v=c4DAnQ6DtF8"
            },
            {
                "title": "تمرين تسلق الجبل",
                "english_name": "Mountain Climbers",
                "sets": "3 جلسات",
                "reps": "20 تكرار لكل رجل",
                "desc": "يركز على تقوية عضلات الجذع والبطن ورفع اللياقة الهوائية.",
                "url": "https://www.youtube.com/watch?v=nmwgirgXLYM"
            }
        ],
        "تمارين الجزء السفلي والكتلة (Legs & Core 🦵)": [
            {
                "title": "تمرين السكوات التفجيري",
                "english_name": "Jump Squats",
                "sets": "4 جلسات",
                "reps": "15 تكرار",
                "desc": "يقوي عضلات الفخذين والأرداف ويزيد القوة الانفجارية للقدمين.",
                "url": "https://www.youtube.com/watch?v=72BSZupb-1I"
            },
            {
                "title": "تمرين الطعن الثابت والمتبادل",
                "english_name": "Lunges",
                "sets": "3 جلسات",
                "reps": "12 تكرار لكل رجل",
                "desc": "يحسن التوازن والثبات الحركي ويقوي عضلات الساقين.",
                "url": "https://www.youtube.com/watch?v=QOVaHwm-Q6U"
            }
        ],
        "تمارين الجزء العلوي والتحمل (Upper Body 🦾)": [
            {
                "title": "تمرين الضغط الكلاسيكي",
                "english_name": "Push-ups",
                "sets": "4 جلسات",
                "reps": "15 تكرار",
                "desc": "يبني عضلات الصدر، الأكتاف الأمامية، والترايسبس بقوة.",
                "url": "https://www.youtube.com/watch?v=IODxDxX7oi4"
            },
            {
                "title": "تمرين البلانك للثبات",
                "english_name": "Plank Hold",
                "sets": "3 جلسات",
                "reps": "45 ثانية ثبات",
                "desc": "أقوى تمرين لشد عضلات البطن العميقة وحماية أسفل الظهر.",
                "url": "https://www.youtube.com/watch?v=pSHjTRCQxIw"
            }
        ]
    }

    category = st.selectbox("اختر تصنيف التمارين:", list(crossfit_data.keys()))
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

# ==================== 2. قسم قياس الجسم وحاسبة كتلة الجسم BMI ====================
elif st.session_state.active_page == "weight":
    st.header("📊 حاسبة مؤشر كتلة الجسم (BMI) والوزن المثالي")
    st.write("أدخل بياناتك الحالية لمعرفة مؤشر كتلة الجسم وتقييمه بشكل شخصي:")

    c1, c2 = st.columns(2)
    with c1:
        weight_val = st.number_input("الوزن الحالي (كجم):", min_value=30.0, max_value=250.0, value=75.0, step=0.5)
    with c2:
        height_val = st.number_input("الطول الحالي (سم):", min_value=100.0, max_value=230.0, value=170.0, step=1.0)

    if st.button("حساب وتقييم مؤشر كتلة الجسم 🔍", key="calc_bmi"):
        height_m = height_val / 100.0
        bmi = round(weight_val / (height_m ** 2), 1)
        
        if bmi < 18.5:
            status = "أقل من الوزن الطبيعي (نحافة)"
            advice = "تحتاج لزيادة السعرات الحرارية بشكل صحي والتركيز على تمارين القوة لبناء الكتلة العضلية."
            color_badge = "#3498db"
        elif 18.5 <= bmi <= 24.9:
            status = "وزن طبيعي وصحي ومثالي"
            advice = "ممتاز جداً! حافظ على نمط حياتك المتوازن وممارسة التمارين بانتظام."
            color_badge = "#2ecc71"
        elif 25.0 <= bmi <= 29.9:
            status = "وزن زائد"
            advice = "يُفضل تقليل السعرات الحرارية المستهلكة وزيادة النشاط البدني والمشي اليومي."
            color_badge = "#f1c40f"
        elif 30.0 <= bmi <= 34.9:
            status = "سمنة درجة أولى"
            advice = "من المهم اتباع حمية غذائية منخفضة السعرات والانتظام على الرياضة."
            color_badge = "#e67e22"
        elif 35.0 <= bmi <= 39.9:
            status = "سمنة درجة ثانية"
            advice = "تتطلب حالتك خطة غذائية صارمة ومتابعة مستمرة للوصول لوزن آمن."
            color_badge = "#e74c3c"
        else:
            status = "سمنة مفرطة"
            advice = "يوصى بشدة تنظيم الوجبات والالتزام بالتمارين بجدية للوصول لنتائج أفضل."
            color_badge = "#8e44ad"

        st.markdown(f"""
        <div class="info-card" style="border-right: 5px solid {color_badge};">
            <h3>نتيجة مؤشر كتلة الجسم: <span style="color: {color_badge};">{bmi}</span></h3>
            <p><b>التصنيف:</b> {status}</p>
            <p><b>التوجيه الإرشادي:</b> {advice}</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== 3. قسم السعرات الدقيقة والماكروز ====================
elif st.session_state.active_page == "calories":
    st.header("⚡ حاسبة السعرات الحرارية والاحتياج اليومي")
    st.write("تعتمد هذه الحاسبة على معادلات الأيض الدقيقة لحساب الطاقة بدقة.")

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        c_weight = st.number_input("الوزن (كجم):", min_value=30.0, max_value=250.0, value=75.0)
    with col_b:
        c_height = st.number_input("الطول (سم):", min_value=100.0, max_value=230.0, value=170.0)
    with col_c:
        c_age = st.number_input("العمر (سنة):", min_value=10, max_value=100, value=25)

    c_gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)
    
    activity_level = st.selectbox(
        "مستوى النشاط البدني الأسبوعي:",
        [
            "خامل (بدون تمارينات / عمل مكتبي)",
            "نشاط خفيف (تمارين خفيفة 1-3 أيام أسبوعياً)",
            "نشاط متوسط (تمارين معتدلة 3-5 أيام أسبوعياً)",
            "جهد مرتفع (تمارين شاقة 6-7 أيام أسبوعياً)",
            "جهد مرتفع جداً (تدريب رياضي مكثف يومياً)"
        ]
    )

    if st.button("احسب السعرات والماكروز بدقة 🧮", key="calc_exact_cals"):
        if c_gender == "ذكر":
            bmr = (10 * c_weight) + (6.25 * c_height) - (5 * c_age) + 5
        else:
            bmr = (10 * c_weight) + (6.25 * c_height) - (5 * c_age) - 161

        if "خامل" in activity_level:
            tdee = bmr * 1.2
        elif "خفيف" in activity_level:
            tdee = bmr * 1.375
        elif "متوسط" in activity_level:
            tdee = bmr * 1.55
        elif "جهد مرتفع" in activity_level and "جداً" not in activity_level:
            tdee = bmr * 1.725
        else:
            tdee = bmr * 1.9

        tdee = int(tdee)

        if "حرق" in user_goal:
            target_calories = tdee - 500
            goal_label = "التنشيف وحرق الدهون (عجز 500 سعرة)"
        elif "ضخامة" in user_goal:
            target_calories = tdee + 300
            goal_label = "الضخامة وبناء العضلات (فائض نظيف)"
        else:
            target_calories = tdee
            goal_label = "المحافظة على ثبات الوزن الحالي"

        p_grams = int((target_calories * 0.30) / 4)
        c_grams = int((target_calories * 0.45) / 4)
        f_grams = int((target_calories * 0.25) / 9)

        st.success("✅ تم حساب احتياجك بنجاح في تطبيقك الشخصي!")
        
        st.markdown(f"""
        <div class="info-card">
            <h3>📊 ملخص النتائج لهدفك ({goal_label}):</h3>
            <p><b>معدل الأيض الأساسي (BMR):</b> {int(bmr)} سعرة (طاقة الجسم في الراحة التامة)</p>
            <p><b>إجمالي الاحتياج للثبات (TDEE):</b> {tdee} سعرة حرارية يومياً</p>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <h4 style="color: #D4AF37;">🎯 السعرات المستهدفة للهدف المحدد: <span style="color:#FFF;">{target_calories} سعرة حرارية</span></h4>
            <p><b>🥩 البروتينات المطلوبة:</b> {p_grams} جرام ({int(p_grams*4)} سعرة)</p>
            <p><b>🍞 الكربوهيدرات المطلوبة:</b> {c_grams} جرام ({int(c_grams*4)} سعرة)</p>
            <p><b>🥑 الدهون الصحية المطلوبة:</b> {f_grams} جرام ({int(f_grams*9)} سعرة)</p>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("🍽️ نموذج جدول وجبات غذائية صحية متكاملة")
        
        bf_cals = int(target_calories * 0.25)
        lunch_cals = int(target_calories * 0.35)
        snack_cals = int(target_calories * 0.15)
        dinner_cals = int(target_calories * 0.25)

        meals_plan = [
            ("🍳 وجبة الإفطار المتوازنة", f"حوالي {bf_cals} سعرة", "• 3 بيضات كاملة + شريحة توست أسمر\n• كوب حليب قليل الدسم أو لبن\n• ثمرة فاكهة (تفاح أو موز) + حبات تمر"),
            ("🥩 وجبة الغداء الرياضية", f"حوالي {lunch_cals} سعرة", "• 180 جرام صدر دجاج مشوي أو لحم بقري هزيل\n• 200 جرام أرز بني أو بطاطس مسلوقة بالفرن\n• طبق سلطة خضراء غني بالخضروات الورقية وملعقة زيت زيتون"),
            ("⚡ وجبة ما قبل/بعد التمرين", f"حوالي {snack_cals} سعرة", "• سكوب واي بروتين أو زبادي يوناني قليل الدسم\n• قبضة يد من المكسرات (لوز أو جوز)"),
            ("🥗 وجبة العشاء المشبعة", f"حوالي {dinner_cals} سعرة", "• علبة تونة خفيفة بالماء مصفاة أو جبن قريش / لبنة قليلة الدسم\n• خبز أسمر بر (شريحتين)\n• طبق خس وخيار طازج")
        ]

        for m_title, m_cals_text, m_desc in meals_plan:
            st.markdown(f"""
            <div class="diet-card">
                <div class="diet-title">{m_title} <span style="font-size:13px; color:#D4AF37;">({m_cals_text})</span></div>
                <div class="diet-desc" style="white-space: pre-line;">{m_desc}</div>
            </div>
            """, unsafe_allow_html=True)

# ==================== 4. قسم الماء ====================
elif st.session_state.active_page == "water":
    st.header("💧 متابعة استهلاك الماء اليومي")
    st.write("سجل كميات الماء التي تشربها يومياً لدعم أدائك الرياضي وطاقتك.")

    if "water_cups" not in st.session_state:
        st.session_state.water_cups = 0

    st.subheader(f"إجمالي ما شربته اليوم: {st.session_state.water_cups} كاسات (تقريباً {round(st.session_state.water_cups * 0.25, 2)} لتر)")
    st.progress(min(st.session_state.water_cups / 12.0, 1.0))
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("إضافة كاس ماء (+250 مل) ➕", key="add_w"):
            st.session_state.water_cups += 1
            st.rerun()
    with col2:
        if st.button("تصفير العداد 🔄", key="rst_w"):
            st.session_state.water_cups = 0
            st.rerun()
