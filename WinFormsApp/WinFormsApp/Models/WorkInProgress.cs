using System;

namespace WinFormsApp.Models
{
    public class WorkInProgress
    {
        public int Id { get; set; }
        public string ProductName { get; set; }
        public int Quantity { get; set; }
        public DateTime StartDate { get; set; }
        public string BlockType { get; set; }
    }
}
