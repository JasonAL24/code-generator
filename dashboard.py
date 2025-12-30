import streamlit as st
import random
import csv
import string
import io
import zipfile
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="Code & PDF Generator", page_icon="📄", layout="wide")

st.title("📄 Code & PDF Generator Dashboard")
st.markdown("---")

# Sidebar for selection
option = st.sidebar.selectbox(
    "Choose Generator Type:",
    ["CSV Codes", "Dummy PDFs"]
)

# Helper functions
def generate_custom_code(format_string):
    """Generate a code based on custom format string"""
    result = format_string
    
    # Replace {d:X} with X random digits
    import re
    for match in re.finditer(r'\{d:(\d+)\}', format_string):
        count = int(match.group(1))
        random_digits = ''.join(random.choices(string.digits, k=count))
        result = result.replace(match.group(0), random_digits, 1)
    
    # Replace {u:X} with X random uppercase letters
    for match in re.finditer(r'\{u:(\d+)\}', format_string):
        count = int(match.group(1))
        random_letters = ''.join(random.choices(string.ascii_uppercase, k=count))
        result = result.replace(match.group(0), random_letters, 1)
    
    # Replace {l:X} with X random lowercase letters
    for match in re.finditer(r'\{l:(\d+)\}', format_string):
        count = int(match.group(1))
        random_letters = ''.join(random.choices(string.ascii_lowercase, k=count))
        result = result.replace(match.group(0), random_letters, 1)
    
    return result

def generate_custom_codes(count, format_string):
    """Generate multiple codes with custom format"""
    codes = set()
    while len(codes) < count:
        codes.add(generate_custom_code(format_string))
    return list(codes)

if option == "CSV Codes":
    st.header("🔢 CSV Code Generator")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        num_codes = st.number_input("How many codes to generate?", min_value=1, max_value=1000000, value=10, step=1)
        
        st.subheader("Custom Format (Optional)")
        use_custom = st.checkbox("Use custom format")
        
        if use_custom:
            st.info("Use {d} for digits, {u} for uppercase letters, {l} for lowercase letters")
            custom_format = st.text_input("Custom format:", value="TVLK{d:5}{u:3}", 
                                         help="Example: TVLK{d:5}{u:3} = TVLK12345ABC")
        else:
            custom_format = None
    
    with col2:
        st.markdown("### Preview")
        if use_custom and custom_format:
            try:
                preview_code = generate_custom_code(custom_format)
                st.code(preview_code)
            except:
                st.error("Invalid format")
        else:
            st.code(f"TVLK{random.randint(10000, 99999)}{''.join(random.choices(string.ascii_uppercase, k=3))}")
    
    if st.button("🎲 Generate CSV Codes", type="primary"):
        with st.spinner("Generating codes..."):
            if use_custom and custom_format:
                codes = generate_custom_codes(num_codes, custom_format)
            else:
                codes = [f"TVLK{random.randint(10000, 99999)}{''.join(random.choices(string.ascii_uppercase, k=3))}" 
                        for _ in range(num_codes)]
            
            # Check for duplicates
            unique_codes = len(set(codes))
            if unique_codes < num_codes:
                st.warning(f"⚠️ {num_codes - unique_codes} duplicate(s) found. Regenerating unique codes...")
                codes = set()
                while len(codes) < num_codes:
                    if use_custom and custom_format:
                        code = generate_custom_code(custom_format)
                    else:
                        code = f"TVLK{random.randint(10000, 99999)}{''.join(random.choices(string.ascii_uppercase, k=3))}"
                    codes.add(code)
                codes = list(codes)
            
            # Create CSV in memory
            csv_buffer = io.StringIO()
            writer = csv.writer(csv_buffer)
            for code in codes:
                writer.writerow([code])
            
            st.success(f"✅ Generated {num_codes} unique codes!")
            
            # Display preview
            st.subheader("Preview (first 10 codes)")
            st.dataframe(codes[:10], use_container_width=True)
            
            # Download button
            st.download_button(
                label="📥 Download CSV",
                data=csv_buffer.getvalue(),
                file_name="generated_codes.csv",
                mime="text/csv"
            )

elif option == "Dummy PDFs":
    st.header("📄 Dummy PDF Generator")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        num_pdfs = st.number_input("How many PDFs to generate?", min_value=1, max_value=100, value=5, step=1)
        pdf_prefix = st.text_input("PDF filename prefix:", value="dummypdf")
        
        st.info("Each PDF will contain a unique random code in the format: TVLKXXXXXYYY")
    
    with col2:
        st.markdown("### Preview")
        preview_code = f"TVLK{random.randint(10000, 99999)}{''.join(random.choices(string.ascii_uppercase, k=3))}"
        st.code(f"Random Code: {preview_code} Dummy PDF")
    
    if st.button("🎲 Generate PDFs", type="primary"):
        with st.spinner("Generating PDFs..."):
            # Generate unique codes
            codes = set()
            while len(codes) < num_pdfs:
                code = f"TVLK{random.randint(10000, 99999)}{''.join(random.choices(string.ascii_uppercase, k=3))}"
                codes.add(code)
            codes = list(codes)
            
            # Create PDFs in memory
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                styles = getSampleStyleSheet()
                
                for i, code in enumerate(codes, 1):
                    pdf_buffer = io.BytesIO()
                    doc = SimpleDocTemplate(pdf_buffer, pagesize=A4)
                    content = [Paragraph(f"Random Code: {code} Dummy PDF", styles['Normal'])]
                    doc.build(content)
                    
                    # Add PDF to zip
                    pdf_buffer.seek(0)
                    zip_file.writestr(f"{pdf_prefix}_{code}.pdf", pdf_buffer.read())
            
            zip_buffer.seek(0)
            st.success(f"✅ Generated {num_pdfs} PDFs!")
            
            # Display list of generated PDFs
            st.subheader("Generated PDFs")
            pdf_names = [f"{pdf_prefix}_{code}.pdf" for code in codes]
            st.dataframe(pdf_names, use_container_width=True)
            
            # Download button
            st.download_button(
                label="📥 Download ZIP with all PDFs",
                data=zip_buffer,
                file_name="dummy_pdfs.zip",
                mime="application/zip"
            )

# Sidebar info
st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ About")
st.sidebar.info("""
**CSV Codes**: Generate random codes with default or custom format.

**Dummy PDFs**: Generate blank PDFs with unique codes.

All codes are guaranteed to be unique within each batch.
""")
