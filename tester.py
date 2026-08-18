import yfinance
import pandas as pd
import streamlit as st
st.set_page_config(page_title="VN30 Stock Data", page_icon=":chart_with_upwards_trend:", layout="wide")
st.title("VN30 Stock Data Viewer")

VN30_list = ["ACB.VN", "BCM.VN", "BID.VN", "BVH.VN", "CTG.VN", 
    "FPT.VN", "GAS.VN", "GVR.VN", "HDB.VN", "HPG.VN", 
    "MBB.VN", "MSN.VN", "MWG.VN", "PLX.VN", "POW.VN", 
    "SAB.VN", "SHB.VN", "SSB.VN", "SSI.VN", "STB.VN", 
    "TCB.VN", "TPB.VN", "VCB.VN", "VHM.VN", "VIB.VN", 
    "VIC.VN", "VJC.VN", "VNM.VN", "VPB.VN", "VRE.VN"]

cot_trai,cot_phai = st.columns([1,3])
with cot_trai:
    ma_duoc_chon = st.selectbox("📌Chọn mã cổ phiếu", VN30_list)
    if ma_duoc_chon:
        with st.spinner("Đang tải dữ liệu..."):
            du_lieu = yfinance.Ticker(ma_duoc_chon).history(period="1mo")
            thong_tin_co_phieu = yfinance.Ticker(ma_duoc_chon).info
            du_lieu = du_lieu.dropna(subset=['Close'])
if len(du_lieu) > 0:
    ten_day_du = thong_tin_co_phieu.get("longName")
    gia_mo_cua = du_lieu["Open"].iloc[-1]
    gia_dong_cua = du_lieu["Close"].iloc[-1]
    volume = du_lieu["Volume"].iloc[-1]
    gia_cao_nhat = du_lieu["High"].iloc[-1]
    gia_thap_nhat = du_lieu["Low"].iloc[-1]
    phan_tram = ((gia_dong_cua - gia_mo_cua) / gia_mo_cua) * 100
    if phan_tram > 0:
        mau_sac = "#00FF00"
    elif phan_tram < 0:
        mau_sac = "#FF0000"
    else:
        mau_sac = "#F2E3E3"
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"Tên đầy đủ: **{ten_day_du}**")
    st.markdown(f"Giá mở cửa: **{gia_mo_cua:,.0f}**")
    st.markdown(f"Giá đóng cửa: **{gia_dong_cua:,.0f}**")
    st.markdown(f"Khối lượng: **{volume:,}**")
    st.markdown(f"Giá cao nhất: **{gia_cao_nhat:,.0f}**")
    st.markdown(f"Giá thấp nhất: **{gia_thap_nhat:,.0f}**")
    st.markdown(f"Phần trăm thay đổi: **<span style='color:{mau_sac}'>{abs(phan_tram):.2f}%</span>**", unsafe_allow_html=True)
with cot_phai:
    if ma_duoc_chon and len(du_lieu) > 0:
        st.markdown(f"### Biểu đồ giá {ma_duoc_chon.replace('.VN', '')} (1 Tháng)")
        st.line_chart(du_lieu["Close"])