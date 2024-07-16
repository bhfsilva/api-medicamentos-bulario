package medicamentos.api.service;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import medicamentos.api.consumer.BularioAnvisaApiConsumer;
import medicamentos.api.domain.anvisaApi.AnvisaApiDTO;
import medicamentos.api.domain.medicamento.Medicamento;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.lang.reflect.Type;
import java.util.List;

@Service
public class MedicamentosService {

    @Autowired
    private BularioAnvisaApiConsumer bularioApiConsumer;

    public AnvisaApiDTO<Medicamento> getPageMedicamentos(Pageable pagination) {
        String jsonResponse = bularioApiConsumer.getPageMedicamentos(pagination);
        Gson gson = new Gson();
        Type responseType = new TypeToken<AnvisaApiDTO<Medicamento>>() {}.getType();
        AnvisaApiDTO<Medicamento> objectResponse = gson.fromJson(jsonResponse, responseType);

        objectResponse.setNumber(objectResponse.getNumber() + 1);

        return objectResponse;
    }
}
