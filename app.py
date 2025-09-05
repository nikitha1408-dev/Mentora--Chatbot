import gradio as gr

# 🔧 MentorBot core logic with full answers
def mentor_bot(message):
    message = message.lower().strip()

    if "prepare for placements" in message:
        return (
            "📚 **Placement Preparation Tips:**\n"
            "- Practice DSA on platforms like LeetCode & GFG.\n"
            "- Work on aptitude, puzzles, and verbal ability.\n"
            "- Build 1–2 solid projects to show.\n"
            "- Learn soft skills: communication & resume writing.\n"
            "- Do mock interviews!"
        )

    elif "best ai course" in message or "ai course" in message:
        return (
            "🎓 **Top AI Courses:**\n"
            "- Andrew Ng’s Machine Learning (Coursera)\n"
            "- NPTEL AI by IITs\n"
            "- Fast.ai's Practical Deep Learning\n"
            "- Google’s AI for Everyone"
        )

    elif "1st year skills" in message or "first year" in message:
        return (
            "🧠 **Skills to Learn in 1st Year BTech:**\n"
            "- Python basics & problem solving\n"
            "- Git & GitHub\n"
            "- Communication & time management\n"
            "- Start exploring Web Dev or ML based on your interest"
        )

    elif "ai or cybersecurity" in message:
        return (
            "🤖 **AI vs Cybersecurity:**\n"
            "- **AI**: Research-heavy, involves ML, Data Science, Automation\n"
            "- **Cybersecurity**: Defending systems, ethical hacking, networks\n"
            "- 🔎 Choose AI if you like data & math; Cybersecurity if you're into system protection & security analysis"
        )

    elif "data science career" in message:
        return (
            "📊 **Data Science Career:**\n"
            "- High demand field in tech, finance, health, etc.\n"
            "- Learn: Python, Pandas, NumPy, ML, Statistics\n"
            "- Tools: Jupyter, Matplotlib, Scikit-learn\n"
            "- Tip: Do Kaggle projects and real-world datasets!"
        )

    elif "linkedin" in message:
        return (
            "🔗 **LinkedIn Tips:**\n"
            "- Use a clear profile photo\n"
            "- Write a strong headline (e.g. 'CS Student | Python | Web Dev')\n"
            "- Add projects, internships & skills\n"
            "- Connect with seniors, alumni & HRs\n"
            "- Post your wins (certificates, projects, blogs) weekly"
        )

    elif "open source" in message:
        return (
            "🌍 **What is Open Source?**\n"
            "Open source means the code is public, free to use, modify, and contribute to.\n"
            "- Example: Python, Linux, VLC Media Player\n"
            "- You can view, clone, and contribute on platforms like GitHub.\n"
            "- Start with issues labeled ‘good first issue’!"
        )

    elif "internship" in message:
        return (
            "💼 **Getting Internships:**\n"
            "- Build projects and put them on GitHub\n"
            "- Create a resume (PDF) and LinkedIn profile\n"
            "- Apply on Internshala, LinkedIn, Google Careers\n"
            "- Don’t hesitate to cold-message startups!"
        )

    elif "gate exam" in message:
        return (
            "📘 **About GATE:**\n"
            "- Graduate Aptitude Test in Engineering\n"
            "- Required for M.Tech/IIT admissions or PSU jobs\n"
            "- Covers core subjects from your branch\n"
            "- Preparation time: 6–12 months"
        )

    elif "resume" in message:
        return (
            "📄 **Resume Building Tips:**\n"
            "- Use a clean format (Zety, Overleaf)\n"
            "- Keep it 1 page\n"
            "- Add: Skills, Projects, Education, Internships\n"
            "- Avoid: Paragraphs, spelling mistakes"
        )

    elif "best programming language" in message:
        return (
            "👨‍💻 **Best Programming Languages:**\n"
            "- Python: Easy + versatile (AI, Data, Web)\n"
            "- JavaScript: Web dev\n"
            "- C/C++: Competitive programming & systems\n"
            "- Java: Interviews & Android dev"
        )

    elif "frontend" in message or "backend" in message:
        return (
            "🖥️ **Frontend vs Backend:**\n"
            "- **Frontend**: What user sees (HTML, CSS, JavaScript, React)\n"
            "- **Backend**: Logic, database (Python, Node.js, SQL)\n"
            "- Learn both = Full Stack Dev"
        )

    elif "youtube" in message:
        return (
            "🎥 **Best YouTube Channels:**\n"
            "- CodeWithHarry (Web Dev)\n"
            "- Apna College (DSA, interviews)\n"
            "- Gate Smashers (Theory subjects)\n"
            "- Jenny’s Lectures (OS, DBMS)"
        )

    elif "web dev roadmap" in message:
        return (
            "🌐 **Web Dev Roadmap:**\n"
            "1. HTML → CSS → JavaScript\n"
            "2. Frameworks: React / Angular\n"
            "3. Backend: Node.js / Django\n"
            "4. Database: MongoDB / MySQL\n"
            "5. Hosting: Vercel, Netlify"
        )

    elif "coding platforms" in message:
        return (
            "💻 **Top Coding Platforms:**\n"
            "- LeetCode: Interviews\n"
            "- GeeksforGeeks: DSA + theory\n"
            "- HackerRank: Practice by topic\n"
            "- Codeforces: Competitive Programming\n"
            "- AtCoder: Tougher contests"
        )

    else:
        return "🙋‍♀️ I don’t have that yet, but I’ll learn it soon! Try a different question related to careers, tech, or college 😊"

# ✅ Suggested clickable questions
suggestions = [
    "How to prepare for placements?",
    "Best AI courses?",
    "What skills should a 1st year BTech student learn?",
    "Scope of AI vs Cybersecurity?",
    "Is data science a good career?",
    "What is open source?",
    "Tips for LinkedIn?",
    "How to get internships?",
    "What is the GATE exam?",
    "How to build resume?",
    "Frontend or Backend?",
    "Best programming language?",
    "Best YouTube channels?",
    "Web dev roadmap?",
    "Best coding platforms?"
]

# ✅ Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 👩‍🏫 Mentora – Career Chat Assistant")
    gr.Markdown("Ask me anything about careers, placements, skills, or college life. Click a question or type your own:")

    chatbot = gr.Chatbot()
    txt = gr.Textbox(show_label=False, placeholder="Type your question here...")
    clear = gr.Button("Clear Chat")

    def reply(message, history):
        response = mentor_bot(message)
        history.append((message, response))
        return "", history

    txt.submit(reply, [txt, chatbot], [txt, chatbot])
    clear.click(lambda: [], None, chatbot)

    with gr.Row():
        for q in suggestions:
            gr.Button(q).click(fn=reply, inputs=[gr.Textbox(value=q, visible=False), chatbot], outputs=[txt, chatbot])

demo.launch()
