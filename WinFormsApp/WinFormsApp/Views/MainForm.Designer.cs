namespace WinFormsApp.Views
{
    partial class MainForm
    {
        private System.ComponentModel.IContainer components = null;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        private void InitializeComponent()
        {
            this.tabControl = new System.Windows.Forms.TabControl();
            this.inventoryTabPage = new System.Windows.Forms.TabPage();
            this.rawMaterialsDataGridView = new System.Windows.Forms.DataGridView();
            this.addRawMaterialButton = new System.Windows.Forms.Button();
            this.editRawMaterialButton = new System.Windows.Forms.Button();
            this.deleteRawMaterialButton = new System.Windows.Forms.Button();

            this.productionTabPage = new System.Windows.Forms.TabPage();
            this.salesTabPage = new System.Windows.Forms.TabPage();
            this.laborTabPage = new System.Windows.Forms.TabPage();
            this.suppliersTabPage = new System.Windows.Forms.TabPage();
            this.qualityControlTabPage = new System.Windows.Forms.TabPage();
            this.reportsTabPage = new System.Windows.Forms.TabPage();


            this.tabControl.SuspendLayout();
            this.inventoryTabPage.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.rawMaterialsDataGridView)).BeginInit();
            this.SuspendLayout();

            //
            // tabControl
            //
            this.tabControl.Controls.Add(this.inventoryTabPage);
            this.tabControl.Controls.Add(this.productionTabPage);
            this.tabControl.Controls.Add(this.salesTabPage);
            this.tabControl.Controls.Add(this.laborTabPage);
            this.tabControl.Controls.Add(this.suppliersTabPage);
            this.tabControl.Controls.Add(this.qualityControlTabPage);
            this.tabControl.Controls.Add(this.reportsTabPage);
            this.tabControl.Location = new System.Drawing.Point(12, 12);
            this.tabControl.Name = "tabControl";
            this.tabControl.SelectedIndex = 0;
            this.tabControl.Size = new System.Drawing.Size(776, 426);
            this.tabControl.TabIndex = 0;

            //
            // inventoryTabPage
            //
            this.inventoryTabPage.Controls.Add(this.deleteRawMaterialButton);
            this.inventoryTabPage.Controls.Add(this.editRawMaterialButton);
            this.inventoryTabPage.Controls.Add(this.addRawMaterialButton);
            this.inventoryTabPage.Controls.Add(this.rawMaterialsDataGridView);
            this.inventoryTabPage.Location = new System.Drawing.Point(4, 22);
            this.inventoryTabPage.Name = "inventoryTabPage";
            this.inventoryTabPage.Padding = new System.Windows.Forms.Padding(3);
            this.inventoryTabPage.Size = new System.Drawing.Size(768, 400);
            this.inventoryTabPage.TabIndex = 0;
            this.inventoryTabPage.Text = "Inventory";
            this.inventoryTabPage.UseVisualStyleBackColor = true;

            //
            // rawMaterialsDataGridView
            //
            this.rawMaterialsDataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.rawMaterialsDataGridView.Location = new System.Drawing.Point(6, 6);
            this.rawMaterialsDataGridView.Name = "rawMaterialsDataGridView";
            this.rawMaterialsDataGridView.Size = new System.Drawing.Size(756, 350);
            this.rawMaterialsDataGridView.TabIndex = 0;

            //
            // addRawMaterialButton
            //
            this.addRawMaterialButton.Location = new System.Drawing.Point(6, 362);
            this.addRawMaterialButton.Name = "addRawMaterialButton";
            this.addRawMaterialButton.Size = new System.Drawing.Size(75, 23);
            this.addRawMaterialButton.TabIndex = 1;
            this.addRawMaterialButton.Text = "Add";
            this.addRawMaterialButton.UseVisualStyleBackColor = true;

            //
            // editRawMaterialButton
            //
            this.editRawMaterialButton.Location = new System.Drawing.Point(87, 362);
            this.editRawMaterialButton.Name = "editRawMaterialButton";
            this.editRawMaterialButton.Size = new System.Drawing.Size(75, 23);
            this.editRawMaterialButton.TabIndex = 2;
            this.editRawMaterialButton.Text = "Edit";
            this.editRawMaterialButton.UseVisualStyleBackColor = true;

            //
            // deleteRawMaterialButton
            //
            this.deleteRawMaterialButton.Location = new System.Drawing.Point(168, 362);
            this.deleteRawMaterialButton.Name = "deleteRawMaterialButton";
            this.deleteRawMaterialButton.Size = new System.Drawing.Size(75, 23);
            this.deleteRawMaterialButton.TabIndex = 3;
            this.deleteRawMaterialButton.Text = "Delete";
            this.deleteRawMaterialButton.UseVisualStyleBackColor = true;

            //
            // productionTabPage
            //
            this.productionTabPage.Controls.Add(this.deleteFinishedGoodButton);
            this.productionTabPage.Controls.Add(this.editFinishedGoodButton);
            this.productionTabPage.Controls.Add(this.addFinishedGoodButton);
            this.productionTabPage.Controls.Add(this.finishedGoodsDataGridView);
            this.productionTabPage.Location = new System.Drawing.Point(4, 22);
            this.productionTabPage.Name = "productionTabPage";
            this.productionTabPage.Padding = new System.Windows.Forms.Padding(3);
            this.productionTabPage.Size = new System.Drawing.Size(768, 400);
            this.productionTabPage.TabIndex = 1;
            this.productionTabPage.Text = "Production";
            this.productionTabPage.UseVisualStyleBackColor = true;

            //
            // finishedGoodsDataGridView
            //
            this.finishedGoodsDataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.finishedGoodsDataGridView.Location = new System.Drawing.Point(6, 6);
            this.finishedGoodsDataGridView.Name = "finishedGoodsDataGridView";
            this.finishedGoodsDataGridView.Size = new System.Drawing.Size(756, 350);
            this.finishedGoodsDataGridView.TabIndex = 0;

            //
            // addFinishedGoodButton
            //
            this.addFinishedGoodButton.Location = new System.Drawing.Point(6, 362);
            this.addFinishedGoodButton.Name = "addFinishedGoodButton";
            this.addFinishedGoodButton.Size = new System.Drawing.Size(75, 23);
            this.addFinishedGoodButton.TabIndex = 1;
            this.addFinishedGoodButton.Text = "Add";
            this.addFinishedGoodButton.UseVisualStyleBackColor = true;

            //
            // editFinishedGoodButton
            //
            this.editFinishedGoodButton.Location = new System.Drawing.Point(87, 362);
            this.editFinishedGoodButton.Name = "editFinishedGoodButton";
            this.editFinishedGoodButton.Size = new System.Drawing.Size(75, 23);
            this.editFinishedGoodButton.TabIndex = 2;
            this.editFinishedGoodButton.Text = "Edit";
            this.editFinishedGoodButton.UseVisualStyleBackColor = true;

            //
            // deleteFinishedGoodButton
            //
            this.deleteFinishedGoodButton.Location = new System.Drawing.Point(168, 362);
            this.deleteFinishedGoodButton.Name = "deleteFinishedGoodButton";
            this.deleteFinishedGoodButton.Size = new System.Drawing.Size(75, 23);
            this.deleteFinishedGoodButton.TabIndex = 3;
            this.deleteFinishedGoodButton.Text = "Delete";
            this.deleteFinishedGoodButton.UseVisualStyleBackColor = true;

            //
            // salesTabPage
            //
            this.salesTabPage.Location = new System.Drawing.Point(4, 22);
            this.salesTabPage.Name = "salesTabPage";
            this.salesTabPage.Size = new System.Drawing.Size(768, 400);
            this.salesTabPage.TabIndex = 2;
            this.salesTabPage.Text = "Sales";
            this.salesTabPage.UseVisualStyleBackColor = true;

            //
            // laborTabPage
            //
            this.laborTabPage.Location = new System.Drawing.Point(4, 22);
            this.laborTabPage.Name = "laborTabPage";
            this.laborTabPage.Size = new System.Drawing.Size(768, 400);
            this.laborTabPage.TabIndex = 3;
            this.laborTabPage.Text = "Labor";
            this.laborTabPage.UseVisualStyleBackColor = true;

            //
            // suppliersTabPage
            //
            this.suppliersTabPage.Location = new System.Drawing.Point(4, 22);
            this.suppliersTabPage.Name = "suppliersTabPage";
            this.suppliersTabPage.Size = new System.Drawing.Size(768, 400);
            this.suppliersTabPage.TabIndex = 4;
            this.suppliersTabPage.Text = "Suppliers";
            this.suppliersTabPage.UseVisualStyleBackColor = true;

            //
            // qualityControlTabPage
            //
            this.qualityControlTabPage.Location = new System.Drawing.Point(4, 22);
            this.qualityControlTabPage.Name = "qualityControlTabPage";
            this.qualityControlTabPage.Size = new System.Drawing.Size(768, 400);
            this.qualityControlTabPage.TabIndex = 5;
            this.qualityControlTabPage.Text = "Quality Control";
            this.qualityControlTabPage.UseVisualStyleBackColor = true;

            //
            // reportsTabPage
            //
            this.reportsTabPage.Location = new System.Drawing.Point(4, 22);
            this.reportsTabPage.Name = "reportsTabPage";
            this.reportsTabPage.Size = new System.Drawing.Size(768, 400);
            this.reportsTabPage.TabIndex = 6;
            this.reportsTabPage.Text = "Reports";
            this.reportsTabPage.UseVisualStyleBackColor = true;

            //
            // MainForm
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.tabControl);
            this.Name = "MainForm";
            this.Text = "MainForm";
            this.tabControl.ResumeLayout(false);
            this.inventoryTabPage.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.rawMaterialsDataGridView)).EndInit();
            this.ResumeLayout(false);
        }

        #endregion

        private System.Windows.Forms.TabControl tabControl;
        private System.Windows.Forms.TabPage inventoryTabPage;
        private System.Windows.Forms.DataGridView rawMaterialsDataGridView;
        private System.Windows.Forms.Button addRawMaterialButton;
        private System.Windows.Forms.Button editRawMaterialButton;
        private System.Windows.Forms.Button deleteRawMaterialButton;
        private System.Windows.Forms.TabPage productionTabPage;
        private System.Windows.Forms.TabPage salesTabPage;
        private System.Windows.Forms.TabPage laborTabPage;
        private System.Windows.Forms.TabPage suppliersTabPage;
        private System.Windows.Forms.TabPage qualityControlTabPage;
        private System.Windows.Forms.TabPage reportsTabPage;
        private System.Windows.Forms.DataGridView finishedGoodsDataGridView;
        private System.Windows.Forms.Button addFinishedGoodButton;
        private System.Windows.Forms.Button editFinishedGoodButton;
        private System.Windows.Forms.Button deleteFinishedGoodButton;
    }
}
