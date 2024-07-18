package medicamentos.api.service;

import medicamentos.api.consumer.AnvisaApiConsumer;
import medicamentos.api.domain.anvisaApiResponse.AnvisaApiResponse;
import medicamentos.api.domain.medicamentoCompleto.MedicamentoCompleto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

@Service
public class MedicamentosService {

    @Autowired
    private AnvisaApiConsumer anvisaApiConsumer;

    public AnvisaApiResponse<MedicamentoCompleto> getMedicamentoCompleto(String numeroProcesso, Pageable pagination) {
        //@TODO adicionar busca por imagem
        return anvisaApiConsumer.getMedicamentoByNumeroProcesso(numeroProcesso, pagination);
    }
}
