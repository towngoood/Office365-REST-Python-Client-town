import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;

public class Office365RestApiExample {
    public static void main(String[] args) throws URISyntaxException, ClientProtocolException, IOException {
        String accessToken = "YOUR_ACCESS_TOKEN_HERE";
        String url = "https://outlook.office.com/api/v2.0/me/messages";
        HttpClient client = HttpClientBuilder.create().build();
        HttpGet request = new HttpGet(new URI(url));
        request.addHeader("Authorization", "Bearer " + accessToken);
        HttpResponse response = client.execute(request);
        HttpEntity entity = response.getEntity();
        String content = EntityUtils.toString(entity);
        System.out.println(content);
    }
}

# 3125
