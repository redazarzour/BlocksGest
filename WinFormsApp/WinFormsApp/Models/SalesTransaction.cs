using System;
using System.Collections.Generic;

namespace WinFormsApp.Models
{
    public class SalesTransaction
    {
        public int Id { get; set; }
        public string ProductName { get; set; }
        public int Quantity { get; set; }
        public double TotalAmount { get; set; }
        public DateTime TransactionDate { get; set; }
        public virtual ICollection<Delivery> Deliveries { get; set; }
        public virtual ICollection<Payment> Payments { get; set; }
    }
}
