from models import db, Contacts
from faker import Factory
from app import app


def generate_fake_contacts(num = 100, locale = 'he_IL'):
    '''
    Generate fake contacts
    @input num = Number of contacts
    @input locale = Language default language is Hebrew (he_IL)
    '''
    # fake = Factory.create()
    # Spanish
    # fake = Factory.create('es_ES')
    fake = Factory.create(locale)
    # fake = Factory.create('ar_PS')
    
    # Make 100 fake contacts
    for num in range(num):
        fullname = fake.name().split()
        name = fullname[0]
        surname = ' '.join(fullname[1:])
        email = fake.email()
        phone = fake.phone_number()
        # Save in database
        mi_contacto = Contacts(name, surname, email, phone)
        db.session.add(mi_contacto)
        db.session.commit()


with app.app_context():
    # Reload tables
    db.drop_all()
    db.create_all()
    generate_fake_contacts()