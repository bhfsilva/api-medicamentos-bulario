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

import java.util.List;

@RestController
@RequestMapping("/medicamentos")
public class MedicamentosController {

    @Autowired
    private AnvisaApiConsumer anvisaApiConsumer;

    @Autowired
    private MedicamentosService medicamentosService;

    @GetMapping
    @GetMapping("/**")
    public AnvisaApiResponse<MedicamentoCompleto> getMedicamentoByNumeroProcesso(
            @RequestParam(required = false, defaultValue = "") String numeroProcesso,
            @PageableDefault(size = 10, page = 1) Pageable pagination
    ) {
        return medicamentosService.getMedicamentoCompleto(numeroProcesso, pagination);
    }

    @GetMapping("/{numeroProcesso}")
    public AnvisaApiResponse<MedicamentoCompleto> getMedicamentoByNumeroProcesso(
            @PathVariable String numeroProcesso,
            @PageableDefault(size = 10, page = 1) Pageable pagination
    ) {
    @GetMapping("/disponiveis/{prefixoNomeMedicamento}")
    public List<String> getNomeMedicamentos(@PathVariable String prefixoNomeMedicamento) {
        return anvisaApiConsumer.getNomeMedicamentos(prefixoNomeMedicamento);
    }
}
