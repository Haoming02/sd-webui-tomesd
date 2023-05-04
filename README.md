# Token Merging for Stable Diffusion
This is an Extention that implements [Token Merging](https://github.com/dbolya/tomesd) for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui).

After installing the extension, close and restart the webui **and** the terminal completely.
It will automatically install the `tomesd` package on launch next time.

Now you can go to the **Token Merging** section of the **Settings** tab to enable the ToMe Patch and adjust the `Ratio`.

### Main Difference from *[the Other Script](https://git.mmaker.moe/mmaker/sd-webui-tome)*
- Now installs the `tomesd` package automatically
- Removed all other settings except for `Ratio`, since the original project mentions:
> Using the default options are recommended for the highest quality, tune ratio to suit your needs.
- If you want to tinker around with the settings, then install the other Extension instead