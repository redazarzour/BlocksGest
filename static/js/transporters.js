document.addEventListener('DOMContentLoaded', () => {
    const transporterForm = document.getElementById('transporter-form');

    transporterForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const name = document.getElementById('name').value;
        const contactPerson = document.getElementById('contact-person').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const address = document.getElementById('address').value;
        const isCustomer = document.getElementById('is-customer').checked;

        try {
            const response = await fetch('/api/transporter/add', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, contact_person: contactPerson, email, phone, address, is_customer: isCustomer }),
            });

            const result = await response.json();

            if (result.success) {
                alert(result.message);
                location.reload();
            } else {
                alert('Error: ' + result.message);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while adding transporter');
        }
    });
});

function openEditModal(id, name, contactPerson, email, phone, address, isCustomer) {
    document.getElementById('edit-transporter-id').value = id;
    document.getElementById('edit-name').value = name;
    document.getElementById('edit-contact-person').value = contactPerson;
    document.getElementById('edit-email').value = email;
    document.getElementById('edit-phone').value = phone;
    document.getElementById('edit-address').value = address;
    document.getElementById('edit-is-customer').checked = isCustomer;
    $('#editTransporterModal').modal('show');
}

async function updateTransporter() {
    const id = document.getElementById('edit-transporter-id').value;
    const name = document.getElementById('edit-name').value;
    const contactPerson = document.getElementById('edit-contact-person').value;
    const email = document.getElementById('edit-email').value;
    const phone = document.getElementById('edit-phone').value;
    const address = document.getElementById('edit-address').value;
    const isCustomer = document.getElementById('edit-is-customer').checked;

    try {
        const response = await fetch('/api/transporter/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ transporter_id: parseInt(id), name, contact_person: contactPerson, email, phone, address, is_customer: isCustomer }),
        });

        const result = await response.json();

        if (result.success) {
            alert(result.message);
            location.reload();
        } else {
            alert('Error: ' + result.message);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while updating transporter');
    }
}

async function deleteTransporter(id) {
    if (confirm('Are you sure you want to delete this transporter?')) {
        try {
            const response = await fetch('/api/transporter/delete', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ transporter_id: parseInt(id) }),
            });

            const result = await response.json();

            if (result.success) {
                alert(result.message);
                location.reload();
            } else {
                alert('Error: ' + result.message);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while deleting transporter');
        }
    }
}
