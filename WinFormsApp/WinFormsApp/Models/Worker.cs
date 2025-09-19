using System;
using System.Collections.Generic;

namespace WinFormsApp.Models
{
    public class Worker
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Position { get; set; }
        public DateTime HireDate { get; set; }
        public double HourlyRate { get; set; }
        public virtual ICollection<Shift> Shifts { get; set; }
    }
}
