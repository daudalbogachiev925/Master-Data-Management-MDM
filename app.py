import streamlit as st
import pandas as pd
from src.data import generate_duplicates
from src.dedup import find_duplicates
from src.golden_record import build_all_golden_records

st.set_page_config(page_title="MDM", layout="wide")
st.title("🧬 Master Data Management")

@st.cache_data
def load():
    return generate_duplicates(300)

df = load()
threshold = st.slider("Similarity threshold", 0.5, 1.0, 0.85)

groups = find_duplicates(df, threshold)

c1, c2, c3 = st.columns(3)
c1.metric("Всего записей", len(df))
c2.metric("Групп дублей", len(groups))
c3.metric("Записей в дублях", sum(len(g) for g in groups))

st.subheader("🔎 Группы дублей")
for i, g in enumerate(groups[:10]):
    st.markdown(f"**Группа {i+1}** ({len(g)} записей):")
    st.dataframe(df.loc[g])

st.subheader("✨ Golden Records")
golden = build_all_golden_records(df, groups)
if golden:
    st.dataframe(pd.DataFrame(golden))
else:
    st.info("Дублей не найдено")

st.subheader("Исходные данные")
st.dataframe(df.head(30))
