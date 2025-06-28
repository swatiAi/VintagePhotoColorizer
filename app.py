import os
import sys
import uuid
from pathlib import Path
from flask import Flask, render_template, request, send_from_directory

# Add DeOldify to system path
sys.path.append(os.path.abspath('./deoldify'))

# DeOldify setup
from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import get_image_colorizer

# Set device to GPU
device.set(device=DeviceId.GPU0)

# Flask setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/results'

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

# Initialize colorizer (artistic=True for more vivid colorization)
colorizer = get_image_colorizer(artistic=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    input_filename = None
    output_filename = None

    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file and uploaded_file.filename != '':
            # Save original upload
            ext = os.path.splitext(uploaded_file.filename)[-1]
            img_id = f"{uuid.uuid4()}{ext}"
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], img_id)
            uploaded_file.save(input_path)

            # Colorize using DeOldify
            output_path = os.path.join(app.config['RESULT_FOLDER'], img_id)
            colorizer.plot_transformed_image(
                path=input_path,
                render_factor=35,
                results_dir=Path(app.config['RESULT_FOLDER']),
                display_render_factor=False
            )

            return render_template(
                'index.html',
                input_path=f"uploads/{img_id}",
                output_path=f"results/{img_id}",
                download_link=f"/download/{img_id}"
            )

    return render_template('index.html')


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['RESULT_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
