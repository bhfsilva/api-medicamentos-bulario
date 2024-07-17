package medicamentos.api.service;

import medicamentos.api.consumer.AnvisaApiConsumer;
import medicamentos.api.domain.anvisaApiResponse.AnvisaApiResponse;
import medicamentos.api.domain.medicamento.Medicamento;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

@Service
public class MedicamentosService {

    @Autowired
    private AnvisaApiConsumer bularioApiConsumer;

    public AnvisaApiResponse<Medicamento> getMedicamentos(Pageable pagination) {

        return null;
    }
}
