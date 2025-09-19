using System;
using System.Windows.Forms;
using WinFormsApp.Models;

namespace WinFormsApp.Views
{
    public partial class EditRawMaterialForm : Form
    {
        public RawMaterial RawMaterial { get; private set; }

        public EditRawMaterialForm(RawMaterial rawMaterial)
        {
            InitializeComponent();
            RawMaterial = rawMaterial;
            nameTextBox.Text = RawMaterial.Name;
            quantityTextBox.Text = RawMaterial.Quantity.ToString();
            unitTextBox.Text = RawMaterial.Unit;
            unitPriceTextBox.Text = RawMaterial.UnitPrice.ToString();
        }

        private void okButton_Click(object sender, EventArgs e)
        {
            if (double.TryParse(quantityTextBox.Text, out double quantity) &&
                double.TryParse(unitPriceTextBox.Text, out double unitPrice))
            {
                RawMaterial.Name = nameTextBox.Text;
                RawMaterial.Quantity = quantity;
                RawMaterial.Unit = unitTextBox.Text;
                RawMaterial.UnitPrice = unitPrice;
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
