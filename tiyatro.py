import streamlit as st
import pandas as pd

def main():
    st.title("Zaman Çizelgesi ve Görevler")
    
    # Zaman Çizelgesi Verisi
    schedule_data = {
        "Olay": [
            "Temaların Belirlenmesi", "Metinlerin okunup seçimlerin tamamlanması", "Metin havuzu oluşturulması", 
            "Mesh-up yapılması (first draft)", "Mesh-up yapılması (first draft-review)", "Mesh-up yapılması (first draft-ekiple okuma)",
            "Mesh-up yapılması (first draft-metnin genel hatlarının belli olması)", "Mesh-up yapılması (first draft-geri dönüt toplantısı)",
            "Mesh-up yapılması (second draft)", "Mesh-up yapılması (second draft-review)", "Mesh-up yapılması (second draft-ekiple okuma)",
            "Mesh-up yapılması (second draft)(kayıt metni)", "Mesh-up yapılması (second draft)(son metin)", "eğitim çalışmaları",
            "eğitim çalışmaları", "eğitim çalışmaları", "pasaj çalışması (ezber)"
        ],
        "Tarih": [
            "22.03.2025", "31.03.2025", "04.04.2025", "06.04.2025", "08.04.2025", "12.04.2025", "16.04.2025", "19.04.2025",
            "03.05.2025", "06.05.2025", "14.05.2025", "17.05.2025", "24.05.2025", "17.03.2025", "24.03.2025", "28.03.2025", "16.03.2025"
        ]
    }
    
    schedule_df = pd.DataFrame(schedule_data)
    st.subheader("Zaman Çizelgesi")
    st.dataframe(schedule_df)
    
    # Görevler Verisi
    task_data = {
        "Grup": ["Sanem, Eda", "Öykü, Gökçe", "Öykü, Gökçe", "Erol, Öykü", "Erol"],
        "Görev": ["Godot", "Oyun Sonu", "Mutlu Günler", "Molloy", "Malone Ölüyor"]
    }
    
    task_df = pd.DataFrame(task_data)
    
    st.subheader("Görevler")
    st.dataframe(task_df)
    
    # Kullanıcıya göre görev belirleme
    selected_person = st.selectbox("Kişi seçin", sorted(set(sum([g.split(", ") for g in task_df["Grup"]], []))))
    
    filtered_tasks = task_df[task_df["Grup"].str.contains(selected_person, na=False)]
    
    st.subheader(f"{selected_person} için görevler")
    st.write(filtered_tasks if not filtered_tasks.empty else "Bu kişi için görev bulunamadı.")
    
    # Notlar Bölümü
    st.subheader("Notlar")
    notes_data = {
        "Genel Notlar": [
            "Dekor-Plastik: Teknoloji-uygulama denemeleri & son ürün -> hareket tasarımı",
            "Kayıt: Kayıt Provasısı (sahne üzeri ve teknik) & kaydın kendisi (çekim & kurgu)",
            "Sahne üzeri: Prova(genel oyun provası ve hareket tasarımı provası) & makyaj & kostüm",
            "Sahne Çalışması: haftada 1-2/5-6 hafta",
            "Durum doğaçları: 5/6 hafta",
            "kostüm-aksesuar denemesi: son 1-2 hafta",
            "Kasım ilk haftası PRÖMİYER!!!!"
        ]
    }
    notes_df = pd.DataFrame(notes_data)
    st.dataframe(notes_df)

if __name__ == "__main__":
    main()
