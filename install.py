import launch

package = 'tomesd'

if not launch.is_installed(package):
    launch.run_pip(f"install {package}", f"sd-webui-tomesd requirement: {package}")