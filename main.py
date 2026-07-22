import streamlit as st
import pandas as pd
import time

# إعدادات الصفحة
st.set_page_config(page_title="تطبيق MB للتمارين", page_icon="⚡", layout="centered")

st.title("⚡ MB CROSSFIT & FITNESS")
st.write("تمارين لياقة وحرق للجسم كامل (CrossFit) + متابعة يومية")

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
    
    # تمارين كروس فيت بوزن الجسم مع صور متحركة حقيقية (GIFs)
    crossfit_data = {
        "تمارين حرق وقوة (Bodyweight 🔥)": [
            {
                "name": "1. بيربيز (Burpees) - 3 جلسات × 12 تكرار",
                "desc": "تمرين كروس فيت شامل يحرك كامل عضلات الجسم ويرفع اللياقة فوراً.",
                "gif": "https://media.giphy.com/media/3o7TKMt1VVNkHV2PaE/giphy.gif"
            },
            {
                "name": "2. نط الحبل الوهمي / العادي (Jumping Jacks) - 3 جلسات × 45 ثانية",
                "desc": "ممتاز لرفع ضغط الدم وضخ الأكسجين للجسم كامل.",
                "gif": "https://media.giphy.com/media/l2JnkWa6KlsfqX8q4/giphy.gif"
            },
            {
                "name": "3. تسلق الجبل (Mountain Climbers) - 3 جلسات × 20 تكرار لكل رجل",
                "desc": "يقوي عضلات البطن، الأكتاف، والأرجل بسرعة عالية.",
                "gif": "https://media.giphy.com/media/l41YkFIhIYvyYdI64/giphy.gif"
            }
        ],
        "تمارين الجزء السفلي والكتلة (Legs & Core 🦵)": [
            {
                "name": "1. سكوات قفز (Jump Squats) - 4 جلسات × 15 تكرار",
                "desc": "تمرين تفجيري للأرجل والأسفل لزيادة اللياقة والقوة.",
                "gif": "https://media.giphy.com/media/3o7TKxOzA3f84E1c76/giphy.gif"
            },
            {
                "name": "2. الطعن المتحرك (Lunges) - 3 جلسات × 12 تكرار لكل رجل",
                "desc": "لتقوية عضلات الفخذ والاتزان.",
                "gif": "https://media.giphy.com/media/l41YvxI1u2x1fU436/giphy.gif"
            }
        ],
        "تمارين الجزء العلوي والتحمل (Upper Body 🦾)": [
            {
                "name": "1. بوش أب كلاسيكي (Push-ups) - 4 جلسات × 15 تكرار",
                "desc": "الأساسي للصدر، الأكتاف، والترايسبس.",
                "gif": "https://media.giphy.com/media/3o7TKRnoS9oI1RmsaA/giphy.gif"
            },
            {
                "name": "2. بلانك مع لمس الأكتاف (Plank Shoulder Taps) - 3 جلسات × 30 ثانية",
                "desc": "تمرين ثبات قوي جداً للبطن والجذع كامل.",
                "gif": "https://media.giphy.com/media/xT1R3x2874fI12iS2I/giphy.gif"
            }
        ]
    }

    category = st.selectbox("اختر نوع الجلسة:", list(crossfit_data.keys()))
    st.markdown("---")
    
    for ex in crossfit_data[category]:
        st.subheader(ex["name"])
        st.caption(ex["desc"])
        # عرض الصور المتحركة بصيغة HTML لضمان عمل الـ GIF بدون مشاكل
        st.markdown(f'<img src="{ex["gif"]}" width="100%" style="border-radius:10px;">', unsafe_allow_html=True)
        st.markdown("---")

    # مؤقت راحة الجولات (WOD Rest Timer)
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
        st.success("تم حفظ الوزن بنجاح!")

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

        # للكروس فيت يتم ضرب المعامل في نشاط عالي (1.6)
        tdee = int(bmr * 1.6)

        st.metric("احتياجك اليومي مع تمارين الكروس فيت", f"{tdee} سعرة")
        st.write(f"📉 للتنشيف والنزول السريع: **{tdee - 400}** سعرة")

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
