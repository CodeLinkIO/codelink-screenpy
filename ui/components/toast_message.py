from screenpy_selenium import Target


class ToastMessageAlert:

    TOAST_MESSAGE = Target.the('Toast Message').located_by("p[class^='Message__Text']")
    CLOSE_ICON = Target.the('Close Icon On Toast Message').located_by("#message-board svg")
