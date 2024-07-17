package medicamentos.api.controller;

import medicamentos.api.consumer.AnvisaApiConsumer;
import medicamentos.api.domain.anvisaApiResponse.AnvisaApiResponse;
import medicamentos.api.domain.medicamento.Medicamento;
import medicamentos.api.domain.medicamentoCompleto.MedicamentoCompleto;
import medicamentos.api.service.MedicamentosService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/medicamentos")
public class MedicamentosController {

    @Autowired
    private AnvisaApiConsumer bularioApiConsumer;

    @Autowired
    private MedicamentosService service;

    @GetMapping
    public AnvisaApiResponse<Medicamento> getMedicamentos(
            @RequestParam(required = false, defaultValue = "") String nomeMedicamento,
            @PageableDefault(size = 10, page = 1) Pageable pagination
    ) {
        return bularioApiConsumer.getMedicamentos(nomeMedicamento, pagination);
    }

    @GetMapping("/{numeroProcesso}")
    public AnvisaApiResponse<MedicamentoCompleto> getMedicamentoByNumeroProcesso(
            @PathVariable String numeroProcesso,
            @PageableDefault(size = 10, page = 1) Pageable pagination
    ) {
        return bularioApiConsumer.getMedicamentoByNumeroProcesso(numeroProcesso, pagination);
    }
}
