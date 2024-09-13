import torch
from diffusers import AutoPipelineForText2Image


class Image2DDao:
    def __init__(
        self,
        model_name="stabilityai/sdxl-turbo",  # Updated model name for SDXL Turbo
        device="cuda",
        torch_dtype=torch.float16,
        variant="fp16",
        use_safetensors=True,
    ):
        self.pipe = AutoPipelineForText2Image.from_pretrained(
            model_name,
            torch_dtype=torch_dtype,
            variant=variant,
            use_safetensors=use_safetensors,
        )
        self.pipe = self.pipe.to(device)

    def generate_image(
        self,
        pos_prompt,
        neg_prompt="",
        steps=20,
        guidance=0.0,
        width=512,
        height=512,
        num_images=1,
    ):
        return self.pipe(
            prompt=pos_prompt,
            negative_prompt=neg_prompt,
            num_inference_steps=steps,
            guidance_scale=guidance,
            width=width,
            height=height,
            num_images_per_prompt=num_images,
        ).images[0]
