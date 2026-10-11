# Installation

## What this is for

Install the VEDA Excel Add-In on a PC that already has Microsoft Excel. The add-in is the **VedaExcelAddIn** package on the same VEDA 2.0 release (`VedaExcelAddIn_<version>.zip`). Install from those extracted files. Excel does not download or update the add-in on its own.

## What you need

- Microsoft Excel 2016 or later ([check supported version](#veda-supported-versions))
- `VedaExcelAddIn_<version>.zip` from the VEDA 2.0 GitHub release (with VEDA 5.0.0.0 this is `VedaExcelAddIn_1.0.0.20.zip`)
- Permission to install software for your Windows user (ClickOnce / VSTO install)

<div markdown="0">
<dialog id="veda-supported-versions" class="veda-supported-dialog">
  <form method="dialog">
    <button class="veda-supported-dialog__close" type="submit" aria-label="Close">&times;</button>
  </form>
  <p><strong>Supported versions</strong></p>
  <p>Tested combinations for Microsoft Excel 2016 or later.</p>
  <table>
    <thead>
      <tr>
        <th>Windows</th>
        <th>Excel versions</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Windows 11</td>
        <td>Excel 2016, 2019, 2021, 2024, and Microsoft 365</td>
      </tr>
      <tr>
        <td>Servers 2019</td>
        <td>Excel 2016, 2019, 2021, 2024, and Microsoft 365</td>
      </tr>
      <tr>
        <td>Servers 2022</td>
        <td>Excel 2016, 2019, 2021, 2024, and Microsoft 365</td>
      </tr>
    </tbody>
  </table>
</dialog>
<script>
(function () {
  var link = document.querySelector('a[href="#veda-supported-versions"]');
  var dialog = document.getElementById("veda-supported-versions");
  if (!link || !dialog || !dialog.showModal) {
    return;
  }
  link.addEventListener("click", function (event) {
    event.preventDefault();
    dialog.showModal();
  });
  dialog.addEventListener("click", function (event) {
    if (event.target === dialog) {
      dialog.close();
    }
  });
})();
</script>
</div>

## How to install

1. Fully **quit Excel** (close every Excel window).
2. Download `VedaExcelAddIn_<version>.zip` from the VEDA 2.0 release and extract it.
3. Run the **`.vsto`** file in that folder (`Veda.ExcelAddIn.vsto`).
4. Follow the ClickOnce / VSTO install prompts to install **VEDA Excel Add-In**.
5. Start Excel.
6. Confirm the **VEDA** tab appears on the ribbon.

Optional check: open **VEDA → About** and note the version.

## Upgrade

1. Fully quit Excel.
2. Uninstall **VEDA Excel Add-In** from Windows **Settings → Apps** (or **Programs and Features**). Remove every existing entry for it.
3. Download `VedaExcelAddIn_<version>.zip` from the **newer** VEDA 2.0 release and extract it.
4. Run `Veda.ExcelAddIn.vsto` and follow the install prompts.
5. Start Excel and confirm the **VEDA** tab and About version.

## After install

- Start **VEDA 2.0** before using add-in features that need the model ([How we connect](how-we-connect.md)).
- Open a workbook under an imported model ([How models are linked](how-models-are-linked.md)).

## If the VEDA tab is missing

See [Troubleshooting](troubleshooting.md) — check that the COM add-in is enabled and that Excel was fully restarted after install.
