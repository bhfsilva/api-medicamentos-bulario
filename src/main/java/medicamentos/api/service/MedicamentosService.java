package medicamentos.api.service;

import medicamentos.api.consumer.AnvisaApiConsumer;
import medicamentos.api.domain.anvisaApiResponse.AnvisaApiResponse;
import medicamentos.api.domain.medicamentoCompleto.MedicamentoCompleto;
import medicamentos.api.domain.medicamentoCompleto.Produto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

@Service
public class MedicamentosService {

    @Autowired
    private AnvisaApiConsumer anvisaApiConsumer;

    public AnvisaApiResponse<MedicamentoCompleto> getMedicamentoCompleto(String numeroProcesso, Pageable pagination) {
        AnvisaApiResponse<MedicamentoCompleto> response = anvisaApiConsumer.getMedicamentoByNumeroProcesso(numeroProcesso, pagination);
        Produto medicamento = response.getContent().get(0).getMedicamento();
        String nomeMedicamento = medicamento.getNomeMedicamento();
        String nomeEmpresaFarmaceutica = response.getContent().get(0).getEmpresaFarmaceutica().getRazaoSocial();
        String fotoMedicamentoBase64 = new ImageScraperService().scrapMedicamentoImage("medicamento " + nomeMedicamento + " " + nomeEmpresaFarmaceutica);
        medicamento.setFotoMedicamentoBase64(fotoMedicamentoBase64);
        response.getContent().get(0).setMedicamento(medicamento);
        return response;
    }
}
