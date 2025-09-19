using System;
using System.Data.Entity;
using System.Windows.Forms;
using WinFormsApp.Data;
using WinFormsApp.Models;
using WinFormsApp.Views;

namespace WinFormsApp.Views
{
    public partial class MainForm : Form
    {
        private AppContext _context;

        public MainForm()
        {
            InitializeComponent();
            _context = new AppContext();
            this.Load += MainForm_Load;
            addRawMaterialButton.Click += addRawMaterialButton_Click;
            editRawMaterialButton.Click += editRawMaterialButton_Click;
            deleteRawMaterialButton.Click += deleteRawMaterialButton_Click;

            addFinishedGoodButton.Click += addFinishedGoodButton_Click;
            editFinishedGoodButton.Click += editFinishedGoodButton_Click;
            deleteFinishedGoodButton.Click += deleteFinishedGoodButton_Click;
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            LoadRawMaterials();
            LoadFinishedGoods();
        }

        private void LoadRawMaterials()
        {
            _context.RawMaterials.Load();
            rawMaterialsDataGridView.DataSource = _context.RawMaterials.Local.ToBindingList();
        }

        private void addRawMaterialButton_Click(object sender, EventArgs e)
        {
            var addRawMaterialForm = new AddRawMaterialForm();
            if (addRawMaterialForm.ShowDialog() == DialogResult.OK)
            {
                _context.RawMaterials.Add(addRawMaterialForm.RawMaterial);
                _context.SaveChanges();
                LoadRawMaterials();
            }
        }

        private void editRawMaterialButton_Click(object sender, EventArgs e)
        {
            if (rawMaterialsDataGridView.SelectedRows.Count > 0)
            {
                var rawMaterialId = (int)rawMaterialsDataGridView.SelectedRows[0].Cells["Id"].Value;
                var rawMaterial = _context.RawMaterials.Find(rawMaterialId);

                if (rawMaterial != null)
                {
                    var editRawMaterialForm = new EditRawMaterialForm(rawMaterial);
                    if (editRawMaterialForm.ShowDialog() == DialogResult.OK)
                    {
                        _context.SaveChanges();
                        LoadRawMaterials();
                    }
                }
            }
        }

        private void deleteRawMaterialButton_Click(object sender, EventArgs e)
        {
            if (rawMaterialsDataGridView.SelectedRows.Count > 0)
            {
                var rawMaterialId = (int)rawMaterialsDataGridView.SelectedRows[0].Cells["Id"].Value;
                var rawMaterial = _context.RawMaterials.Find(rawMaterialId);

                if (rawMaterial != null)
                {
                    if (MessageBox.Show("Are you sure you want to delete this raw material?", "Confirm Delete", MessageBoxButtons.YesNo) == DialogResult.Yes)
                    {
                        _context.RawMaterials.Remove(rawMaterial);
                        _context.SaveChanges();
                        LoadRawMaterials();
                    }
                }
            }
        }

        private void LoadFinishedGoods()
        {
            _context.FinishedGoods.Load();
            finishedGoodsDataGridView.DataSource = _context.FinishedGoods.Local.ToBindingList();
        }

        private void addFinishedGoodButton_Click(object sender, EventArgs e)
        {
            var addFinishedGoodForm = new AddFinishedGoodForm();
            if (addFinishedGoodForm.ShowDialog() == DialogResult.OK)
            {
                _context.FinishedGoods.Add(addFinishedGoodForm.FinishedGood);
                _context.SaveChanges();
                LoadFinishedGoods();
            }
        }

        private void editFinishedGoodButton_Click(object sender, EventArgs e)
        {
            if (finishedGoodsDataGridView.SelectedRows.Count > 0)
            {
                var finishedGoodId = (int)finishedGoodsDataGridView.SelectedRows[0].Cells["Id"].Value;
                var finishedGood = _context.FinishedGoods.Find(finishedGoodId);

                if (finishedGood != null)
                {
                    var editFinishedGoodForm = new EditFinishedGoodForm(finishedGood);
                    if (editFinishedGoodForm.ShowDialog() == DialogResult.OK)
                    {
                        _context.SaveChanges();
                        LoadFinishedGoods();
                    }
                }
            }
        }

        private void deleteFinishedGoodButton_Click(object sender, EventArgs e)
        {
            if (finishedGoodsDataGridView.SelectedRows.Count > 0)
            {
                var finishedGoodId = (int)finishedGoodsDataGridView.SelectedRows[0].Cells["Id"].Value;
                var finishedGood = _context.FinishedGoods.Find(finishedGoodId);

                if (finishedGood != null)
                {
                    if (MessageBox.Show("Are you sure you want to delete this finished good?", "Confirm Delete", MessageBoxButtons.YesNo) == DialogResult.Yes)
                    {
                        _context.FinishedGoods.Remove(finishedGood);
                        _context.SaveChanges();
                        LoadFinishedGoods();
                    }
                }
            }
        }
    }
}
