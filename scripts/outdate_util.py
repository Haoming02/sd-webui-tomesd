import modules.scripts as scripts
import gradio as gr
import os

class OutdateReminder(scripts.Script):

    def title(self):
        return None

    def ui(self, is_img2img):
        if is_img2img == True:
            return None

        NAME = 'tomesd'
        VERSION = 'v1.3'

        print('\n\nWarning! Extension [' + NAME + '] has been outdated since sd-webui ' + VERSION + '!\n\n')
        return None