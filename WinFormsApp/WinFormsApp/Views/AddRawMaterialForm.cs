using System;
using System.Windows.Forms;
using WinFormsApp.Models;

namespace WinFormsApp.Views
{
    public partial class AddRawMaterialForm : Form
    {
        public RawMaterial RawMaterial { get; private set; }

        public AddRawMaterialForm()
        {
            InitializeComponent();
        }

        private void okButton_Click(object sender, EventArgs e)
        {
            if (double.TryParse(quantityTextBox.Text, out double quantity) &&
                double.TryParse(unitPriceTextBox.Text, out double unitPrice))
            {
                RawMaterial = new RawMaterial
                {
                    Name = nameTextBox.Text,
                    Quantity = quantity,
                    Unit = unitTextBox.Text,
                    UnitPrice = unitPrice
                };
                this.DialogResult = DialogResult.OK;
            }
            else
            {
                MessageBox.Show("Please enter valid numbers for quantity and unit price.", "Invalid Input", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void cancelButton_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.Cancel;
        }
    }
}
