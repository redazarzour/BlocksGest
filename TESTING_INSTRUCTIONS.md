# Testing Instructions

Follow these instructions to test the WinForms application.

## 1. Set up the project in Visual Studio

1.  Open Visual Studio.
2.  Create a new "Windows Forms App (.NET Framework)" project. Name it `WinFormsApp`.
3.  In the Solution Explorer, right-click on the project and select "Add > Existing Item...".
4.  Navigate to the `WinFormsApp/WinFormsApp` directory and add all the `.cs` files from the `Data`, `Models`, and `Views` directories.
5.  You will be asked if you want to replace the existing `Program.cs` and `Form1.cs` files. You can delete the `Form1.cs`, `Form1.Designer.cs` and `Form1.resx` files that were created by default.
6.  You will need to create a `Program.cs` file with the following content:
    ```csharp
    using System;
    using System.Windows.Forms;
    using WinFormsApp.Views;

    namespace WinFormsApp
    {
        static class Program
        {
            [STAThread]
            static void Main()
            {
                Application.EnableVisualStyles();
                Application.SetCompatibleTextRenderingDefault(false);
                Application.Run(new MainForm());
            }
        }
    }
    ```

## 2. Install necessary packages

1.  In the Solution Explorer, right-click on the project and select "Manage NuGet Packages...".
2.  Go to the "Browse" tab and search for "EntityFramework".
3.  Install the `EntityFramework` package (version 6.x.x).

## 3. Configure the database connection

1.  Open the `App.config` file in your project.
2.  Add the following connection string inside the `<configuration>` section:

    ```xml
    <connectionStrings>
      <add name="AppContext"
           connectionString="Data Source=(LocalDb)\MSSQLLocalDB;Initial Catalog=WinFormsApp.Data.AppContext;Integrated Security=SSPI;"
           providerName="System.Data.SqlClient"/>
    </connectionStrings>
    ```
    This will create a local database named `WinFormsApp.Data.AppContext` when the application is run for the first time.

3. Also add the following section to the `App.config` file, inside the `<configuration>` section:
    ```xml
    <entityFramework>
      <providers>
        <provider invariantName="System.Data.SqlClient" type="System.Data.Entity.SqlServer.SqlProviderServices, EntityFramework.SqlServer" />
      </providers>
    </entityFramework>
    ```

## 4. Running the application

1.  Build the project by pressing `Ctrl+Shift+B`.
2.  Run the application by pressing `F5`.

## 5. Testing the implemented features

### Inventory Tab

1.  The application should open with the "Inventory" tab selected.
2.  The grid should be empty at first.
3.  Click the "Add" button. The "Add Raw Material" form should appear.
4.  Enter the details for a new raw material and click "OK".
5.  The new raw material should appear in the grid.
6.  Select the newly added raw material and click the "Edit" button. The "Edit Raw Material" form should appear.
7.  Change some of the details and click "OK".
8.  The changes should be reflected in the grid.
9.  Select the raw material and click the "Delete" button. A confirmation message should appear.
10. Click "Yes". The raw material should be removed from the grid.

### Finished Goods Tab

1.  Click on the "Production" tab.
2.  The grid should be empty at first.
3.  Click the "Add" button. The "Add Finished Good" form should appear.
4.  Enter the details for a new finished good and click "OK".
5.  The new finished good should appear in the grid.
6.  Select the newly added finished good and click the "Edit" button. The "Edit Finished Good" form should appear.
7.  Change some of the details and click "OK".
8.  The changes should be reflected in the grid.
9.  Select the finished good and click the "Delete" button. A confirmation message should appear.
10. Click "Yes". The finished good should be removed from the grid.
