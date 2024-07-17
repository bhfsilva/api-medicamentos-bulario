package medicamentos.api.consumer.bulario;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import medicamentos.api.infra.AnvisaWebClient;
import medicamentos.api.domain.anvisaApi.AnvisaApiDTO;
import medicamentos.api.domain.medicamento.Medicamento;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Component;

import java.lang.reflect.Type;

@Component
public class BularioAnvisaApiConsumer {

    @Autowired
    private AnvisaWebClient anvisaWebClient;

    public AnvisaApiDTO<Medicamento> getMedicamentos(String nomeMedicamento, Pageable pagination) {

        String endpoint = "/consulta/bulario/?filter[nomeProduto]=" + nomeMedicamento;

        String jsonResponse = anvisaWebClient.get(endpoint, pagination);
        Gson gson = new Gson();
        Type responseType = new TypeToken<AnvisaApiDTO<Medicamento>>() {}.getType();
        AnvisaApiDTO<Medicamento> objectResponse = gson.fromJson(jsonResponse, responseType);
        objectResponse.setNumber(objectResponse.getNumber() + 1);
        return objectResponse;
    }
}