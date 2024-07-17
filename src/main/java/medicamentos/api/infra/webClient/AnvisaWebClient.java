package medicamentos.api.infra.webClient;

import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.util.UriComponentsBuilder;
import reactor.core.publisher.Mono;

@Component
public class AnvisaWebClient {

    private final String ANVISA_WEBSITE = "https://consultas.anvisa.gov.br";

    private void configureDefaultHeaders(final HttpHeaders headers) {
        headers.add(HttpHeaders.ACCEPT, "application/json, text/plain, */*");
        headers.add(HttpHeaders.AUTHORIZATION, "Guest");
        headers.add(HttpHeaders.REFERER, ANVISA_WEBSITE);
    }

    public WebClient anvisaConsumerClient() {
        return WebClient
                .builder()
                .baseUrl(ANVISA_WEBSITE + "/api")
                .defaultHeaders(this::configureDefaultHeaders)
                .build();
    }

    public String get(String resource, Pageable pagination) {

        Integer numPage = pagination.getPageNumber() != 0 ? pagination.getPageNumber() : 1;
        Integer contentSize = pagination.getPageSize();

        String paginationParams = UriComponentsBuilder.newInstance()
                .queryParam("page", numPage)
                .queryParam("size", contentSize)
                .build().toUriString();

        String endpoint = resource + paginationParams.replace("?", "&");;
        Mono<String> monoPageAnvisaApi = this.anvisaConsumerClient().method(HttpMethod.GET)
                .uri(endpoint)
                .retrieve()
                .bodyToMono(String.class);
        return monoPageAnvisaApi.block();
    }
}
