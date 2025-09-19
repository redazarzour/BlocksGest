using System.Data.Entity;
using WinFormsApp.Models;

namespace WinFormsApp.Data
{
    public class AppContext : DbContext
    {
        public AppContext() : base("name=AppContext")
        {
        }

        public DbSet<RawMaterial> RawMaterials { get; set; }
        public DbSet<FinishedGood> FinishedGoods { get; set; }
        public DbSet<WorkInProgress> WorkInProgresses { get; set; }
        public DbSet<ProductionSchedule> ProductionSchedules { get; set; }
        public DbSet<SalesTransaction> SalesTransactions { get; set; }
        public DbSet<Delivery> Deliveries { get; set; }
        public DbSet<Payment> Payments { get; set; }
        public DbSet<Worker> Workers { get; set; }
        public DbSet<Shift> Shifts { get; set; }
        public DbSet<Supplier> Suppliers { get; set; }
        public DbSet<PurchaseOrder> PurchaseOrders { get; set; }
        public DbSet<PurchaseOrderItem> PurchaseOrderItems { get; set; }
        public DbSet<QualityCheck> QualityChecks { get; set; }
    }
}
