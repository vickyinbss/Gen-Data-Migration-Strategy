def get_styles():
    return """
    <style>
    body, .main, .stApp {
        background: linear-gradient(135deg, #e3f2fd 0%, #fce4ec 100%);
    }
    .reportview-container .main .block-container{padding-top:2rem;}
    .stTitle, .stSubheader {
        color: #1a237e;
        font-family: 'Segoe UI', sans-serif;
    }
    .step-box {
        background: linear-gradient(90deg, #bbdefb 0%, #f8bbd0 100%);
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 8px;
        font-size: 16px;
        color: #263238;
        box-shadow: 0 2px 8px rgba(33,150,243,0.08);
        animation: fadeInUp 0.8s;
    }
    .result-box {
        background: #fffde7;
        border-left: 6px solid #fbc02d;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 12px;
        font-size: 17px;
        color: #6d4c41;
        box-shadow: 0 2px 8px rgba(251,192,45,0.08);
        animation: fadeIn 1s;
    }
    .stButton>button {
        background: linear-gradient(90deg, #42a5f5 0%, #f06292 100%);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 0.5em 2em;
        font-size: 18px;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 16px rgba(66,165,245,0.2);
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px);}
        to { opacity: 1; transform: translateY(0);}
    }
    </style>
    """