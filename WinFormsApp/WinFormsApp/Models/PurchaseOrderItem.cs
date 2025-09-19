namespace WinFormsApp.Models
{
    public class PurchaseOrderItem
    {
        public int Id { get; set; }
        public int PurchaseOrderId { get; set; }
        public int RawMaterialId { get; set; }
        public double Quantity { get; set; }
        public double UnitPrice { get; set; }
        public virtual PurchaseOrder PurchaseOrder { get; set; }
        public virtual RawMaterial RawMaterial { get; set; }
    }
}
