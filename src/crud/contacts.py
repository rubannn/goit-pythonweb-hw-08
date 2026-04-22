from sqlalchemy.orm import Session

from src.models.contact import Contact
from src.schemas.contact import ContactCreate, ContactUpdate


def create_contact(db: Session, body: ContactCreate) -> Contact:
    contact = Contact(**body.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


def get_contacts(db: Session) -> list[Contact]:
    return db.query(Contact).all()


def get_contact_by_id(db: Session, contact_id: int) -> Contact | None:
    return db.query(Contact).filter(Contact.id == contact_id).first()


def update_contact(
    db: Session, contact_id: int, body: ContactUpdate
) -> Contact | None:
    contact = get_contact_by_id(db, contact_id)

    if contact is None:
        return None

    update_data = body.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(contact, field, value)

    db.commit()
    db.refresh(contact)
    return contact


def delete_contact(db: Session, contact_id: int) -> Contact | None:
    contact = get_contact_by_id(db, contact_id)

    if contact is None:
        return None

    db.delete(contact)
    db.commit()
    return contact
