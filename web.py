import streamlit as st

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="ID Guard",
    page_icon="🪪",
    layout="wide"
)

# -------------------------------
# CUSTOM DESIGN
# -------------------------------

st.markdown("""
<style>
    .stApp {
        background-color: #F5F7FB;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #172554;
        margin-bottom: 0;
    }

    .subtitle {
        color: #64748B;
        font-size: 17px;
        margin-top: 4px;
    }

    .panel {
        background-color: white;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        margin-bottom: 16px;
    }

    .status {
        background-color: #FFF7ED;
        color: #9A3412;
        padding: 14px;
        border-radius: 10px;
        font-weight: 600;
    }

    .reminder {
        background-color: #EFF6FF;
        color: #000000;
        padding: 16px;
        border-radius: 10px;
        font-weight: 600;
    }

    .small-text {
        color: #64748B;
        font-size: 13px;
    }
    
    .info {
        color: #5c697d;
    }
    
    /* Make the main text dark */
.stApp,
.stApp p,
.stApp label,
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp li,
.stApp span,
.stApp div {
    color: #1E293B;
}

/* Make input labels readable */
.stApp label {
    color: #1E293B !important;
}

/* Keep secondary text readable */
.small-text {
    color: #475569 !important;
}

#BUTTON STUFF
/* Style the camera's Take Photo button */
[data-testid="stCameraInput"] button {
    background-color: #172554 !important;
    color: #FFFFFF !important;
    border: 5px solid #172554 !important;
}

/* Keep the button text white */
[data-testid="stCameraInput"] button p,
[data-testid="stCameraInput"] button span {
    color: #FFFFFF !important;
}

/* Slightly change the button on hover */
[data-testid="stCameraInput"] button:hover {
    background-color: #0c1152 !important;
    border-color: #0c1152 !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------

st.markdown(
    '<div class="main-title">🪪 ID GUARD</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Smart School ID Detection System'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    '<div class="info">'
    "Welcome to ID Guard! Capture an image to prepare "
    "for an ID card check. AI detection is coming soon."
    '</div>',
    unsafe_allow_html=True
)

# -------------------------------
# MAIN PAGE LAYOUT
# -------------------------------

camera_column, result_column = st.columns(
    [1.25, 1],
    gap="large"
)

with camera_column:

    st.markdown(
        '<div class="main-title">'
        "📸 Camera Scanner"
        '</div>',
        unsafe_allow_html=True
        )

    st.write("Position the student in the camera view.")

    picture = st.camera_input(
        "Capture an image",
        key="id_guard_camera"
    )

    if picture is not None:
            st.markdown(
            '<p class="info">'
            "Image captured successfully!"
            '</p>',
            unsafe_allow_html=True)

    st.markdown(
        '<p class="small-text">'
        'Camera images are not saved by this app.'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

with result_column:

    st.markdown("### 🔍 Detection Results")

    st.markdown(
        '<div class="status">'
        '⏳ AI model not connected'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.write("**ID Status**")
    st.write("Waiting for the AI model")

    st.write("**Lanyard Colour**")
    st.write("Not analysed")

    st.write("**Model Confidence**")
    st.write("Not available")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### 💬 Reminder")

    st.markdown(
        '<div class="reminder">'
        'Your ID reminder will appear here once '
        'AI detection is enabled.'
        '</div>',
        unsafe_allow_html=True
    )

# -------------------------------
# LANYARD INFORMATION
# -------------------------------

st.write("")
st.markdown("### 🎨 School Lanyard Categories")

green_column, maroon_column, beige_column = st.columns(3)

with green_column:
    st.markdown(
        '<div class="panel" style="border-top: 5px solid #16A34A;">'
        '<h4>🟢 Green</h4>'
        '<p>Unaccompanied walkers</p>'
        '</div>',
        unsafe_allow_html=True
    )

with maroon_column:
    st.markdown(
        '<div class="panel" style="border-top: 5px solid #800000;">'
        '<h4>🔴 Maroon</h4>'
        '<p>Bus students</p>'
        '</div>',
        unsafe_allow_html=True
    )

with beige_column:
    st.markdown(
        '<div class="panel" style="border-top: 5px solid #C8B68A;">'
        '<h4>🟤 Beige</h4>'
        '<p>Accompanied students</p>'
        '</div>',
        unsafe_allow_html=True
    )

# -------------------------------
# FOOTER
# -------------------------------

st.divider()

st.caption(
    "ID GUARD | Computer Vision School Project | "
)