from modules import script_callbacks, shared
import gradio as gr
import tomesd

def on_model_loaded(sd_model):
    if hasattr(shared.opts, "token_merging_enabled"):
        if shared.opts.token_merging_enabled:
            print("Applying ToMe Patch...")

            try:
                tomesd.apply_patch(sd_model, ratio=shared.opts.token_merging_ratio)
            except Exception as e:
                print("Failed to apply ToMe Patch: ", e)
                return

            print("ToMe Patch Applied")

        else:
            print("Removing ToMe Patch...")

            try:
                tomesd.remove_patch(sd_model)
            except Exception as e:
                print("Failed to remove ToMe Patch: ", e)
                return

            print("ToMe Patch Removed")

def on_ui_settings():
    section = ("token_merging", "Token Merging")

    shared.opts.add_option(
        "token_merging_enabled",
        shared.OptionInfo(False, "Enable Token Merging", section=section),
    )
    shared.opts.add_option(
        "token_merging_ratio",
        shared.OptionInfo(
            0.5,
            "Token Merging - Ratio",
            gr.Slider,
            {"minimum": 0.1, "maximum": 0.9, "step": 0.1},
            section=section,
        ),
    )

script_callbacks.on_model_loaded(on_model_loaded)
script_callbacks.on_ui_settings(on_ui_settings)