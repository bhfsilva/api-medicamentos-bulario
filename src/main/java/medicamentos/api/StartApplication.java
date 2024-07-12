package medicamentos.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.http.HttpHeaders;
import org.springframework.web.reactive.function.client.WebClient;

@SpringBootApplication(exclude = DataSourceAutoConfiguration.class)
public class StartApplication {

	private void configureDefaultHeaders(final HttpHeaders headers) {
		headers.add(HttpHeaders.ACCEPT, "application/json, text/plain, */*");
		headers.add(HttpHeaders.AUTHORIZATION, "Guest");
		headers.add(HttpHeaders.REFERER, "https://consultas.anvisa.gov.br/");
	}

	@Bean
	public WebClient webClient(WebClient.Builder builder) {
		return builder
			.baseUrl("https://consultas.anvisa.gov.br/api")
			.defaultHeaders(this::configureDefaultHeaders)
			.build();
	}

	public static void main(String[] args) {
		SpringApplication.run(StartApplication.class, args);
	}

}
