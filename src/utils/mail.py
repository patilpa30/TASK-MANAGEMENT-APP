from pydantic import BaseModel , EmailStr
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType



conf = ConnectionConfig(
    MAIL_USERNAME ="username",
    MAIL_PASSWORD = "*******",
    MAIL_FROM = "user@email.com",
    MAIL_PORT = 465,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="Desired name",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

async def send_email(emails: List[str]):
    html= """<p> Hi , Thanks for Registration .Our Team Will connect you soon! </p>"""
    message = MessageSchema(
        subject="Registration Confirmation",
        recipients=emails,  # Can include "Name <email@domain.com>" format
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return {"message": "email has been sent"}