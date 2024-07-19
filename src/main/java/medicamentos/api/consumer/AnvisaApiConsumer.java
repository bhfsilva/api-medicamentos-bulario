package medicamentos.api.consumer;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import medicamentos.api.domain.medicamentoCompleto.MedicamentoCompleto;
import medicamentos.api.infra.AnvisaWebClient;
import medicamentos.api.domain.anvisaApiResponse.AnvisaApiResponse;
import medicamentos.api.domain.medicamento.Medicamento;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Component;
import java.lang.reflect.Type;
import java.util.List;

@Component
public class AnvisaApiConsumer {

    @Autowired
    private AnvisaWebClient anvisaWebClient;

    public AnvisaApiResponse<Medicamento> getMedicamentos(String nomeMedicamento, Pageable pagination) {

        String endpoint = "/consulta/bulario/?filter[nomeProduto]=" + nomeMedicamento;

        String jsonResponse = anvisaWebClient.get(endpoint, pagination);
        Gson gson = new Gson();
        Type responseType = new TypeToken<AnvisaApiResponse<Medicamento>>() {}.getType();
        AnvisaApiResponse<Medicamento> objectResponse = gson.fromJson(jsonResponse, responseType);
        objectResponse.setNumber(objectResponse.getNumber() + 1);
        return objectResponse;
    }

    public AnvisaApiResponse<MedicamentoCompleto> getMedicamentoByNumeroProcesso(String numeroProcesso, Pageable pagination) {

        String endpoint = "/consulta/medicamento/produtos/?filter[numeroProcesso]=" + numeroProcesso;

        String jsonResponse = anvisaWebClient.get(endpoint, pagination);
        Gson gson = new Gson();
        Type responseType = new TypeToken<AnvisaApiResponse<MedicamentoCompleto>>() {}.getType();
        AnvisaApiResponse<MedicamentoCompleto> objectResponse = gson.fromJson(jsonResponse, responseType);
        objectResponse.setNumber(objectResponse.getNumber() + 1);
        return objectResponse;
    }

    public List<String> getNomeMedicamentos(String prefixoNomeMedicamento) {

        String endpoint = "/produto/listaMedicamentoBula/" + prefixoNomeMedicamento;

        String jsonResponse = anvisaWebClient.get(endpoint, null);
        Gson gson = new Gson();
        Type responseType = new TypeToken<List<String>>() {}.getType();
        return gson.fromJson(jsonResponse, responseType);
    }
}
