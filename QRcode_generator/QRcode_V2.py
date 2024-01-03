import tkinter as tk
from tkinter import ttk
import qrcode as qrcode_module

# Start variables zone
tk_accent_color = '#0D1B2A'
tk_secondary_color = '#415A77'
tk_dominant_color = '#E0E1DD'
qr_error_correction = qrcode_module.constants.ERROR_CORRECT_M
tk_xpadding = 15
tk_ypadding = 15
test = 'you are a loser'

tk_error_correction_options = ['Low', 'Medium', 'Quartile', 'High']
error_correction_mapping = {
    'Low': qrcode_module.constants.ERROR_CORRECT_L,
    'Medium': qrcode_module.constants.ERROR_CORRECT_M,
    'Quartile': qrcode_module.constants.ERROR_CORRECT_Q,
    'High': qrcode_module.constants.ERROR_CORRECT_H,
}
# End variables zone

# Start functions declaration zone
def retrieve_data():
    global qr_data, qr_file, qr_file_extension, qr_error_correction
    qr_data = tk_data.get('1.0', tk.END).strip()
    if tk_save_as_svg.get():
        qr_file_extension = '.svg'
    else:
        qr_file_extension = '.png'
        
    qr_file = tk_file_name.get() + qr_file_extension
    error_correction_option = tk_spinbox_error_correction.get()
    qr_error_correction = error_correction_mapping[error_correction_option]
    print(qr_data)
    print(qr_file)
    print(qr_file_extension)
    print(qr_error_correction)

    generate_qrcode()

def generate_qrcode():
    qr_code = qrcode_module.QRCode(
        version=1,
        error_correction=qr_error_correction,
        box_size=10,
        border=4,
    )
    qr_code.add_data(qr_data)
    qr_code.make(fit=True)
    img = qr_code.make_image(fill_color='black', back_color='white')
    img.save(qr_file)
# End of functions declaration zone

# Start tk_main_window config zone
tk_main_window = tk.Tk()
tk_main_window.configure(background=tk_dominant_color)
tk_main_window.title('QRcode generator')

tk_main_window.columnconfigure((0, 1), weight=1)

tk_main_window.rowconfigure(0, weight=2)
tk_main_window.rowconfigure((1, 2, 3, 4), weight=1)
# End tk_main_window config zone

# Start widgets zone
label_preview = ttk.Label(background=tk_dominant_color, text='Should be a preview of the QRcode')

tk_data = tk.Text(master=tk_main_window)

tk_file_name = ttk.Entry(master=tk_main_window)

tk_spinbox_error_correction = ttk.Combobox(tk_main_window, values=tk_error_correction_options)
tk_spinbox_error_correction.set('Medium')

tk_save_as_svg = tk.BooleanVar()
tk_save_as_svg.set(False)
tk_button_svg = ttk.Checkbutton(tk_main_window, text='Save as SVG', variable=tk_save_as_svg)

tk_save_data_button = ttk.Button(tk_main_window, text='Generate', command=retrieve_data)
# End widgets zone

# Start layout zone
label_preview.grid(row=0, column=0, columnspan=2, sticky='nsew')

tk_data.grid(row=1, column=0, rowspan=4, columnspan=1, padx=tk_xpadding, pady=tk_ypadding, sticky='nsew')

tk_file_name.grid(row=1, column=1, padx=tk_xpadding, pady=tk_ypadding, sticky='nsew')

tk_spinbox_error_correction.grid(row=2, column=1, padx=tk_xpadding, pady=tk_ypadding, sticky='nsew')

tk_button_svg.grid(row=3, column=1, padx=tk_xpadding, pady=tk_ypadding, sticky='w')

tk_save_data_button.grid(row=4, column=1, columnspan=2, padx=tk_xpadding, pady=tk_ypadding, sticky='nsew')
# End layout zone

tk_main_window.mainloop()