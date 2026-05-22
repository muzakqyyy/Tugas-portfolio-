from django.shortcuts import render

def portfolio_view(request):
    context = {
        # =========================
        # DATA DIRI
        # =========================
        "nama": "Zaky",  # ganti nama kamu
        "ttl": "Pasuruan, 1 Januari 2008",  # ganti tempat & tanggal lahir
        "nisn": "1234567890",  # ganti NISN kamu
        "sekolah": "SMK Negeri 1 Contoh",  # ganti nama sekolah

        # =========================
        # ABOUT ME
        # =========================
        "about_me": (
            "Saya adalah pelajar yang tertarik pada dunia teknologi, "
            "khususnya software development, artificial intelligence, "
            "computer vision, dan desain digital. Saya senang membangun "
            "project modern menggunakan Python, Django, OpenCV, dan tools kreatif."
        ),

        # =========================
        # CONTACT
        # =========================
        "email": "mailto:zaky@example.com",  # ganti email kamu
        "email_text": "zaky@example.com",

        "phone": "https://wa.me/628123456789",  # ganti nomor WA/telepon kamu
        "phone_text": "+62 812-3456-789",

        "instagram": "https://instagram.com/zakydev",  # ganti akun IG kamu
        "instagram_text": "@zakydev",

        # =========================
        # SKILLS
        # =========================
        "skills": [
            "Python",
            "JavaScript",
            "Django",
            "React",
            "Machine Learning",
            "Photoshop",
            "Illustrator",
            "Cisco",
            "HTML",
            "CSS",
        ],

        # =========================
        # CERTIFICATES
        # =========================
        "certificates": [
            "Python Programming",
            "Django Web Development",
            "AI & Machine Learning",
            "Computer Vision",
            "Data Science",
            "Web Development",
        ],
    }

    return render(request, "portfolio_app/portfolio.html", context)