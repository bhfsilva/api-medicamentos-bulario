package medicamentos.api.consumer;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpMethod;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.util.UriComponentsBuilder;
import reactor.core.publisher.Mono;

@Service
public class BularioAnvisaApiConsumer {

    @Autowired
    private WebClient webClient;

    public String getPageMedicamentos(Pageable pagination) {

        Integer numPage = pagination.getPageNumber() != 0 ? pagination.getPageNumber() : 1;
        Integer contentSize = pagination.getPageSize();

        String paginationParams = UriComponentsBuilder.newInstance()
                .queryParam("page", numPage)
                .queryParam("size", contentSize)
                .build().toUriString();

        Mono<String> monoPageAnvisaApi = this.webClient.method(HttpMethod.GET)
            .uri("/consulta/bulario/" + paginationParams)
            .retrieve()
            .bodyToMono(String.class);
        return monoPageAnvisaApi.block();
    }
}