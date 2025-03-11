import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;

public class Office365RestApiExample {
    public static void main(String[] args) {
        String accessToken = "YOUR_ACCESS_TOKEN_HERE";
        String url = "https://outlook.office.com/api/v2.0/me/messages";
        
        // 配置请求超时
        RequestConfig requestConfig = RequestConfig.custom()
            .setConnectTimeout(5000)  // 连接超时时间
            .setSocketTimeout(5000)   // 读取超时时间
            .build();
        
        HttpClient client = HttpClientBuilder.create()
            .setDefaultRequestConfig(requestConfig)
            .build();
        
        HttpGet request = new HttpGet(URI.create(url));
        request.addHeader("Authorization", "Bearer " + accessToken);
        
        try {
            HttpResponse response = client.execute(request);
            int statusCode = response.getStatusLine().getStatusCode();
            
            if (statusCode >= 200 && statusCode < 300) {
                HttpEntity entity = response.getEntity();
                String content = EntityUtils.toString(entity);
                System.out.println("邮件数据获取成功：\n" + content);
                
                // 这里可以添加JSON解析逻辑（如使用Jackson/Gson）
                // parseEmails(content);
                
            } else {
                handleErrorResponse(response, statusCode);
            }
        } catch (ClientProtocolException e) {
            System.err.println("协议错误: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("I/O 错误: " + e.getMessage());
        } finally {
            // HttpClient实例可以重复使用，不需要关闭
        }
    }

    private static void handleErrorResponse(HttpResponse response, int statusCode) throws IOException {
        HttpEntity errorEntity = response.getEntity();
        String errorContent = errorEntity != null ? EntityUtils.toString(errorEntity) : "";
        
        switch (statusCode) {
            case 401:
                System.err.println("认证失败（401）: 检查访问令牌是否有效");
                break;
            case 403:
                System.err.println("权限不足（403）: " + errorContent);
                break;
            case 404:
                System.err.println("资源未找到（404）: 确认API端点是否正确");
                break;
            case 500:
                System.err.println("服务器内部错误（500）: " + errorContent);
                break;
            default:
                System.err.println("HTTP错误 " + statusCode + ": " + errorContent);
        }
    }
    
    // 示例：解析邮件数据的JSON响应（需要添加Jackson/Gson依赖）
    /* private static void parseEmails(String json) {
        ObjectMapper mapper = new ObjectMapper();
        try {
            JsonNode root = mapper.readTree(json);
            // 解析逻辑...
        } catch (IOException e) {
            e.printStackTrace();
        }
    } */
}
