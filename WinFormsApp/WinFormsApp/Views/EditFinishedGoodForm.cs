using System;
using System.Windows.Forms;
using WinFormsApp.Models;

namespace WinFormsApp.Views
{
    public partial class EditFinishedGoodForm : Form
    {
        public FinishedGood FinishedGood { get; private set; }

        public EditFinishedGoodForm(FinishedGood finishedGood)
        {
            InitializeComponent();
            FinishedGood = finishedGood;
            nameTextBox.Text = FinishedGood.Name;
            quantityTextBox.Text = FinishedGood.Quantity.ToString();
            blockTypeTextBox.Text = FinishedGood.BlockType;
        }

        private void okButton_Click(object sender, EventArgs e)
        {
            if (int.TryParse(quantityTextBox.Text, out int quantity))
            {
                FinishedGood.Name = nameTextBox.Text;
                FinishedGood.Quantity = quantity;
                FinishedGood.BlockType = blockTypeTextBox.Text;
                this.DialogResult = DialogResult.OK;
            }
            else
            {
                MessageBox.Show("Please enter a valid number for quantity.", "Invalid Input", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void cancelButton_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.Cancel;
        }
    }
}
