package medicamentos.api.domain.medicamento;

import com.google.gson.annotations.SerializedName;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
public class Medicamento{

    @SerializedName("idProduto")
    String idMedicamento;

    @SerializedName("numProcesso")
    String numeroProcessoMedicamento;

    @SerializedName("nomeProduto")
    String nomeMedicamento;

    @SerializedName("razaoSocial")
    String nomeEmpresaFarmaceutica;

    String dataAtualizacao;

    @SerializedName("idBulaPacienteProtegido")
    String idBulaPaciente;

    @SerializedName("idBulaProfissionalProtegido")
    String idBulaProfissional;
}
