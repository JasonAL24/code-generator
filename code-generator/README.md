# 📄 Code & PDF Generator

A Streamlit-based web dashboard for generating random codes and dummy PDF files. Perfect for testing, development, or generating unique identifiers in bulk.

## 🚀 Features

- **CSV Code Generator**: Generate unique random codes with customizable formats
- **Dummy PDF Generator**: Create PDF files with unique codes for testing purposes
- **Custom Format Support**: Define your own code patterns using placeholders
- **Bulk Generation**: Generate up to 1,000,000 codes or 100 PDFs at once
- **Download Ready**: Export as CSV files or ZIP archives

## 📋 Requirements

- Python 3.7 or higher
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JasonAldeo/code-generator.git
   cd code-generator
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install packages individually:
   ```bash
   pip install streamlit reportlab
   ```

## 🎯 Usage

1. **Start the dashboard**:
   ```bash
   streamlit run dashboard.py
   ```

2. **Open your browser**:
   The dashboard will automatically open at `http://localhost:8501`

3. **Choose your generator type**:
   - **CSV Codes**: Generate random codes in CSV format
   - **Dummy PDFs**: Generate PDF files with unique codes

## 🔧 Code Generation Options

### Default Format
- Pattern: `TVLK#####XXX`
- Example: `TVLK12345ABC`

### Custom Format
Use these placeholders to create your own patterns:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{d:X}` | X random digits | `{d:5}` → `12345` |
| `{l:X}` | X random uppercase letters | `{l:3}` → `ABC` |
| `{s:X}` | X random lowercase letters | `{s:4}` → `abcd` |

#### Custom Format Examples:
- `ORDER-{d:6}` → `ORDER-123456`
- `USER_{l:2}{d:4}` → `USER_AB1234`
- `temp_{s:3}-{d:3}` → `temp_xyz-789`

## 📁 Output Formats

### CSV Codes
- **File**: `generated_codes.csv`
- **Format**: One code per line
- **Use case**: Import into databases, spreadsheets, or other applications

### Dummy PDFs
- **File**: `dummy_pdfs.zip`
- **Contents**: Individual PDF files named `{prefix}_{code}.pdf`
- **Use case**: Testing file processing systems, mock data generation

## 🎨 Dashboard Preview

The dashboard includes:
- **Sidebar**: Generator type selection and info
- **Main Panel**: Configuration options and generation controls
- **Preview**: Live preview of generated codes
- **Download**: Direct download buttons for generated files

## 🔒 Features & Guarantees

- ✅ **Unique Codes**: All codes within a batch are guaranteed to be unique
- ✅ **Duplicate Detection**: Automatic detection and regeneration of duplicates
- ✅ **Memory Efficient**: Files generated in-memory without temporary storage
- ✅ **Scalable**: Handle large batches efficiently

## 🐛 Troubleshooting

### Common Issues

1. **Module not found error**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. **Port already in use**:
   ```bash
   streamlit run dashboard.py --server.port 8502
   ```

3. **Browser doesn't open automatically**:
   Manually navigate to `http://localhost:8501`

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Jason Aldeo**
- GitHub: [@JasonAldeo](https://github.com/JasonAldeo)
- Email: jason.leonard@traveloka.com

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- PDF generation powered by [ReportLab](https://www.reportlab.com/)

---

⭐ If you found this project helpful, please give it a star!