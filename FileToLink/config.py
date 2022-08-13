import os


class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    Token = os.environ.get("BOT_TOKEN")
    Session = os.environ.get("Session_String")
    if Session is None or Session == "":
        Session = ":memory:"
    App_Name = os.environ.get("APP_NAME")
    Port = int(os.environ.get("PORT"))
    Archive_Channel_ID = int(os.environ.get("ARCHIVE_CHANNEL_ID"))
    Start_Message = os.environ.get("Start_Message")
    Bot_Channel = os.environ.get("Bot_Channel_UserName")
    if Bot_Channel and Bot_Channel.startswith("@"):
        Bot_Channel = Bot_Channel[1:]
    elif Bot_Channel == "":
        Bot_Channel = None

    Link_Root = f"https://{App_Name}.herokuapp.com/"
    Download_Folder = "Files"
    Dev_Channel = "shadow_bots"
    Bot_UserName = None  # The bot will set it after starting
    Part_size = 1024 * 1024  # (1MB) For Pyrogram
    Buffer_Size = 512 * 1024  # For Quart
    Pre_Dl = 1  # How many parts to download from telegram before client request them
    Separate_Time = 4  # (seconds)  wait time between messages if user send more than one
    Sleep_Threshold = 60  # (Seconds) sleep threshold for flood wait exceptions
    Max_Fast_Processes = 1  # How many links user can update them to fast links at the same time


class Strings:
    start = Config.Start_Message
    dl_link = "🔗 Descargar LINK"
    st_link = "🎞 Stream LINK"
    generating_link = "**⏳ Generando Link...**"
    fast = "⚡️**El link ah sido actualizado a un Link rápido**⚡"
    update_link = "⚡ Actualizar a Link rápido"
    update_limited = (f"⛔ No puedes actualizar el Link {Config.Max_Fast_Processes} dentro de un tiempo, "
                      "por favor, espera a que se complete la actualización del Link pendiente...")
    re_update_link = "🔄 Re-Actualizar Link rápido"
    already_updated = "El Link ah sido actualizado"
    wait_update = "⏳ Actualizando Link..."
    wait = "⏳ Por favor espera..."
    progress = "⏳ Progreso"
    file_not_found = "⚠️Archivo no encontrado, Por favor reenvía el archivo..."
    delete_manually_button = "⚠️Ah sido eliminado"
    delete_forbidden = "El bot no puede borrar mensajes anteriores a 48 horas, has eliminado este mensaje manualmente..."
