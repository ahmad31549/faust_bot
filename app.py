from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    try:
        data = request.json
        incoming = data["payload"]["payload"]["text"].strip().lower()

        if incoming in ['hi', 'hello', 'start', 'university']:
            reply = (
                "🎓 Welcome to FUUAST Info Bot\n"
                "----------------------------------\n"
                "📌 Virtual assistant for admissions, programs, fees & more.\n\n"
                "🧭 *Main Menu*\n"
                "1️⃣ Admission Info\n"
                "2️⃣ Programs Offered\n"
                "3️⃣ Fee Structure\n"
                "4️⃣ LMS (MIS Cell)\n"
                "5️⃣ Scholarships\n"
                "6️⃣ Campus Location\n"
                "7️⃣ Contact Us\n"
                "8️⃣ Live Support\n\n"
                "💡 Reply with a number (1–8) to proceed"
            )
        elif incoming == '1':
            reply = (
                "📝 *Admission Info*\n"
                "----------------------------------\n"
                "🎓 Undergraduate: https://isbadmission.fuuast.edu.pk/ug/login\n"
                "🎓 Postgraduate: https://isbadmission.fuuast.edu.pk/pg/login\n"
                "🎓 Ph.D: https://fuuastisb.edu.pk/admissions\n\n"
                "📁 Documents Required – Type 5\n"
                "🔁 Type start to return to main menu."
            )
        elif incoming == '3':
            reply = "💰 *Fee Details*: https://fuuastisb.edu.pk/FeeDetails.aspx"
        elif incoming == '6':
            reply = "📍 *Campus*: https://maps.app.goo.gl/jSnkP9JR45NEuwyj6"
        elif incoming == '7':
            reply = (
                "🏛️ Contact Info:\n"
                "📞 +92-9252861-64\n"
                "✉️ info@fuuastisb.edu.pk\n"
                "🌐 https://www.fuuastisb.edu.pk"
            )
        else:
            reply = "❌ Invalid input. Type *start* to see the menu."

        return jsonify({"type": "text", "text": reply})

    except Exception as e:
        return jsonify({"type": "text", "text": "⚠️ Error: " + str(e)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
