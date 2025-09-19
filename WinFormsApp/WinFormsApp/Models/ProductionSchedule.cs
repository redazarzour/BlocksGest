using System;

namespace WinFormsApp.Models
{
    public class ProductionSchedule
    {
        public int Id { get; set; }
        public string ProductName { get; set; }
        public int Quantity { get; set; }
        public DateTime ScheduledDate { get; set; }
        public string BlockType { get; set; }
    }
}
