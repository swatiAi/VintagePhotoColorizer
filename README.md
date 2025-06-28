# 🎞️ Vintage Photo Colorizer

A DeOldify-based Flask web app that colorizes black-and-white images using deep learning and offers a modern, vintage-themed user interface.

---

## 🌟 Features

- 🖼 Upload black & white photos via drag & drop or file input.
- 🎨 Get high-quality colorized results powered by DeOldify.
- 🔄 Interactive **before/after slider** for visual comparison.
- ⏳ Spinner animation during processing.
- 📥 Download the final result in one click.
- 🧹 Automatically clears previous uploads to keep it lightweight.

---

## 🧠 Technologies Used

- **Backend**: Python, Flask
- **Model**: [DeOldify](https://github.com/jantic/DeOldify) (ResNet34 with Artistic model)
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **Other**: Torch, FastAI, Pillow, OpenCV

---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/VintagePhotoColorizer.git
cd VintagePhotoColorizer
```

### 2️⃣ Set Up Python Environment

```bash
python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate       # On Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download the DeOldify Model

Download the **pretrained model weights**:

- [ColorizeArtistic_gen.pth](https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth)

Place it in the following directory:
```
deoldify/models/ColorizeArtistic_gen.pth
```

### 5️⃣ Run the App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Folder Structure

```
VintagePhotoColorizer/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── deoldify/
│   ├── ...
│   └── models/
│       └── ColorizeArtistic_gen.pth (not uploaded)
├── static/
│   ├── css/
│   │   └── style.css
│   ├── img/
│   │   └── spinner.gif
│   ├── uploads/
│   └── results/
├── templates/
│   └── index.html
```

---

## 📷 Demo

| Grayscale Input | Colorized Output |
|------------------|-------------------|
| ![](static/img/sample_bw.jpg) | ![](static/img/sample_color.jpg) |

---

## 📜 License

MIT License

> Powered by [DeOldify](https://github.com/jantic/DeOldify)  
> Credits to Jason Antic and contributors

---

## 🙋‍♂️ Contributions & Feedback

Pull requests and suggestions are welcome.  
For issues or ideas, open an issue on GitHub.