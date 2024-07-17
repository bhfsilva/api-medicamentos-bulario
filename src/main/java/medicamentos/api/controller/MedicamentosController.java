package medicamentos.api.controller;

import medicamentos.api.consumer.bulario.BularioAnvisaApiConsumer;
import medicamentos.api.domain.anvisaApi.AnvisaApiDTO;
import medicamentos.api.domain.medicamento.Medicamento;
import medicamentos.api.service.MedicamentosService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/medicamentos")
public class MedicamentosController {

    @Autowired
    private BularioAnvisaApiConsumer bularioApiConsumer;

    @Autowired
    private MedicamentosService service;

    @GetMapping
    public AnvisaApiDTO<Medicamento> getMedicamentos(
            @RequestParam(required = false, defaultValue = "") String nomeMedicamento,
            @PageableDefault(size = 10, page = 1) Pageable pagination
    ) {
        return bularioApiConsumer.getMedicamentos(nomeMedicamento, pagination);
    }
}
