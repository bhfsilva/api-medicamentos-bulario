package medicamentos.api.service;

import lombok.NoArgsConstructor;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@NoArgsConstructor
public class ImageScraperService {

    public String scrapMedicamentoImage(String search) {
        ChromeOptions chromeOptions = new ChromeOptions();
        chromeOptions.addArguments("--headless=new");
        ChromeDriver driver = new ChromeDriver(chromeOptions);
        String URL = "https://www.google.com/search?tbm=isch&q=";
        driver.get(URL + search.replace(" ", "+"));
        List<WebElement> imgList = driver.findElements(By.xpath("//div[@style=\"position:relative\"]//img"));
        if (!imgList.isEmpty()) {
            String imageSource = imgList.get(0).getAttribute("src").split(",")[1];
            driver.quit();
            return imageSource;
        }
        driver.quit();
        return "";
    }
}
