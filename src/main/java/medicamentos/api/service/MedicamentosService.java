package medicamentos.api.service;

import medicamentos.api.consumer.bulario.BularioAnvisaApiConsumer;
import medicamentos.api.domain.anvisaApi.AnvisaApiDTO;
import medicamentos.api.domain.medicamento.Medicamento;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

@Service
public class MedicamentosService {

    @Autowired
    private BularioAnvisaApiConsumer bularioApiConsumer;

    public AnvisaApiDTO<Medicamento> getMedicamentos(Pageable pagination) {

        return null;
    }
}
