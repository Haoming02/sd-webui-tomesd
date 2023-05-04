# Token Merging for Stable Diffusion
This is an Extention that implements [Token Merging](https://github.com/dbolya/tomesd) for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui).

After installing the extension, close and restart the webui **and** the terminal completely.
It will automatically install the `tomesd` package on launch next time.

Now you can go to the **Token Merging** section of the **Settings** tab to enable the ToMe Patch and adjust the `Ratio`.

## Examples
> Tested on **RTX 3060** w/ `--xformers`
 
> Generating at 512x512; 32 Steps; Euler a

> Hires. Fix to 1024x1024; 16 Steps; Latent (nearest)

> Same Prompt; Same Seed

<table>
    <tbody>
        <tr align="center">
            <td><b>Ratio</b></td>
            <td>Off</td>
            <td>0.3</td>
            <td>0.5</td>
            <td>0.7</td>
        </tr>
        <tr align="center">
            <td><b>Base</b></td>
            <td>8.00 it/s</td>
            <td>8.33 it/s</td>
            <td>8.69 it/s</td>
            <td>8.91 it/s</td>
        </tr>
        <tr align="center">
            <td><b>Hires. Fix</b></td>
            <td>1.48 it/s</td>
            <td>1.86 it/s</td>
            <td>2.15 it/s</td>
            <td>2.38 it/s</td>
        </tr>
        <tr align="center">
            <td><b>Total</b></td>
            <td>16s</td>
            <td>14s</td>
            <td>12s</td>
            <td>10s</td>
        </tr>
        <tr align="center">
            <td><b>Result</b></td>
            <td><img src="https://raw.githubusercontent.com/Haoming02/All-in-One-StableDiffusion-Guide/main/ToMe/Off.jpg" width=100></td>
            <td><img src="https://raw.githubusercontent.com/Haoming02/All-in-One-StableDiffusion-Guide/main/ToMe/0.3.jpg" width=100></td>
            <td><img src="https://raw.githubusercontent.com/Haoming02/All-in-One-StableDiffusion-Guide/main/ToMe/0.5.jpg" width=100></td>
            <td><img src="https://raw.githubusercontent.com/Haoming02/All-in-One-StableDiffusion-Guide/main/ToMe/0.7.jpg" width=100></td>
        </tr>
    </tbody>
</table>

## Main Difference from *[the Other Script](https://git.mmaker.moe/mmaker/sd-webui-tome)*
- Now installs the `tomesd` package automatically
- Removed all other settings except for `Ratio`, since the original project mentions:
> Using the default options are recommended for the highest quality, tune ratio to suit your needs.
- If you want to tinker around with the settings, then install the other Extension instead