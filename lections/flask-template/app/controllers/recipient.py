import csv
import tempfile
from datetime import date, datetime
from typing import Optional
from werkzeug.datastructures import FileStorage
from app import db

from pydantic import BaseModel, validator

from app.models import Recipient


class RecipientRow(BaseModel):
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    birthday: Optional[date]

    @validator(
        "birthday",
        pre=True,
    )
    def parse_birthday(cls, v: str) -> date:
        return datetime.strptime(v, "%d.%m.%Y").date()

    class Config:
        orm_mode = True


def upload_recipient_controller(input_file: FileStorage):
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        file_path = temp_file.name
        with open(file_path, "wb") as examined_file:
            begin_data = input_file.read(3)
            if b"\xef\xbb\xbf" not in begin_data:
                examined_file.write(begin_data)
            examined_file.write(input_file.read())
        with open(file_path, mode="r") as read_file:
            reader = csv.DictReader(read_file)
            reader.fieldnames = [
                name.lower().replace(" ", "_") for name in reader.fieldnames
            ]
            for row in reader:
                r: RecipientRow = RecipientRow.parse_obj(row)
                r_exist = (
                    db.session.query(Recipient)
                    .filter_by(
                        email=r.email,
                        first_name=r.first_name,
                        last_name=r.last_name,
                        phone=r.phone,
                        address=r.address,
                        birthday=r.birthday,
                    )
                    .first()
                )
                if r_exist:
                    pass
                else:
                    recipient = Recipient(**r.dict())
                    recipient.save()
            db.session.commit()
