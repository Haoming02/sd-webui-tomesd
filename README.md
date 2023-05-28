<h1 align="center">Outdated</h1>
<p align="center">This function is now implemented natively in the webui since v1.3</p>

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
            <td><img src="https://raw.githubusercontent.com/Haoming02/All-in-One-StableDiffusion-Guide/main/ToMe/Off.jpg" width=128></td>
            <td><img src="https://raw.githubusercontent.com/Haoming02/All-in-One-StableDiffusion-Guide/main/ToMe/0.3.jpg" width=128></td>
            <td><img src="https://raw.githubusercontent.com/Haoming02/All-in-One-StableDiffusion-Guide/main/ToMe/0.5.jpg" width=128></td>
            <td><img src="https://raw.githubusercontent.com/Haoming02/All-in-One-StableDiffusion-Guide/main/ToMe/0.7.jpg" width=128></td>
        </tr>
    </tbody>
</table>

# SD Webui Token Merging
This is an Extension for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), that implements [Token Merging](https://github.com/dbolya/tomesd).

## How to Use
After installing the extension, close and restart the webui completely.
It will then automatically install the `tomesd` package.

Now you can go to the **Token Merging** section of the **Settings** tab to enable the ToMe Patch and adjust the `Ratio`.