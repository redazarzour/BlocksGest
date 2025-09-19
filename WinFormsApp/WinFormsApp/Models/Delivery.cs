using System;

namespace WinFormsApp.Models
{
    public class Delivery
    {
        public int Id { get; set; }
        public int SalesTransactionId { get; set; }
        public int Quantity { get; set; }
        public DateTime DeliveryDate { get; set; }
        public string Status { get; set; }
        public virtual SalesTransaction SalesTransaction { get; set; }
    }
}
