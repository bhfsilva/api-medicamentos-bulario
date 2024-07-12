package medicamentos.api.service;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import medicamentos.api.consumer.BularioAnvisaApiConsumer;
import medicamentos.api.domain.anvisaApi.AnvisaApiDTO;
import medicamentos.api.domain.medicamento.Medicamento;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.stereotype.Service;

import java.lang.reflect.Type;
import java.util.List;

@Service
public class MedicamentosService {

    @Autowired
    private BularioAnvisaApiConsumer bularioApiConsumer;

    public List<Medicamento> getPageMedicamentos() {
        String jsonResponse = bularioApiConsumer.getPageMedicamentos();
        Gson gson = new Gson();
        Type responseType = new TypeToken<PageImpl<Medicamento>>() {}.getType();
        PageImpl<Medicamento> objectResponse = gson.fromJson(jsonResponse, responseType);

        return objectResponse.getContent();
    }
}
