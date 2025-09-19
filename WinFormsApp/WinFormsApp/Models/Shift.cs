using System;

namespace WinFormsApp.Models
{
    public class Shift
    {
        public int Id { get; set; }
        public int WorkerId { get; set; }
        public DateTime StartTime { get; set; }
        public DateTime EndTime { get; set; }
        public double HoursWorked { get; set; }
        public virtual Worker Worker { get; set; }
    }
}
