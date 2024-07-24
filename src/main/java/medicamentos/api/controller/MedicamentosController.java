package medicamentos.api.controller;

import medicamentos.api.consumer.AnvisaApiConsumer;
import medicamentos.api.domain.anvisaApiResponse.AnvisaApiResponse;
import medicamentos.api.domain.medicamento.Medicamento;
import medicamentos.api.domain.medicamentoCompleto.MedicamentoCompleto;
import medicamentos.api.service.MedicamentosService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
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
    public ResponseEntity<AnvisaApiResponse<Medicamento>> getMedicamentos(@PageableDefault(size = 10, page = 1) Pageable pagination) {
        return ResponseEntity.ok(anvisaApiConsumer.getMedicamentos("", pagination));
    }

    @GetMapping("/**")
    public ResponseEntity<AnvisaApiResponse<MedicamentoCompleto>> getMedicamentoByNumeroProcesso(
            @RequestParam(required = false, defaultValue = "") String numeroProcesso,
            @PageableDefault(size = 10, page = 1) Pageable pagination
    ) {
        AnvisaApiResponse<MedicamentoCompleto> response = medicamentosService.getMedicamentoCompleto(numeroProcesso, pagination);
        if (response.getContent().get(0).getMedicamento().getFotoMedicamentoBase64().isBlank()) {
            return ResponseEntity.status(HttpStatus.PARTIAL_CONTENT).body(response);
        }
        return ResponseEntity.ok(response);
    }

    @GetMapping("/{nomeMedicamento}/")
    public ResponseEntity<AnvisaApiResponse<Medicamento>> getMedicamentoByNome(
            @PathVariable String nomeMedicamento,
            @PageableDefault(size = 10, page = 1) Pageable pagination
    ) {
        return ResponseEntity.ok(anvisaApiConsumer.getMedicamentos(nomeMedicamento, pagination));
    }

    @GetMapping("/disponiveis/{prefixoNomeMedicamento}/")
    public ResponseEntity<List<String>> getNomeMedicamentosDisponiveis(@PathVariable String prefixoNomeMedicamento) {
        return ResponseEntity.ok(anvisaApiConsumer.getNomeMedicamentos(prefixoNomeMedicamento));
    }
}
