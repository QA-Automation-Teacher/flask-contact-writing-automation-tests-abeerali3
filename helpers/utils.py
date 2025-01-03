# Add the helper method to the Contacts model
from models import Contacts


# Helper method to convert contact to dictionary
def contact_to_dict(self):
    return {
        'id': self.id,
        'name': self.name,
        'surname': self.surname,
        'email': self.email,
        'phone': self.phone
    }


Contacts.to_dict = contact_to_dict