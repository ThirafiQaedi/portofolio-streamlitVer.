import streamlit as st
from pathlib import Path

# ---------------------------------------------------------
# 1. KONFIGURASI HALAMAN & STYLE
# ---------------------------------------------------------
st.set_page_config(
    page_title="Portofolio | Muhamad Thirafi Qaedi Setiawan",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Path foto profil (simpan gambar dari CV ke assets/profile_photo.png)
PHOTO_PATH = Path("Asset/profile_photo.png")

# ---------------------------------------------------------
# 2. SIDEBAR - NAVIGASI & PROFIL SINGKAT
# ---------------------------------------------------------
with st.sidebar:
    if PHOTO_PATH.exists():
        st.image(str(PHOTO_PATH), width=150)
    else:
        st.image("https://via.placeholder.com/150?text=MTQS", width=150)
        st.caption("⚠️ foto profil tidak ditemukan")

    st.title("Muhamad Thirafi Qaedi Setiawan")
    st.caption("Fresh Graduate Informatics Engineering | AI, Data & Software Enthusiast")

    st.markdown("---")

    menu = st.radio(
        "Navigasi",
        [
            "Tentang Saya",
            "Pengalaman & Pendidikan",
            "Sertifikasi",
            "Keahlian & Bahasa",
            "Kontak"
        ]
    )

    st.markdown("---")
    st.markdown("📍 **Lokasi:** Jakarta, Indonesia")
    st.markdown("📞 **Telepon:** 08121802867")
    st.markdown("✉️ **Email:** m.thirafi.setiawan@gmail.com")
    st.markdown("[🔗 LinkedIn](https://linkedin.com)")  

# ---------------------------------------------------------
# 3. HALAMAN: TENTANG SAYA
# ---------------------------------------------------------
if menu == "Tentang Saya":
    st.title("👋 Halo, Saya Muhamad Thirafi Qaedi Setiawan")
    st.subheader("Informatics Engineering Graduate • AI, Machine Learning & Data Analysis")

    st.write(
        """
        Saya adalah *fresh graduate* Teknik Informatika dari **Universitas Muhammadiyah Jakarta (UMJ)**
        dengan keahlian di bidang Teknologi Informasi, *Machine Learning*, dan Analisis Data. Berpengalaman
        dalam membangun model prediktif, memproses data terstruktur maupun visual, serta menerapkan pendekatan
        berbasis data untuk menyelesaikan masalah di dunia nyata.
        """
    )

    st.write(
        """
        Selain memiliki dasar di pengembangan web, *Machine Learning*, dan pengembangan aplikasi *mobile*,
        keterlibatan saya dalam organisasi sebagai anggota dan sekretaris memperkuat kemampuan koordinasi,
        dokumentasi, dan kerja sama tim secara analitis, sistematis, dan kolaboratif.
        """
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Pendidikan", value="S1 Teknik Informatika")
    with col2:
        st.metric(label="Program / Cohort", value="3 Cohort / MSIB")
    with col3:
        st.metric(label="Sertifikasi", value="3 Sertifikat")
    with col4:
        st.metric(label="Bahasa Inggris", value="Upper-Intermediate")

# ---------------------------------------------------------
# 4. HALAMAN: PENGALAMAN & PENDIDIKAN
# ---------------------------------------------------------
elif menu == "Pengalaman & Pendidikan":
    st.title("💼 Pengalaman & Pendidikan")

    tab1, tab2 = st.tabs(["Pengalaman Program & Organisasi", "Pendidikan"])

    with tab1:
        st.subheader("AI Engineer — Laskar AI Cohort")
        st.caption("Laskar AI | 02/2025 - 07/2025")
        st.markdown(
            """
            - **Python Programming:** Membangun solusi cerdas berbasis AI.
            - **Machine Learning & Deep Learning:** Menerapkan konsep inti hingga aplikasi dunia nyata.
            - **Data Science & Visualization:** Menerapkan praktik data science dan visualisasi ke kebutuhan industri.
            """
        )

        st.markdown("---")

        st.subheader("RevoU Tech Academy: Data Analytics & Software Engineering with AI (KM MSIB)")
        st.caption("RevoU & Kampus Merdeka | 02/2024 - 06/2024")
        st.write(
            """
            Mempelajari *Data Processing* pada *Data Analytics*, *Data Visualisation and Communication with AI Tools*,
            *Intro to Web Development*, *Front-End Development with AI Tools*, serta *Career Development with AI Tools*.
            """
        )

        st.markdown("---")

        st.subheader("Organization Field Secretary")
        st.caption("Ikatan Mahasiswa Muhammadiyah | 12/2023 - 12/2024")
        st.markdown(
            """
            - Mengelola administrasi dan korespondensi seluruh program kerja di bidang keorganisasian serta memastikan kepatuhan terhadap pedoman penyusunan dokumen resmi.
            - Mengelola dokumentasi dan laporan rapat evaluasi organisasi.
            - Menjaga komunikasi dan koordinasi dengan Komisariat setempat lainnya.
            """
        )

        st.markdown("---")

        st.subheader("Mobile Development Cohort — Bangkit Academy 2023 Batch 2 (SIB)")
        st.caption("Bangkit Academy (Google, Tokopedia, Gojek, & Traveloka) | 08/2023 - 01/2024")
        st.markdown(
            """
            - Mempelajari dasar *Android UI Design*.
            - Mempelajari fundamental pengembangan aplikasi Android menggunakan **Kotlin**.
            """
        )

        st.markdown("---")

        st.subheader("Communication and Information Department Staff")
        st.caption("HMIF BEM FT-UMJ | 04/2023 - 12/2023")
        st.write(
            """
            Berkolaborasi dengan anggota lain untuk membuat konten media sosial dan mengelola/memelihara situs web Himpunan Mahasiswa.
            """
        )

    with tab2:
        st.subheader("Sarjana Teknik Informatika (Informatics Engineering)")
        st.caption("Universitas Muhammadiyah Jakarta | 09/2021 - 02/2026")
        st.write(
            "Menyelesaikan studi Sarjana Teknik Informatika di Universitas Muhammadiyah Jakarta."
        )

# ---------------------------------------------------------
# 5. HALAMAN: SERTIFIKASI
# ---------------------------------------------------------
elif menu == "Sertifikasi":
    st.title("🏅 Sertifikasi")

    st.subheader("Laskar AI Certificate of Completion")
    st.caption("Laskar AI | 08/2025 - Sekarang")
    st.write("Sertifikat kelulusan program Laskar AI Cohort.")

    st.markdown("---")

    st.subheader("Certificate of Achievements — RevoU Tech Academy Data Analytics & Software Engineering with AI")
    st.caption("MSIB Kampus Merdeka & RevoU | 06/2024 - Sekarang")
    st.write(
        "Penghargaan atas penyelesaian RevoU Tech Academy (Learn Data Analytics & Software Development With AI) "
        "sebagai bagian dari Studi Independen Bersertifikat (SIB) yang didukung Kampus Merdeka."
    )

    st.markdown("---")

    st.subheader("Bangkit Academy Mobile Development 2023 Batch 2 (SIB) Completion Certificate")
    st.caption("Bangkit (Google, GoTo, dan Traveloka) | 01/2024 - Sekarang")
    st.write("Sertifikat kelulusan jalur Mobile Development pada program Bangkit Academy 2023 Batch 2.")

# ---------------------------------------------------------
# 6. HALAMAN: KEAHLIAN & BAHASA
# ---------------------------------------------------------
elif menu == "Keahlian & Bahasa":
    st.title("🛠️ Keahlian Teknis, Soft Skill & Bahasa")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Technical Skills")
        skills_data = [
            ("Python", "Intermediate"),
            ("SQL", "Intermediate"),
            ("Microsoft Excel", "Intermediate"),
            ("Microsoft Word", "Intermediate"),
            ("HTML & CSS", "Intermediate"),
            ("JavaScript", "Intermediate"),
            ("Power BI", "Basic"),
            ("PHP", "Basic"),
            ("Kotlin", "Basic"),
            ("Flutter", "Basic"),
        ]
        for skill, level in skills_data:
            st.markdown(f"- **{skill}:** `{level}`")

    with col2:
        st.subheader("Soft Skills")
        st.markdown("- **Teamwork Skills:** `Intermediate`")

        st.markdown("---")

        st.subheader("Languages")
        st.markdown("- **Indonesia:** `Native`")
        st.markdown("- **English:** `Upper-intermediate`")

# ---------------------------------------------------------
# 7. HALAMAN: KONTAK
# ---------------------------------------------------------
elif menu == "Kontak":
    st.title("📬 Hubungi Saya")
    st.markdown(
        """
        - **Email:** m.thirafi.setiawan@gmail.com
        - **Telepon:** 08121802867
        - **Lokasi:** Jakarta, Indonesia
        """
    )

    st.markdown("---")

    with st.form("contact_form"):
        name = st.text_input("Nama Lengkap")
        email = st.text_input("Email Anda")
        message = st.text_area("Pesan")

        submitted = st.form_submit_button("Kirim Pesan")
        if submitted:
            if name and email and message:
                st.success(f"Terima kasih, {name}! Pesan Anda telah dicatat.")
            else:
                st.warning("Harap lengkapi nama, email, dan pesan terlebih dahulu.")