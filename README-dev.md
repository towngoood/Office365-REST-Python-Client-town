# Installing to virtualenv
In the pipenv/poetry era one would already forget these commands...

```bash
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt
```

# Running tests

Most of the tests are end-to-end - operations are invoked against actual tenant (not mocked). 
So one has to configure his/her office/sharepoint credentials. 
To do so, create a file ```.env``` like this (replace the bracketed values by your values):

```
export office365_python_sdk_securevars='{username};{password};{client_id};{client_password}'
```

This file is in .gitignore, so it will never be committed.

```bash
$ . .env   # source it to export the variable
$ pytest ...  # run the test(s) you need...
```

#### Configure Tenant

Roles:

- Global reader
- Groups admin
- Search admin
- SharePoint admin
- Teams service admin
- Users admin

- # Ensure you have the necessary roles assigned to your account
# You can use the Azure portal or PowerShell to assign these roles

# Example PowerShell command to assign a role
$role = Get-AzureADDirectoryRole | Where-Object { $_.DisplayName -eq "Global Reader" }
Add-AzureADDirectoryRoleMember -ObjectId $role.ObjectId -RefObjectId <your-user-object-id>

# After configuring the roles, you can proceed with running the tests
$ pytest tests/  # Adjust the path to your test directory as needed

# If you encounter any issues, make sure to check the logs for detailed error messages
# and verify that your credentials and roles are correctly configured.

## 🛠️ Debugging Tips

When running end-to-end tests, you may encounter issues related to authentication, permissions, or API throttling. Here are some tips to help you debug effectively:

- ✅ **Enable verbose logging** by setting the environment variable:
  ```bash
  export OFFICE365_SDK_LOGLEVEL=DEBUG
  ```
  This will print detailed request/response logs to the console.

- 🔍 **Check token expiration**: If you're using `client_id` and `client_password`, ensure the token is refreshed properly. You may need to re-authenticate or regenerate secrets.

- 🔐 **Validate permissions**: Use the Microsoft Graph Explorer or PowerShell to confirm your account has the necessary roles.

- 📄 **Inspect response payloads**: Many SDK methods return structured error messages. Log or print them to understand the root cause.

---

## 📈 Test Coverage

To measure how much of your code is covered by tests, you can use `pytest-cov`:

```bash
$ pip install pytest-cov
$ pytest --cov=your_module tests/
```

This will generate a coverage report. For HTML output:

```bash
$ pytest --cov=your_module --cov-report=html tests/
$ open htmlcov/index.html
```

---

## 🔄 CI/CD Integration

To integrate these tests into a CI/CD pipeline (e.g., GitHub Actions, GitLab CI), follow these steps:

1. **Store secrets securely** using encrypted secrets or vaults.
2. **Set up environment variables** in your CI config file:
   ```yaml
   env:
     office365_python_sdk_securevars: ${{ secrets.OFFICE365_VARS }}
   ```
3. **Install dependencies and run tests**:
   ```yaml
   steps:
     - name: Set up Python
       uses: actions/setup-python@v4
       with:
         python-version: '3.10'
     - name: Install dependencies
       run: |
         python -m venv venv
         . venv/bin/activate
         pip install -r requirements.txt
         pip install -r requirements-dev.txt
     - name: Run tests
       run: |
         . .env
         pytest tests/
   ```

---

## ❗ Common Pitfalls

- **Missing roles**: If you get `403 Forbidden`, double-check your Azure AD role assignments.
- **Incorrect `.env` format**: Ensure there are no extra spaces or missing semicolons.
- **Rate limits**: Microsoft Graph API enforces throttling. Add retry logic or stagger test execution.
- **Multi-factor authentication (MFA)**: If your account uses MFA, consider using app passwords or service principals.

---

## 📚 Additional Resources

- [Microsoft Graph API Documentation](https://learn.microsoft.com/en-us/graph/)
- [Azure AD Role Management](https://learn.microsoft.com/en-us/azure/active-directory/roles/)
- [Office365 Python SDK GitHub](https://github.com/vgrem/Office365-REST-Python-Client)

---
