import tkinter as tk
from tkinter import ttk

'''
Cheat sheet of commands:
[-h] [--model MODEL] [--device DEVICE] [--seed SEED] [--beta-start BETA_START] [--beta-end BETA_END]
               [--beta-schedule BETA_SCHEDULE] [--num-inference-steps NUM_INFERENCE_STEPS]
               [--guidance-scale GUIDANCE_SCALE] [--eta ETA] [--tokenizer TOKENIZER] [--prompt PROMPT]
               [--params-from PARAMS_FROM] [--init-image INIT_IMAGE] [--strength STRENGTH] [--mask MASK]
               [--output OUTPUT]
'''

# Start of variables zone
light_green = '#606C38'
dark_green = '#606C38'
white = '#FEFAE0'
light_orange = '#DDA15E'
dark_orange = '#BC6C25'

tk_xpadding = 15
tk_ypadding = 15


device = 'CPU'
prompt = 'astronaut riding a horse at dawn'
output = 'image.png'
notification = r'New-BurntToastNotification -Text "Stable Diffusion`nAll images have been generated" -Sound "default"'
last_command = 'python --version'
num_inference_steps = 32
# End of variables zone

# Start tk_window config zone
tk_window = tk.Tk()
tk_window.configure(background=dark_green)
tk_window.title('Open vino commands agregator')
tk_window.columnconfigure((0, 1, 2), weight=1)
tk_window.rowconfigure((1, 2, 3, 4, 5), weight=1)
# End tk_window config zone

# Start of widget town
tk_output = tk.Label()

tk_prompt = tk.Text(master=tk_window)

tk_device_cpu = ttk.Radiobutton(tk_window, text='CPU', value='CPU', variable=device)
tk_device_gpu = ttk.Radiobutton(tk_window, text='GPU', value='GPU', variable=device)
# End of widget town

# Start of the layout
tk_output.grid(row=0, column=0, rowspan=1, columnspan=2, padx=tk_xpadding, pady=tk_ypadding, sticky='nsew')

tk_prompt.grid(row=0, column=0, rowspan=4, columnspan=2, padx=tk_xpadding, pady=tk_ypadding, sticky='nsew')

tk_device_cpu.grid(row=0, column=3, rowspan=1, columnspan=1, padx=tk_xpadding, pady=tk_ypadding, sticky='nsew')
tk_device_gpu.grid(row=0, column=4, rowspan=1, columnspan=1, padx=tk_xpadding, pady=tk_ypadding, sticky='nsew')
# End of the layout

tk_window.mainloop()