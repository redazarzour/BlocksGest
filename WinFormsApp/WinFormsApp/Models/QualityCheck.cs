using System;

namespace WinFormsApp.Models
{
    public class QualityCheck
    {
        public int Id { get; set; }
        public string ProductName { get; set; }
        public string BatchNumber { get; set; }
        public DateTime CheckDate { get; set; }
        public string InspectorName { get; set; }
        public bool Passed { get; set; }
        public string Notes { get; set; }
    }
}
