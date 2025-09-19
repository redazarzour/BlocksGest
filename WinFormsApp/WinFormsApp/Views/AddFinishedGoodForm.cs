using System;
using System.Windows.Forms;
using WinFormsApp.Models;

namespace WinFormsApp.Views
{
    public partial class AddFinishedGoodForm : Form
    {
        public FinishedGood FinishedGood { get; private set; }

        public AddFinishedGoodForm()
        {
            InitializeComponent();
        }

        private void okButton_Click(object sender, EventArgs e)
        {
            if (int.TryParse(quantityTextBox.Text, out int quantity))
            {
                FinishedGood = new FinishedGood
                {
                    Name = nameTextBox.Text,
                    Quantity = quantity,
                    BlockType = blockTypeTextBox.Text
                };
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
