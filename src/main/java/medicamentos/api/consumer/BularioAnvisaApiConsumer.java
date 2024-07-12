package medicamentos.api.consumer;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpMethod;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

@Service
public class BularioAnvisaApiConsumer {

    @Autowired
    private WebClient webClient;

    public String getPageMedicamentos() {
        Mono<String> monoPageAnvisaApi = this.webClient.method(HttpMethod.GET)
            .uri("/consulta/bulario/")
            .retrieve()
            .bodyToMono(String.class);
        return monoPageAnvisaApi.block();
    }
}
