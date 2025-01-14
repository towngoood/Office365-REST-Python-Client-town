using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Office365RestClient
{
    class Program
    {
        // Replace these values with your own tenant, client id, client secret and site url
        private static readonly string tenant = "contoso.onmicrosoft.com";
        private static readonly string clientId = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx";
        private static readonly string clientSecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        private static readonly string siteUrl = "https://contoso.sharepoint.com/sites/demo";

        // The resource and authority endpoints for SharePoint Online
        private static readonly string resource = "https://contoso.sharepoint.com";
        private static readonly string authority = "https://login.microsoftonline.com/" + tenant;

        // The base address for SharePoint REST API
        private static readonly string baseAddress = siteUrl + "/_api/";

        // The HttpClient instance for sending requests
        private static readonly HttpClient httpClient = new HttpClient();

        static async Task Main(string[] args)
        {
            // Get the access token from Azure AD
            var accessToken = await GetAccessTokenAsync();

            // Set the authorization header with the access token
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", accessToken);

            // Get the current user information
            var user = await GetCurrentUserAsync();

            // Print the user login name
            Console.WriteLine("Current user: " + user.LoginName);
        }

        // A method to get the access token from Azure AD using client credentials flow
        private static async Task<string> GetAccessTokenAsync()
        {
            // Create a new request with the authority endpoint
            var request = new HttpRequestMessage(HttpMethod.Post, authority + "/oauth2/token");

            // Set the request content with the required parameters
            request.Content = new FormUrlEncodedContent(new[]
            {
                new KeyValuePair<string, string>("grant_type", "client_credentials"),
                new KeyValuePair<string, string>("client_id", clientId),
                new KeyValuePair<string, string>("client_secret", clientSecret),
                new KeyValuePair<string, string>("resource", resource)
            });

            // Send the request and get the response
            var response = await httpClient.SendAsync(request);

            // Ensure the response status code is successful
            response.EnsureSuccessStatusCode();

            // Read the response content as a string
            var content = await response.Content.ReadAsStringAsync();

            // Deserialize the content as a JSON object
            var json = JsonConvert.DeserializeObject<dynamic>(content);

            // Return the access token from the JSON object
            return json.access_token;
        }

        // A method to get the current user information from SharePoint REST API
        private static async Task<User> GetCurrentUserAsync()
        {
            // Create a new request with the base address and the endpoint for the current user
            var request = new HttpRequestMessage(HttpMethod.Get, baseAddress + "web/currentuser");

            // Set the request header to accept JSON response
            request.Headers.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

            // Send the request and get the response
            var response = await httpClient.SendAsync(request);

            // Ensure the response status code is successful
            response.EnsureSuccessStatusCode();

            // Read the response content as a string
            var content = await response.Content.ReadAsStringAsync();

            // Deserialize the content as a JSON object
            var json = JsonConvert.DeserializeObject<dynamic>(content);

            // Return the user object from the JSON object
            return json.d.ToObject<User>();
        }
    }

    // A class to represent a user object
    class User
    {
        public string LoginName { get; set; }
    }
}
using System.Text;

namespace Office365RestClient
{
    class Program
    {
        // Other methods and classes remain the same...

        static async Task Main(string[] args)
        {
            // Get the access token from Azure AD
            var accessToken = await GetAccessTokenAsync();

            // Set the authorization header with the access token
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", accessToken);

            // Get the current user information
            var user = await GetCurrentUserAsync();

            // Print the user login name
            Console.WriteLine("Current user: " + user.LoginName);

            // Create a new list item
            var newItem = await CreateListItemAsync("DemoList", new { Title = "New Item" });

            // Print the new item ID
            Console.WriteLine("New item ID: " + newItem.Id);
        }

        // A method to create a new list item in a SharePoint list
        private static async Task<ListItem> CreateListItemAsync(string listName, object item)
        {
            // Create a new request with the base address and the endpoint for the list items
            var request = new HttpRequestMessage(HttpMethod.Post, baseAddress + $"web/lists/getbytitle('{listName}')/items");

            // Set the request header to accept JSON response
            request.Headers.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

            // Set the request content with the item data as JSON
            request.Content = new StringContent(JsonConvert.SerializeObject(item), Encoding.UTF8, "application/json");

            // Send the request and get the response
            var response = await httpClient.SendAsync(request);

            // Ensure the response status code is successful
            response.EnsureSuccessStatusCode();

            // Read the response content as a string
            var content = await response.Content.ReadAsStringAsync();

            // Deserialize the content as a JSON object
            var json = JsonConvert.DeserializeObject<dynamic>(content);

            // Return the list item object from the JSON object
            return json.d.ToObject<ListItem>();
        }
    }

    // A class to represent a list item object
    class ListItem
    {
        public int Id { get; set; }
    }
}
# test
