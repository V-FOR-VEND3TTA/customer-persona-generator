# 📄 Project Overview: Customer Persona Generator

## 🎯 Purpose

The **Customer Persona Generator** is a web-based tool designed to help marketers, entrepreneurs, and business strategists create detailed customer personas. By inputting key characteristics—like demographics, goals, challenges, and interests—users can generate a well-structured PDF report of their ideal customer, ready to use in campaigns, planning sessions, or pitches.

This tool is especially useful for teams focused on **customer acquisition and retention**, enabling better targeting and personalized messaging.

---

## 🛠️ Tech Stack

* **Backend**: Django (Python)
* **Frontend**: Bootstrap 4
* **PDF Generation**: xhtml2pdf
* **Forms**: Django Forms
* **Templating**: Django Templates

---

## 🧩 Key Features

* Clean and intuitive UI for persona creation
* Input fields for:

  * Name
  * Age
  * Gender
  * Occupation
  * Interests
  * Challenges
  * Goals
* Automatically generates a downloadable PDF persona sheet
* Responsive design for desktop and mobile use
* No database required (lightweight and form-based)

---

## 📂 Folder Structure

```bash
customer_persona_generator/
├── manage.py
├── personas/
│   ├── templates/
│   │   └── personas/
│   │       ├── home.html
│   │       └── persona_template.html
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
├── persona_generator/
│   ├── settings.py
│   ├── urls.py
│   └── ...
```

---

## 🚀 Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/customer-persona-generator.git
   cd customer-persona-generator
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**

   ```bash
   python manage.py runserver
   ```

4. **Visit**
   Open `http://127.0.0.1:8000/` in your browser.

---

## 📄 Example Use Case

> A marketing manager wants to better understand their target audience before launching a new email campaign. Using this tool, they create a persona named “Tech-Savvy Tina,” outlining her habits, goals, and pain points. This persona is then shared with the copywriting and design teams to tailor the messaging.

---

## 📌 Future Improvements

* Save personas to a database for future edits
* Add image upload for persona avatars
* Offer downloadable persona templates in .docx and JSON
* Multi-language support

---

## 👥 Ideal Users

* Marketing Teams
* Product Managers
* UX Designers
* Business Consultants
* Founders & Startups

---

## 🧠 Why This Matters

Building accurate customer personas is foundational to effective marketing. This tool simplifies that process, helping businesses get clarity on **who they're speaking to** — and how best to reach them.
