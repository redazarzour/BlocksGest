using System;
using System.Collections.Generic;

namespace WinFormsApp.Models
{
    public class PurchaseOrder
    {
        public int Id { get; set; }
        public int SupplierId { get; set; }
        public DateTime OrderDate { get; set; }
        public DateTime DeliveryDate { get; set; }
        public string Status { get; set; }
        public double TotalAmount { get; set; }
        public virtual Supplier Supplier { get; set; }
        public virtual ICollection<PurchaseOrderItem> Items { get; set; }
    }
}
