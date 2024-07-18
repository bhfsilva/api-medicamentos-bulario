package medicamentos.api.domain.medicamentoCompleto;

import com.google.gson.annotations.SerializedName;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class EmpresaFarmaceutica {
    String razaoSocial;
    String cnpj;
}
