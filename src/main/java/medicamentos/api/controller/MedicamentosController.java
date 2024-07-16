package medicamentos.api.controller;

import medicamentos.api.domain.anvisaApi.AnvisaApiDTO;
import medicamentos.api.domain.medicamento.Medicamento;
import medicamentos.api.service.MedicamentosService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/medicamentos")
public class MedicamentosController {

    @Autowired
    private MedicamentosService service;

    @GetMapping
    public AnvisaApiDTO<Medicamento> getMedicamentos(Pageable pagination) {
        return service.getPageMedicamentos(pagination);
    }

}
