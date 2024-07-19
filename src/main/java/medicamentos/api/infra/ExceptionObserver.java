package medicamentos.api.infra;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.reactive.function.client.WebClientResponseException;

@RestControllerAdvice
public class ExceptionObserver {

    @ExceptionHandler(WebClientResponseException.NotFound.class)
    public ResponseEntity HTTPNotFound() {
        return ResponseEntity.notFound().build();
    }
}
