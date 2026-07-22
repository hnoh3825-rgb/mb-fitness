import streamlit as st
import pandas as pd
import time

# إعدادات الصفحة
st.set_page_config(page_title="تطبيق MB للتمارين", page_icon="⚡", layout="centered")

# ==================== خلفية مظلمة جداً (Dark Aesthetics - Abs/Six Pack) ====================
bg_img_url = "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=1200&auto=format&fit=crop"

st.markdown(
    f"""
    <style>
    /* خلفية التطبيق بالكامل مع صورة السيكس باك المظلمة */
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.85)), url("{bg_img_url}") no-repeat center center fixed;
        background-size: cover !important;
    }}
    
    /* حاوية المحتوى شاشتها متناسقة وشفافة لإبراز الخلفية المظلمة */
    .main .block-container {{
        background-color: rgba(10, 10, 10, 0.80) !important;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 25px;
        margin-top: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.9);
        color: white;
    }}

    /* هيدر عريض وفخم لعبارة NO EXCUSES */
    .no-excuses-banner {{
        text-align: center;
        font-family: 'Impact', 'Arial Black', sans-serif;
        font-size: 42px;
        letter-spacing: 8px;
        color: #ffffff;
        text-shadow: 0px 0px 15px rgba(255, 255, 255, 0.3), 3px 3px 10px rgba(0,0,0,0.9);
        border-bottom: 2px solid rgba(255, 255, 255, 0.3);
        padding-bottom: 10px;
        margin-bottom: 25px;
    }}

    /* تحسين ألوان التبويبات لتناسب المود الداكن */
    .stTabs [data-baseweb="tab-list"] button {{
        color: #e0e0e0 !important;
        font-weight: bold;
        font-size: 16px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# عرض العبارة التحفيزية الفخمة
st.markdown('<div class="no-excuses-banner">NO EXCUSES ⚡</div>', unsafe_allow_html=True)

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
        "تمارين حرق وقوة (Bodyweight 🔥)":
