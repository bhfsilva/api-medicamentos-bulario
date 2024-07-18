package medicamentos.api.domain.anvisaApiResponse;

import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
public class AnvisaApiResponse<T> {
    List<T> content;
    Integer totalElements;
    Integer totalPages;
    Boolean last;
    Integer numberOfElements;
    Integer size;
    Integer number;
    Boolean first;
    String sort;
}
