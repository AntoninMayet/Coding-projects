'''
Cheat sheet of commands:
[-h] [--model MODEL] [--device DEVICE] [--seed SEED] [--beta-start BETA_START] [--beta-end BETA_END]
               [--beta-schedule BETA_SCHEDULE] [--num-inference-steps NUM_INFERENCE_STEPS]
               [--guidance-scale GUIDANCE_SCALE] [--eta ETA] [--tokenizer TOKENIZER] [--prompt PROMPT]
               [--params-from PARAMS_FROM] [--init-image INIT_IMAGE] [--strength STRENGTH] [--mask MASK]
               [--output OUTPUT]
'''

import argparse

'''
device = "CPU"
prompt = "astronaut riding a horse at dawn"
output = "image.png"
notification = r'New-BurntToastNotification -Text "Stable Diffusion`nAll images have been generated" -Sound "default'
'''

parser = argparse.ArgumentParser(description="Agregator arguments")

parser.add_argument("--prompt", type=str, default="Astronaut riding a horse at dawn", help="help")

args = parser.parse_args()

print(args.prompt)