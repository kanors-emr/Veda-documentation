#############
Excel Errors
#############

Error loading type library/DLL. (Exception from HRESULT: 0x80029C4A)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Issue**: Unable to cast COM object of type 'Microsoft.Office.Interop.Excel.ApplicationClass' to interface type 'Microsoft.Office.Interop.Excel._Application'. This operation failed because the Query Interface call on the COM component for the interface with IID '{000208D5-0000-0000-C000-000000000046}' failed due to the following error: **Error loading type library/DLL. (Exception from HRESULT: 0x80029C4A (TYPE_E_CANTLOADLIBRARY)**).

**Solution 1**: "Repair" Office Installation from the Add/Remove programs in Control Panel
    * Right Click on Start Menu
    * Click Apps and Features
    * Search Microsoft Office (either Office 2007, Office 2010, Office 2013, Office 2016 or Office 365 and so on...)
    * Click Microsoft Office
    * Click Modify

    .. image:: images/office_365.jpg
        :width: 400

    * Click Repair

    .. image:: images/office_repair.jpg
        :width: 400

**Solution 2**: "Uninstall" Office Automatically
    .. note::
        Do this only if the **Solution 1** fails

    * `Download`_ the automated tool.
    * Run the **SetupProd_OffScrub.exe** file.
    * Select the version you want to uninstall, and then select Next.
    * Follow through the remaining screens and when prompted, restart your computer.
    * After you restart your computer, the uninstall tool automatically re-opens to complete the final step of the uninstall process. Follow the remaining prompts.
    * If you need to reinstall Office, select the version you want to install and follow those steps: `Microsoft 365`_, `Office 2019`_, `Office 2016`_, `Office 2013`_, `Office 2010`_, or `Office 2007`_.

    .. _Download: https://aka.ms/SaRA-OfficeUninstallFromPC
    .. _Microsoft 365: https://support.office.com/article/4414eaaf-0478-48be-9c42-23adc4716658
    .. _Office 2019: https://support.office.com/article/4414eaaf-0478-48be-9c42-23adc4716658
    .. _Office 2016: https://support.office.com/article/7c695b06-6d1a-4917-809c-98ce43f86479
    .. _Office 2013: https://support.office.com/article/7c695b06-6d1a-4917-809c-98ce43f86479
    .. _Office 2010: https://support.office.com/article/1b8f3c9b-bdd2-4a4f-8c88-aa756546529d
    .. _Office 2007: https://support.office.com/article/88a8e329-3335-4f82-abb2-ecea3e319657


The remote procedure call failed. (Exception from HRESULT: 0x800706BE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Issue**: Error in Syncing the model. **The remote procedure call failed. (Exception from HRESULT: 0x800706BE)**.

    .. image:: images/remote_procedure_call_failed.PNG
       :width: 600


**Reason**: The problem was caused by third-party Excel COM plug-ins.

**Solution**: How to disable the plugin: Excel > File > Options > Add-ins > Manage, then choose "COM add-ins" > Go. And then uncheck the problematic plugin.