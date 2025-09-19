using System;

namespace WinFormsApp.Models
{
    public class Payment
    {
        public int Id { get; set; }
        public int SalesTransactionId { get; set; }
        public double Amount { get; set; }
        public DateTime PaymentDate { get; set; }
        public string Status { get; set; }
        public virtual SalesTransaction SalesTransaction { get; set; }
    }
}
