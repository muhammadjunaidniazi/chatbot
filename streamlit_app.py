import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="University of Layyah AI Assistant",
    page_icon="🎓",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #071b2f 0%, #0d3158 100%);
        color: white;
    }
    .main-title {
        text-align: center;
        font-size: 44px;
        font-weight: 800;
        color: #ffffff;
        margin-top: 20px;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #e8eef7;
        max-width: 950px;
        margin: 10px auto 35px auto;
        line-height: 1.7;
    }
    .info-card {
        background: rgba(255, 255, 255, 0.12);
        padding: 26px;
        border-radius: 18px;
        min-height: 170px;
        box-shadow: 0 12px 28px rgba(0,0,0,0.18);
        border: 1px solid rgba(255,255,255,0.08);
    }
    .info-card h3 {
        color: white;
        margin-bottom: 12px;
    }
    .info-card p {
        color: #f2f5fa;
        font-size: 16px;
    }
    .chat-panel {
        background: rgba(255, 255, 255, 0.12);
        padding: 24px;
        border-radius: 18px;
        margin-top: 30px;
        border: 1px solid rgba(255,255,255,0.08);
    }
    .small-note {
        color: #d6e3f3;
        text-align: center;
        font-size: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">University of Layyah AI Assistant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">A smart web-based chatbot project designed to help students, applicants, and visitors find information about admissions, programs, campus details, student life, exam guidelines, and university services.</div>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        """
        <div class="info-card">
            <h3>Admissions & Programs</h3>
            <p>BS programs, eligibility criteria, fee structure, and application guidance.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <div class="info-card">
            <h3>Campus Information</h3>
            <p>Departments, faculty information, office locations, and desk support.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        """
        <div class="info-card">
            <h3>Student Life</h3>
            <p>Exam rules, campus updates, guidelines, events, and student support.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="chat-panel">', unsafe_allow_html=True)
st.subheader("💬 Chatbot Module")
st.markdown('<p class="small-note">Type your question below. Example: admission criteria, BS programs, computing faculty, CS department, IT department, fee structure, exams, or campus information.</p>', unsafe_allow_html=True)

SYSTEM_PROMPT = """
You are the University of Layyah AI Assistant. Answer clearly and professionally.
Help users with admissions, BS programs, eligibility, fee structure, campus information,
student life, exam guidelines, departments, faculty, and university services.
If exact official data is not available, tell the user to verify from the University of Layyah official website or admission office.
"""

BASIC_DATA = {
    "admission": "For admissions, please ask about program name, eligibility, fee structure, or application process. Always verify final dates and official notices from the University of Layyah website/admission office.",
    "program": "The assistant can guide users about BS programs, eligibility criteria, and department information. Add the latest official program list in the project dataset for more accurate answers.",
    "fee": "Fee details should be confirmed from the official University of Layyah fee structure or admission office because fee amounts can change.",
    "exam": "For exams, follow university exam guidelines, date sheets, roll number slips, and department instructions. Confirm official notices from the exam branch.",
    "campus": "Campus information includes departments, offices, desk support, faculty information, and student service areas.",
    "contact": "For official support, contact the University of Layyah admission office, department office, or relevant university help desk.",
    "computing": "The Faculty of Computing & Engineering at the University of Layyah includes the Department of Computer Science, Department of Information Technology, and Department of Computer Engineering. It focuses on computing, engineering, emerging technologies, practical learning, and professional skills.",
    "faculty of computing": "The Faculty of Computing & Engineering at the University of Layyah includes three main departments: Department of Computer Science, Department of Information Technology, and Department of Computer Engineering.",
    "computing faculty": "The Faculty of Computing & Engineering at the University of Layyah includes three main departments: Department of Computer Science, Department of Information Technology, and Department of Computer Engineering.",
    "department of computer science": "The Department of Computer Science at the University of Layyah offers computing-focused education such as BS Computer Science and BS Artificial Intelligence. The department covers programming, algorithms, data structures, artificial intelligence, computer networks, cybersecurity, database systems, computer graphics, and human-computer interaction.",
    "computer science": "The Department of Computer Science at the University of Layyah offers computing-focused education such as BS Computer Science and BS Artificial Intelligence. The department covers programming, algorithms, data structures, artificial intelligence, computer networks, cybersecurity, database systems, computer graphics, and human-computer interaction.",
    "cs department": "The Department of Computer Science at the University of Layyah focuses on programming, algorithms, data structures, artificial intelligence, networks, cybersecurity, database systems, and software problem solving.",
    "department of information technology": "The Department of Information Technology at the University of Layyah offers IT-focused education such as BS Information Technology and BS Data Science. The department focuses on applied computing, software and web development, network administration, cybersecurity, IT infrastructure, cloud systems, data science, and data analytics.",
    "information technology": "The Department of Information Technology at the University of Layyah offers IT-focused education such as BS Information Technology and BS Data Science. The department focuses on applied computing, software and web development, network administration, cybersecurity, IT infrastructure, cloud systems, data science, and data analytics.",
    "it department": "The Department of Information Technology at the University of Layyah focuses on applied computing, web development, networking, cybersecurity, IT infrastructure, cloud systems, data science, and data analytics.",
    "department of computer engineering": "The Department of Computer Engineering at the University of Layyah focuses on both hardware and software systems. Key areas include computer hardware and architecture, embedded systems, digital logic design, microprocessors, controllers, software-hardware integration, and engineering problem solving.",
    "computer engineering": "The Department of Computer Engineering at the University of Layyah focuses on computer hardware, software systems, embedded systems, digital logic design, microprocessors, controllers, and hardware-software integration.",
    "bs computer science": "BS Computer Science at the University of Layyah is a computing program focused on programming, data structures, algorithms, databases, software engineering, artificial intelligence, networking, and cybersecurity basics.",
    "bs artificial intelligence": "BS Artificial Intelligence at the University of Layyah focuses on programming, machine learning, artificial intelligence concepts, data handling, problem solving, and intelligent system development.",
    "bs information technology": "BS Information Technology at the University of Layyah focuses on applied computing, web and software development, networks, databases, cybersecurity, IT infrastructure, and cloud-based systems.",
    "bs data science": "BS Data Science at the University of Layyah focuses on data analysis, statistics, programming, databases, machine learning basics, visualization, and data-driven decision making.",
}

KEYWORD_ALIASES = {
    "computing": ["computing", "computing faculty", "faculty of computing", "faculty of computing and engineering", "computer faculty", "fce", "computing engineering"],
    "faculty of computing": ["departments in computing faculty", "which departments are in computing faculty", "computing departments"],
    "department of computer science": ["computer science department", "cs", "cs department", "bscs", "bs cs", "bs computer science"],
    "department of information technology": ["information technology department", "it", "it department", "bsit", "bs it", "bs information technology", "bs data science", "bsds"],
    "department of computer engineering": ["computer engineering department", "ce department", "hardware", "embedded systems", "digital logic", "microprocessor"],
    "bs artificial intelligence": ["bs ai", "artificial intelligence", "ai program"],
}

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Assalam-o-Alaikum! I am the University of Layyah AI Assistant. How can I help you today?",
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

with st.sidebar:
    st.header("Settings")
    openai_api_key = st.text_input("OpenAI API Key (optional)", type="password")
    st.caption("Without an API key, the chatbot will still answer basic university-related questions from built-in demo data.")

user_message = st.chat_input("Type your message here...")

if user_message:
    st.session_state.messages.append({"role": "user", "content": user_message})
    with st.chat_message("user"):
        st.markdown(user_message)

    answer = None
    lower_message = user_message.lower()

    for keyword, reply in BASIC_DATA.items():
        if keyword in lower_message:
            answer = reply
            break

    if not answer:
        for main_keyword, aliases in KEYWORD_ALIASES.items():
            if any(alias in lower_message for alias in aliases):
                answer = BASIC_DATA.get(main_keyword)
                break

    if openai_api_key and not answer:
        try:
            client = OpenAI(api_key=openai_api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages[-10:]
                    ],
                ],
            )
            answer = response.choices[0].message.content
        except Exception as error:
            answer = f"AI response error: {error}. Basic demo mode is still available."

    if not answer:
        answer = (
            "I can help with admissions, programs, eligibility, fees, campus information, computing faculty, departments, exams, and student life. "
            "Please ask a specific question, for example: 'Which departments are in the Faculty of Computing & Engineering?'"
        )

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)

st.markdown("</div>", unsafe_allow_html=True)
